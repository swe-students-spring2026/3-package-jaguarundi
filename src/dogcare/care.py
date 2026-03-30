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

    return f"💧🐕 Estimated water consumption: {water_amount}L/day"

# function 2
def food_needed(dog, activity="normal"):
    """
    Return recommended daily amount of food (rough estimate).
    activity: "low", "normal", or "high"
    """
    if not isinstance(dog, Dog):
        raise TypeError("Input must be a Dog object.")

    activity = activity.lower().strip()
    if activity not in {"low", "normal", "high"}:
        raise ValueError("activity must be 'low', 'normal', or 'high'.")

    food_kg = dog.weight * 0.02

    if activity == "low":
        food_kg *= 0.9
    elif activity == "high":
        food_kg *= 1.2

    # puppy/senior dogs
    if dog.age < 1:
        food_kg *= 1.5
    elif dog.age > 8:
        food_kg *= 0.85

    food_kg = round(food_kg, 3)
    return f"🍽️🐕 Estimated food: {food_kg} kg/day (activity: {activity})"

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

# function 5
def dog_tip(dog):
    if not isinstance(dog, Dog):
        raise TypeError("Input must be a Dog object.")

    tip = []
    
    if dog.age < 1:
        tip.append("Focus on training, socialization, and multiple small meals per day. ")
    elif dog.age > 8:
        tip.append("Senior Care: Reduce intense activity and schedule regular vet checkups.\n")
        if dog.size == "large":
            if dog.weight > 45:
                tip.append("Oversize: Watch for joint strain. ")
            elif dog.weight < 23:
                tip.append("Underweight: Watch for malnutrition. ")
        elif dog.size == 'medium':
            if dog.weight > 27:
                tip.append("Oversize: Watch for joint strain. ")
            elif dog.weight < 9:
                tip.append("Underweight: Watch for malnutrition. ")
        elif dog.size == 'small':
            if dog.weight > 11:
                tip.append("Oversize: Watch for joint strain. ")
            elif dog.weight < 4:
                tip.append("Underweight: Watch for malnutrition. ")
    else:
        if dog.size == "large":
            if dog.weight > 45:
                tip.append("Oversize: Watch for joint strain. ")
            elif dog.weight < 23:
                tip.append("Underweight: Watch for malnutrition. ")
            else:
                tip.append("Your dog is in good condition! ")
        elif dog.size == 'medium':
            if dog.weight > 27:
                tip.append("Oversize: Watch for joint strain. ")
            elif dog.weight < 9:
                tip.append("Underweight: Watch for malnutrition. ")
            else:
                tip.append("Your dog is in good condition! ")
        elif dog.size == 'small':
            if dog.weight > 11:
                tip.append("Oversize: Watch for joint strain. ")
            elif dog.weight < 4:
                tip.append("Underweight: Watch for malnutrition. ")
            else:
                tip.append("Your dog is in good condition! ")
    return "Care Tips:\n" + " ".join(tip)

# function 6
def human_years(dog):
    """
    Return dog's age to human years
    """

    if not isinstance(dog, Dog):
        raise TypeError("Input must be a Dog object.")
    
    if dog.age < 1:
        human_years = dog.age * 15
        return f"🎂🐕 {round(human_years, 1)} human years old"
    
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

    return f"🎂🐕 {round(human_age, 1)} human years old"
