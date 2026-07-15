from dataclasses import dataclass


@dataclass
class Persona:
    """Represents a fictional AI creator (a digital persona)."""
    name: str
    age: int
    personality: str
    appearance: str

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, a {self.age}-year-old {self.personality} creator."


if __name__ == "__main__":
    aria = Persona("Aria", 24, "cheerful", "warm smile and freckles")
    print(aria.introduce())
    print(aria)            # ← dataclass gives us readable printing for FREE