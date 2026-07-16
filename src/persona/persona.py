import json
from dataclasses import dataclass, asdict


@dataclass
class Persona:
    """Represents a fictional AI creator (a digital persona)."""
    name: str
    age: int
    personality: str
    appearance: str
    voice_style: str = "friendly"


    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, a {self.age}-year-old {self.personality} creator."

    def save(self, filepath: str) -> None:
        """Save this persona to a JSON file on disk."""
        with open(filepath, "w") as f:
            json.dump(asdict(self), f, indent=4)
        print(f"Saved {self.name} to {filepath}")

    @classmethod
    def load(cls, filepath: str) -> "Persona":
        """Load a persona from a JSON file and return a new Persona object."""
        with open(filepath, "r") as f:
            data = json.load(f)
        return cls(**data)


if __name__ == "__main__":
    aria = Persona("Aria", 24, "cheerful", "warm smile and freckles")
    aria.save("data/personas/aria.json")

    loaded = Persona.load("data/personas/aria.json")
    print(loaded.introduce())
    print("Round-trip successful:", aria == loaded)