import os
from dotenv import load_dotenv
from groq import Groq

from src.persona.persona import Persona

load_dotenv()  # load GROQ_API_KEY from .env into the environment


def build_script_prompt(persona: Persona, topic: str) -> str:
    """Build the instruction we send to the LLM (pure text — testable locally)."""
    return (
        f"Write a punchy 30-second social-media video script about: {topic}.\n"
        f"The creator is {persona.name}, a {persona.age}-year-old {persona.personality} "
        f"person with a {persona.voice_style} voice.\n"
        f"Keep it under 80 words, first-person, with a strong hook and a friendly sign-off. "
        f"Return only the spoken script — no stage directions or camera notes."
    )


def generate_script(persona: Persona, topic: str) -> str:
    """Call the Groq LLM and return the generated script text."""
    client = Groq()  # auto-reads GROQ_API_KEY from the environment
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert short-form video scriptwriter."},
            {"role": "user", "content": build_script_prompt(persona, topic)},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    aria = Persona("Aria", 24, "cheerful", "warm smile and freckles")
    script = generate_script(aria, "a 30-second travel tip about Ludhiana")
    print(script)
