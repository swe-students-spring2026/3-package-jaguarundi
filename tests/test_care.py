import pytest
from dogcare.dog import Dog
import dogcare.care as care

# Fixtures
@pytest.fixture
def small_puppy():
    return Dog("Chihuahua", 2, "small", 0.5)

@pytest.fixture
def medium_adult():
    return Dog("Beagle", 10, "medium", 4)

@pytest.fixture
def large_senior():
    return Dog("Labrador", 35, "large", 10)

@pytest.fixture
def large_adult():
    return Dog("Golden Retriever", 30, "large", 5)

@pytest.fixture
def oversized_medium_adult():
    return Dog("Bulldog", 30, "medium", 5)

@pytest.fixture
def underweight_small_adult():
    return Dog("Chihuahua", 3, "small", 3)

@pytest.fixture
def underweight_large_senior():
    return Dog("German Shephard", 12, "large", 20)

# test function 1
def test_water_small(small_puppy):
    assert "0.13L" in care.water_needed(small_puppy)

def test_water_medium(medium_adult):
    assert "0.65L" in care.water_needed(medium_adult)

def test_water_large_senior(large_senior):
    assert "2.27L" in care.water_needed(large_senior)

def test_water_large_adult(large_adult):
    assert "1.95" in care.water_needed(large_adult)

def test_water_oversized_medium(oversized_medium_adult):
    assert "1.95L" in care.water_needed(oversized_medium_adult)

def test_water_underweight_small(underweight_small_adult):
    assert "0.2L" in care.water_needed(underweight_small_adult)

def test_water_underweight_large(underweight_large_senior):
    assert "0.78L" in care.water_needed(underweight_large_senior)

def test_water_formatting(large_senior):
    assert "💧🐕" in care.water_needed(large_senior)

def test_water_invalid():
    with pytest.raises(TypeError):
        care.water_needed(None)

# test function 3
def test_walks_small(small_puppy):
    assert "2 walks/day" in care.walks_needed(small_puppy)
    assert "15 mins" in care.walks_needed(small_puppy)

def test_walks_medium(medium_adult):
    assert "2 walks/day" in care.walks_needed(medium_adult)
    assert "30 mins" in care.walks_needed(medium_adult)

def test_walks_large_senior(large_senior):
    # senior duration reduced by 10
    assert "3 walks/day" in care.walks_needed(large_senior)
    assert "20 mins" in care.walks_needed(large_senior)

def test_walks_has_emoji(medium_adult):
    assert "🚶" in care.walks_needed(medium_adult)

def test_walks_invalid():
    with pytest.raises(TypeError):
        care.walks_needed(None)

# test function 5
def test_dog_tip_puppy(small_puppy):
    result = care.dog_tip(small_puppy)
    assert "training" in result.lower()

def test_dog_tip_senior(large_senior):
    result = care.dog_tip(large_senior)
    assert "senior care" in result.lower()

def test_dog_tip_condition_check(medium_adult):
    result = care.dog_tip(medium_adult)
    assert "good condition" in result.lower()

def test_dog_tip_large_adult(large_adult):
    result = care.dog_tip(large_adult)
    assert "good condition" in result.lower()

def test_dog_tip_oversize(oversized_medium_adult):
    result = care.dog_tip(oversized_medium_adult)
    assert "oversize" in result.lower()

def test_dog_tip_underweight_small_adult(underweight_small_adult):
    result = care.dog_tip(underweight_small_adult)
    assert "underweight" in result.lower()

def test_dog_tip_underweight_large_senior(underweight_large_senior):
    result = care.dog_tip(underweight_large_senior)
    assert "underweight" in result.lower()
    assert "senior care" in result.lower()

def test_dog_tip_invalid():
    with pytest.raises(TypeError):
        care.dog_tip(None)

# test function 6
def test_human_years_small(small_puppy):
    assert "7.5" in care.human_years(small_puppy)

def test_human_years_medium(medium_adult):
    assert "34.0" in care.human_years(medium_adult)

def test_human_years_large_senior(large_senior):
    assert "72.0" in care.human_years(large_senior)

def test_human_years_large_senior(large_adult):
    assert "42.0" in care.human_years(large_adult)

def test_human_years_oversized(oversized_adult):
    assert "39.0" in care.human_years(oversized_adult)

def test_human_years_underweight_small(underweight_small_adult):
    assert "28.0" in care.human_years(underweight_small_adult)

def test_human_years_underweight_large(underweight_large_senior):
    assert "132.0" in care.human_years(underweight_large_senior)

def test_human_years_formatting(medium_adult):
    assert "🎂🐕" in care.human_years(medium_adult)

def test_human_years_invalid():
    with pytest.raises(TypeError):
        care.human_years(None)