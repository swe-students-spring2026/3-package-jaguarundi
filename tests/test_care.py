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
