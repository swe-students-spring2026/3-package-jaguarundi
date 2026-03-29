class Dog:
    VALID_SIZES = ["small", "medium", "large"]

    def __init__(self, species, weight, size, age):
        if not isinstance(species, str) or not species.strip():
            raise ValueError("Species must be a non-empty string.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number, in kilograms.")
        if size.strip().lower() not in self.VALID_SIZES:
            raise ValueError(f"Size must be one of {self.VALID_SIZES}.")
        if not isinstance(age, (int, float)) or age < 0:
            raise ValueError("Age must be a non-negative number.")
        
        self.species = species.strip()
        self.weight = weight
        self.size = size.strip().lower()
        self.age = age