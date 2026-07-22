"""Prompt-building logic for image generation.

Pure Python (no torch / diffusers) so it can be tested LOCALLY without a GPU.
"""
from src.persona.persona import Persona

QUALITY = ("photorealistic, natural skin texture, film grain, "
           "soft natural lighting, high detail, sharp focus")

NEGATIVE = ("plastic skin, airbrushed, cgi, 3d render, cartoon, illustration, "
            "deformed, extra fingers, blurry, out of focus, "
            "oversaturated, unnatural colors, watermark, text, low quality")


def build_prompt(persona: Persona) -> str:
    """Structured positive prompt: subject + appearance + quality tokens."""
    return (f"candid photo of a {persona.age}-year-old {persona.personality} person, "
            f"{persona.appearance}, {QUALITY}")


def build_negative_prompt() -> str:
    """What to steer AWAY from — fights the plastic/AI look."""
    return NEGATIVE


if __name__ == "__main__":
    aria = Persona("Aria", 24, "cheerful", "warm smile and freckles")
    print("POSITIVE:\n", build_prompt(aria))
    print("\nNEGATIVE:\n", build_negative_prompt())
