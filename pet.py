class Pet:
    """
    A class to represent a virtual pet using OOP concepts.
    """

    def __init__(self, name):
        """
        Initialize the Pet class with attributes for:
        - name: The name of the pet
        - hunger: Hunger level (0 = full, 10 = very hungry)
        - energy: Energy level (0 = tired, 10 = fully rested)
        - happiness: Happiness level (0–10)
        - tricks: A list to store tricks learned by the pet
        """
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # Empty list to store learned tricks

    def eat(self):
        """
        Simulate the pet eating.
        - Reduces hunger by 3 points (not below 0).
        - Increases happiness by 1 (not above 10).
        """
        self.hunger = max(0, self.hunger - 3)  # Ensure hunger doesn't go below 0
        self.happiness = min(10, self.happiness + 1)  # Ensure happiness doesn't exceed 10
        print(f"{self.name} ate some food. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        """
        Simulate the pet sleeping.
        - Increases energy by 5 points (not above 10).
        """
        self.energy = min(10, self.energy + 5)  # Ensure energy doesn't exceed 10
        print(f"{self.name} took a nap. Energy: {self.energy}")

    def play(self):
        """
        Simulate the pet playing.
        - Decreases energy by 2 (not below 0).
        - Increases happiness by 2 (not above 10).
        - Increases hunger by 1 (not above 10).
        """
        if self.energy >= 2:  # Check if there is enough energy to play
            self.energy -= 2  # Playing decreases energy by 2
            self.happiness = min(10, self.happiness + 2)  # Ensure happiness doesn't exceed 10
            self.hunger = min(10, self.hunger + 1)  # Ensure hunger doesn't exceed 10
            print(f"{self.name} played and had fun! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Energy: {self.energy}")

    def get_status(self):
        """
        Print the current state of the pet, including:
        - Hunger level
        - Energy level
        - Happiness level
        """
        print(f"Pet Status - Name: {self.name}, Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

    def train(self, trick):
        """
        Teach the pet a new trick.
        - Adds the trick to the tricks list.
        - Increases happiness by 1 (not above 10).
        """
        self.tricks.append(trick)  # Add the trick to the list
        self.happiness = min(10, self.happiness + 1)  # Ensure happiness doesn't exceed 10
        print(f"{self.name} learned a new trick: {trick}. Happiness: {self.happiness}")

    def show_tricks(self):
        """
        Display all the tricks learned by the pet.
        """
        if self.tricks:  # Check if the pet knows any tricks
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
