from dataclasses import dataclass
from typing import Optional
import random
import numpy as np
import torch


@dataclass
class SteeringConfig:
    """
    Config for CAA/AA steering runs.

    Notes:
      - Llama-3.2-3B has 28 layers; middle layers (~10-18) tend to work well.
      - Tweak ALPHA_* to adjust steering strength (typical range ≈ 0.5–3.0).
    """
    # ===== Model =====
    model_name: str = "meta-llama/Llama-3.2-3B-Instruct"
    layer_idx: int = 13  # middle layer

    # ===== Steering Strengths =====
    alpha_aa: float = 1.5          # love vs hate (AA)


    # ===== Data / Inference =====
    batch_size: int = 8
    max_len: int = 256              # prompt encoding length when computing directions
    gen_max_new_tokens: int = 128
    normalize: bool = False

    # ===== Repro =====
    seed: int = 42
    device: Optional[str] = None    # "cuda", "cpu", or None to auto-detect

    # --- helpers ---
    def resolved_device(self) -> str:
        """Return an explicit device string."""
        if self.device is not None:
            return self.device
        return "cuda" if torch.cuda.is_available() else "cpu"

    def set_seed(self) -> None:
        """Seed Python, NumPy, and Torch for reproducibility."""
        random.seed(self.seed)
        np.random.seed(self.seed % (2**32 - 1))
        torch.manual_seed(self.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.seed)