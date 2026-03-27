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
