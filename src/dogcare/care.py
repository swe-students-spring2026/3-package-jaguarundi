from dogcare.dog import Dog

# function 1
def water_needed(dog):
    """
    Return recommended daily amount of water, determined by its weight
    """
    if not isinstance(dog, Dog):
        raise TypeError("Input must be a Dog object.")

    water_amount = dog.weight * 0.065
    water_amount = round(water_amount, 2)

    return f"Your 🐕 needs {water_amount}kg of water a day!"

# function 2

# function 3
def walks_needed(dog):
    """
    Return recommened daily walks
    """

    if not isinstance(dog, Dog):
        raise TypeError("Input must be a Dog object.")
    
    if dog.size == "small":
        walks, duration = 2, 15
    elif dog.size == "medium":
        walks, duration = 2, 30
    else:
        walks, duration = 3, 30
    
    # senior dogs
    if dog.age > 8:
        duration = max(10, duration - 10)
    
    return f"🚶‍♂️🐕{walks} walks/day, {duration} mins each"

# function 4
def dog_profile(dog):
    profile = f"\nDOG PROFILE\n"
    profile += f"Species: {dog.species}\n"
    profile += f"Weight: {dog.weight} kg\n"
    profile += f"Size: {dog.size}\n"
    profile += f"Age: {dog.age} years\n"

    if dog.age < 2:
        profile += "Stage: Puppy\n"
    elif dog.age < 7:
        profile += "Stage: Adult\n"
    else:
        profile += "Stage: Senior\n"

    if dog.size == "small":
        profile += "Note: Small dogs need more frequent feeding.\n"
    elif dog.size == "large":
        profile += "Note: Large dogs require more exercise.\n"

    return profile

# function 6
def human_years(dog):
    """
    Return dog's age to human years
    """

    if not isinstance(dog, Dog):
        raise TypeError("Input must be a Dog object.")
    
    if dog.age < 1:
        human_years = dog.age * 15
        return f"🎂🐕 {round(human_years)} human years old"
    
    human_age = 15
    
    if dog.age >= 2:
        human_age += 9
    
    if dog.age > 2:
        if dog.size == "small":
            human_age += (dog.age - 2) * 4
        elif dog.size == "medium":
            human_age += (dog.age - 2) * 5
        elif dog.size == "large":
            human_age += (dog.age - 2) * 6

    return f"🎂🐕 {round(human_years)} human years old"

