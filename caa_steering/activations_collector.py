from abc import ABC, abstractmethod
from configs import SteeringConfig
from typing import Any, Dict, List
import torch

class ActivationsCollector(ABC):
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer=tokenizer

    @abstractmethod
    def collect_activations(positive_texts, negative_texts, config: dict):
        pass


class TorchActivationsCollector(ActivationsCollector):
    @torch.no_grad()
    def _mean_hidden_for_prompts(
        self,
        prompts: List[str],
        layer_idx: int,
        batch_size: int = 8,
        max_len: int = 256,
    ) -> torch.Tensor:
        """
        Compute the mean hidden state for the last token at a chosen layer over a list of prompts.
        """
        hs_sum = None
        count = 0
        model, tokenizer = self.model, self.tokenizer

        tokenizer.padding_side = 'left'

        for i in range(0, len(prompts), batch_size):
            batch = prompts[i:i + batch_size]
            inputs = tokenizer(
                batch, return_tensors="pt", padding=True, truncation=True, max_length=max_len
            ).to(model.device)

            outputs = model(**inputs, output_hidden_states=True, use_cache=False)
            # outputs.hidden_states: [embeddings, layer1, ..., layerN]
            hs = outputs.hidden_states[layer_idx]  # (B, T, H)

            attn_mask = inputs["attention_mask"]
            last_idxs = attn_mask.sum(dim=1) - 1  # (B,)
            last_states = hs[torch.arange(hs.size(0), device=hs.device), last_idxs]  # (B, H)

            if hs_sum is None:
                hs_sum = last_states.sum(dim=0)
            else:
                hs_sum = hs_sum + last_states.sum(dim=0)
            count += last_states.size(0)

        print(f"Have a count of {count} activations")

        return (hs_sum / max(count, 1)).detach()  # (H,)


    @torch.no_grad()
    def collect_activations(
        self,
        pos_texts: List[str],
        neg_texts: List[str],
        config: SteeringConfig,
    ) -> Dict[str, torch.Tensor]:
        """
        Args
        ----
        pos_texts / neg_texts: lists of strings for the two classes
        config:
            layer_idx (int): which hidden_states index to sample (e.g., 18 for mid layer)
            batch_size (int): batching for encoding
            max_len (int): tokenizer max length
            normalize (bool): L2-normalize the delta vector

        Returns
        -------
        dict with:
            pos_mu: (H,) mean hidden for positive class (last-token at layer)
            neg_mu: (H,) mean hidden for negative class
            delta:  (H,) pos_mu - neg_mu (normalized if config['normalize'])
        """
        layer_idx = config.layer_idx
        batch_size = config.batch_size
        max_len = config.max_len
        normalize = config.normalize

        pos_mu = self._mean_hidden_for_prompts(pos_texts, layer_idx, batch_size, max_len)
        neg_mu = self._mean_hidden_for_prompts(neg_texts, layer_idx, batch_size, max_len)
        delta = pos_mu - neg_mu
        if normalize:
            delta = delta / (delta.norm(p=2) + 1e-6)

        return {"pos_mu": pos_mu, "neg_mu": neg_mu, "delta": delta}


