# Thoughtworks Research Blogs / Demos

This repo accompanies Thoughtworks Research blogs and demos. It contains
runnable notebooks and lightweight utilities for **activation steering** in
large language models, with a focus on **Contrastive Activation Addition (CAA)**.

The main demo right now lives in `caa_steering/` and shows how to:

- Build contrastive steering directions from labeled text (love vs hate, tones)
- Collect residual-stream activations from Llama-3.1-8B
- Apply steering vectors during generation using `nnsight`
- Compare baseline vs steered generations

---

## Layout

- `caa_steering/`
  - `steering.ipynb` – main end-to-end demo notebook
  - `configs.py` – dataclass with model + steering hyperparameters
  - `prompts.py` – prompt templates and tone/debate-style definitions
  - `activations_collector.py` – utilities to build CAA steering vectors
  - `requirements.txt` – minimal pinned versions (`torch`, `transformers`, `nnsight`)
---

## Quickstart

```bash
git clone https://github.com/amir-abdullah-thoughtworks/demos_and_blogs.git
cd demos_and_blogs/caa_steering

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt

You’ll need a GPU and HF token with access to Llama 3.1:

`export HF_TOKEN=YOUR_HF_TOKEN`


Then open:

`jupyter lab`

and run steering.ipynb top-to-bottom.

## What the CAA demo does

At a high level, the demo:

- Loads **`meta-llama/Llama-3.1-8B-Instruct`** and a tone dataset  
  (`amirali1985/tone_agnostic_questions`).

- Uses prompt templates (`prompts.py`) to create:
  - Love vs hate sentiment prompts
  - “Neutral” vs “cautious” / “empathetic” tone prompts

- Uses `TorchActivationsCollector` (`activations_collector.py`) to:
  - Run prompts through the model
  - Collect last-token hidden states at a chosen layer
  - Compute mean activations for each class and a contrast vector  
    `delta = pos_mu - neg_mu`

- Uses **nnsight** in `steering.ipynb` to:
  - Wrap the model as a `LanguageModel`
  - Inject the steering vector `delta` into a window of layers around
    `layer_idx` during generation
  - Compare baseline vs steered generations on test prompts

- Saves the learned vector (e.g. `hate_vector_19.pt`) for reuse.

The code is intentionally minimal and hackable rather than a polished library.
