class Persona:
    """Represents a fictional AI creator (a digital persona)."""

    def __init__(self, name, age, personality, appearance):#constructor
        self.name = name
        self.age = age
        self.personality = personality
        self.appearance = appearance

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.age} year old {self.personality} creator."


if __name__ == "__main__":
    aria = Persona("Aria", 28, "cheerful", "warm smile and freckles")
    print(aria.introduce())

    leo = Persona("LEO", 22, "smart", "athletic")
    print(leo.introduce())