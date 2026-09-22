# Local Food Image Lab

Local, reproducible food-photography generation with ComfyUI and FLUX.1 [schnell].

## Runtime

- Windows + NVIDIA CUDA
- ComfyUI fork: `comfyui/`
- Model: `Comfy-Org/flux1-schnell` FP8 checkpoint
- Python environment: `.venv311`

Model weights are intentionally ignored by Git. Download them into
`comfyui/models/checkpoints/` as `flux1-schnell-fp8.safetensors`.

## Generate

Start ComfyUI from the repository root:

```powershell
.\.venv311\Scripts\python.exe comfyui\main.py --windows-standalone-build --listen 127.0.0.1
```

Then run the API generator from another terminal:

```powershell
.\.venv311\Scripts\python.exe scripts\generate_food.py
```

The default prompt and prompt-building guidance are in `prompts/food-photography.md`.

## Research basis

FLUX.1 [schnell] is a 12B rectified-flow text-to-image model released under
Apache-2.0. The FP8 Comfy-Org repackaging is selected here because it materially
reduces memory use and is practical on this machine's 12 GB RTX 3060. ComfyUI
provides the local graph/API runtime and supports FLUX workflows.
