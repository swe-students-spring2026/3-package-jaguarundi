# Placeholder test file, change the name once functions are set
import pytest
from dogcare.dog import Dog

# Valid cases
def test_valid_dog():
    dog = Dog("Labrador", 30, "large", 3)
    assert dog.species == "Labrador"
    assert dog.weight == 30
    assert dog.size == "large"
    assert dog.age == 3

def test_size_uppercase_stripped():
    dog = Dog("Poodle", 5, " Small ", 2)
    assert dog.size == "small"

def test_species_stripped():
    dog = Dog("  Beagle  ", 10, "medium", 4)
    assert dog.species == "Beagle"

# Invalid cases 
## Species
def test_invalid_species_empty():
    with pytest.raises(ValueError):
        Dog("", 10, "medium", 3)

def test_invalid_species_not_string():
    with pytest.raises(ValueError):
        Dog(123, 10, "medium", 3)

## Weight
def test_invalid_weight_zero():
    with pytest.raises(ValueError):
        Dog("Labrador", 0, "large", 3)

def test_invalid_weight_negative():
    with pytest.raises(ValueError):
        Dog("Labrador", -5, "large", 3)

def test_invalid_weight_string():
    with pytest.raises(ValueError):
        Dog("Labrador", "heavy", "large", 3)

## Size
def test_invalid_size():
    with pytest.raises(ValueError):
        Dog("Labrador", 30, "huge", 3)

## Age
def test_age_negative():
    with pytest.raises(ValueError):
        Dog("Labrador", 30, "large", -1)

def test_invalid_age_string():
    with pytest.raises(ValueError):
        Dog("Labrador", 30, "large", "old")
    
