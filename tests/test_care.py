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
def oversized_adult():
    return Dog("Bulldog", 30, "medium", 5)

@pytest.fixture
def large_senior():
    return Dog("Labrador", 35, "large", 10)

# water needed
def test_water_needed(medium_adult):
    result = care.water_needed(medium_adult)
    assert "needs" in result
    assert "L of water" in result

def test_water_needed_invalid():
    with pytest.raises(TypeError):
        care.water_needed(None)

# food needed
def test_food_needed_normal(medium_adult):
    result = care.food_needed(medium_adult)
    assert "Estimated food" in result
    assert "normal" in result

def test_food_needed_high_activity(medium_adult):
    result = care.food_needed(medium_adult, activity="high")
    assert "high" in result

def test_food_needed_invalid_activity(medium_adult):
    with pytest.raises(ValueError):
        care.food_needed(medium_adult, activity="extreme")

def test_food_needed_invalid_dog():
    with pytest.raises(TypeError):
        care.food_needed(None)


# walks needed
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

# tip
def test_dog_tip_puppy(small_puppy):
    result = care.dog_tip(small_puppy)
    assert "training" in result.lower()

def test_dog_tip_senior(large_senior):
    result = care.dog_tip(large_senior)
    assert "senior care" in result.lower()

def test_dog_tip_condition_check(medium_adult):
    result = care.dog_tip(medium_adult)
    assert "condition" in result.lower()

def test_dog_tip_oversize(oversized_adult):
    result = care.dog_tip(oversized_adult)
    assert "oversize" in result.lower()

def test_dog_tip_invalid():
    with pytest.raises(TypeError):
        care.dog_tip(None)


# human years
def test_human_years_puppy(small_puppy):
    result = care.human_years(small_puppy)
    assert "human years old" in result

def test_human_years_adult(medium_adult):
    result = care.human_years(medium_adult)
    assert "human years old" in result

def test_human_years_senior(large_senior):
    result = care.human_years(large_senior)
    assert "human years old" in result

def test_human_years_invalid():
    with pytest.raises(TypeError):
        care.human_years(None)