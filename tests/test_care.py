import pytest
from dogcare.dog import Dog
from dogcare.care import walks_needed

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


# walks needed
def test_walks_small(small_puppy):
    assert "2 walks/day" in walks_needed(small_puppy)
    assert "15 mins" in walks_needed(small_puppy)

def test_walks_medium(medium_adult):
    assert "2 walks/day" in walks_needed(medium_adult)
    assert "30 mins" in walks_needed(medium_adult)

def test_walks_large_senior(large_senior):
    # senior duration reduced by 10
    assert "3 walks/day" in walks_needed(large_senior)
    assert "20 mins" in walks_needed(large_senior)

def test_walks_has_emoji(medium_adult):
    assert "🚶" in walks_needed(medium_adult)

def test_walks_invalid():
    with pytest.raises(TypeError):
        walks_needed(None)
