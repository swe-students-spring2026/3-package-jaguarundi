# DogCare
[![CI](https://github.com/swe-students-spring2026/3-package-jaguarundi/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-spring2026/3-package-jaguarundi/actions/workflows/build.yaml)

## Team
- [**Zeyue Xu**](https://github.com/zeyuexu123)
- [**Hanlin Yan**](https://github.com/hanlinyan-dev)
- [**Ed Ye**](https://github.com/EdwarddYe)
- [**Grace Yin**](https://github.com/gy28611)
- [**Steve Yoo**](https://github.com/seonghoyu11)

## Description
dogcare is a Python package that helps dog owners understand and manage their pet's daily needs. 

Given a dog's species, weight, size, and age, the package calculates recommended daily water intake, food intake, and walks needed. It also generates personalized care tips, displays a full dog profile, and converts your dog's age into human years.

Whether you have a tiny Chihuahua puppy or a senior Labrador, dogcare gives you practical, science-based guidance to keep your dog healthy and happy.
## About
This Python package helps dog owners to estimate the amount of walks, water, and food needed for their dogs based on inputs such as species, weight, age, and size. It also includes dog care tips and dog-to-human age conversion. 

Given Dog(species, weight, size, age):
- `water_needed(dog)`
    - Returns a string estimating daily water intake (liters/day) based on weight.
- `food_needed(dog, activity="normal")`
    - Returns a string estimating daily food amount (kg/day). activity can be "low", "normal", or "high".
- `walks_needed(dog)`
    - Returns a string recommending number of walks per day and minutes per walk (adjusted for seniors).
- `dog_tip(dog)`
    - Returns a care tip string (puppy training reminders, senior care notes, under/overweight warnings).
- `human_years(dog)`
    - Converts dog age to a playful “human years” estimate.

## How to use the package
### Download
You can install this package directly from PyPI using pip:

```Bash
pip install DogCare
```

### Importing
Import the package to your code with the following code:

```python
import DogCare
```

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.
