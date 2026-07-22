import os
import torch
from diffusers import StableDiffusionXLPipeline

from src.persona.persona import Persona
from src.image.prompts import build_prompt, build_negative_prompt


class ImageGenerator:
    """Loads SDXL once, then generates images from personas."""

    def __init__(self):
        print("Loading SDXL (first run downloads ~7GB)...")
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        ).to("cuda")

    def generate(self, persona: Persona, seed: int = 42, steps: int = 30) -> str:
        image = self.pipe(
            prompt=build_prompt(persona),
            negative_prompt=build_negative_prompt(),
            num_inference_steps=steps,
            generator=torch.Generator(device="cuda").manual_seed(seed),
        ).images[0]

        os.makedirs("outputs", exist_ok=True)
        path = f"outputs/{persona.name.lower()}_seed{seed}.png"
        image.save(path)
        print(f"Saved: {path}")
        return path
