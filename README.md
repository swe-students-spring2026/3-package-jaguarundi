# DogCare
[![CI](https://github.com/swe-students-spring2026/3-package-jaguarundi/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-spring2026/3-package-jaguarundi/actions/workflows/build.yaml)

## Description
DogCare is a Python package that helps dog owners understand and manage their pet's daily needs. 

Given a dog's species, weight, size, and age, the package calculates recommended daily water intake, food intake, and walks needed. It also generates personalized care tips, displays a full dog profile, and converts your dog's age into human years.

Whether you have a tiny Chihuahua puppy or a senior Labrador, DogCare gives you practical, science-based guidance to keep your dog healthy and happy.

## About
This Python package helps dog owners to estimate the amount of walks, water, and food needed for their dogs based on inputs such as species, weight, age, and size. It also includes dog care tips and dog-to-human age conversion. 

Given `Dog(species, weight, size, age)`:
- `water_needed(dog)`
    - Returns a string estimating daily water intake (liters/day) based on weight.
- `food_needed(dog, activity="normal")`
    - Returns a string estimating daily food amount (kg/day). activity can be "low", "normal", or "high".
- `walks_needed(dog)`
    - Returns a string recommending number of walks per day and minutes per walk (adjusted for seniors).
- `dog_profile(dog)`
    - Returns a string displaying the dog's profile.
- `dog_tip(dog)`
    - Returns a care tip string (puppy training reminders, senior care notes, under/overweight warnings).
- `human_years(dog)`
    - Converts dog age to a playful “human years” estimate.

## How to use the package
### Installation
You can install this package directly from PyPI using pip:

```bash
pip install DogCare
```

## Usage Example
Here is a complete example of how to import and use all the features of the `DogCare` package:

### Import
```python
from dogcare.dog import Dog
import dogcare.care as care
```

### Create a Dog object
- Size must be "small", "medium", or "large", weight is in kg, age in years
```python
my_dog = Dog(species="Golden Retriever", weight=30.0, size="large", age=5)
```

### Calculate daily water intake
```python
print(care.water_needed(my_dog))
```
Output: 
```
💧🐕 Estimated water consumption: 1.95L/day
```

### Calculate daily food intake 
- Activity can be "low", "normal", or "high"
```python
print(care.food_needed(my_dog, activity="high"))
```
Output: 
```
🍽️ 🐕 Estimated food: 0.72 kg/day (activity: high)
```

### Get walk recommendations
```python
print(care.walks_needed(my_dog))
```
Output:
```
🚶🐕 Estimated walks: 3 walks/day, 30 mins each
```

### Get Dog's profile
```python
print(care.dog_profile(my_dog))
```
Output:
```
DOG PROFILE
Species: Golden Retriever
Weight: 30.0 kg
Size: large
Age: 5 years
Stage: Adult
Note: Large dogs require more exercise.
```

### Get personalized care tips
```python
print(care.dog_tip(my_dog))
```
Output:
```
Care Tips:
Your dog is in good condition! 
```

### Convert age to human years
```python
print(care.human_years(my_dog))
```
Output: 
```
🎂🐕 42 human years old
```

## For Developers
If you want to contribute to the project, here is how you can set up your local development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/swe-students-spring2026/3-package-jaguarundi.git
   cd 3-package-jaguarundi
   ```

2. Install pipenv and project dependencies:
   ```bash
   pip install pipenv
   pipenv install --dev
   ```

3. Run tests using pytest:
   ```bash
   pipenv run pytest
   ```

4. Build the package:
   ```bash
   python -m build
   ```

## Team
- [**Zeyue Xu**](https://github.com/zeyuexu123)
- [**Hanlin Yan**](https://github.com/hanlinyan-dev)
- [**Ed Ye**](https://github.com/EdwarddYe)
- [**Grace Yin**](https://github.com/gy28611)
- [**Steve Yoo**](https://github.com/seonghoyu11)