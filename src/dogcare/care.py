from dogcare.dog import Dog

# function 1

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