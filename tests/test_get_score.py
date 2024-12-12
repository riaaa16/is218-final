"""
Test cases for the Score class.

This module contains tests for valid and invalid inputs, as well as the string representation 
methods (__repr__ and __str__) of the Score class.
"""
import pytest
from app.get_score import Score, scoreMap

# Valid input test cases
valid_inputs = [
    (10, 5, 10, 2, 1.5, 3),  # All valid inputs
    (5, 0, 5, 0, 0.5, 1),    # Minimum valid inputs
    (10, 10, 10, 2, 2, 5),   # Maximum valid inputs
]

# Invalid input test cases
invalid_inputs = [
    # Invalid types
    ("10", 5, 10, 2, 1.5, 3),       # finish as string
    (10, 5, "shade", 2, 1.5, 3),    # shading as string
    # Out-of-range values
    (15, 5, 10, 2, 1.5, 3),         # finish not in scoreMap
    (10, -1, 10, 2, 1.5, 3),        # negative color
    (10, 5, 10, 2, 1.5, 0),         # num_chars is 0
    (10, 5, 10, 2, 1.5, -1),        # num_chars negative
    # Non-whole num_chars
    (10, 5, 10, 2, 1.5, 2.5),
]

# Test valid input
@pytest.mark.parametrize("finish, color, shading, bg, size, num_chars", valid_inputs)
def test_valid_inputs(finish, color, shading, bg, size, num_chars):
    """Test Score creation with valid inputs."""
    score = Score(finish, color, shading, bg, size, num_chars)
    assert score.calculate() > 0  # Ensure calculation works

# Test invalid input
@pytest.mark.parametrize("finish, color, shading, bg, size, num_chars", invalid_inputs)
def test_invalid_inputs(finish, color, shading, bg, size, num_chars):
    """Test Score creation with invalid inputs."""
    with pytest.raises((KeyError, ValueError)):
        invalid_score = Score(finish, color, shading, bg, size, num_chars)
        invalid_score.calculate()

# Test __repr__ method
@pytest.mark.parametrize("finish, color, shading, bg, size, num_chars", valid_inputs)
def test_repr(finish, color, shading, bg, size, num_chars):
    """Test __repr__ method for Score class."""
    score = Score(finish, color, shading, bg, size, num_chars)
    expected_repr = (
        f"Finish: {scoreMap['finish'][finish]} = {finish}\n"
        f"Color: {scoreMap['color'][color]} = {color}\n"
        f"Shading: {scoreMap['shading'][shading]} = {shading}\n"
        f"Background: {scoreMap['background'][bg]} = {bg}\n"
        f"Size: {scoreMap['size'][size]} = {size}\n"
        f"Characters: {num_chars}\n"
    )
    assert repr(score) == expected_repr  # Using built-in repr function

# Test __str__ method
@pytest.mark.parametrize("finish, color, shading, bg, size, num_chars", valid_inputs)
def test_str(finish, color, shading, bg, size, num_chars):
    """Test __str__ method for Score class."""
    score = Score(finish, color, shading, bg, size, num_chars)
    expected_str = (
        f"Finish: {scoreMap['finish'][finish]}\n"
        f"Color: {scoreMap['color'][color]}\n"
        f"Shading: {scoreMap['shading'][shading]}\n"
        f"Background: {scoreMap['background'][bg]}\n"
        f"Size: {scoreMap['size'][size]}\n"
        f"Characters: {num_chars}\n"
    )
    assert str(score) == expected_str  # Using built-in str function

# Test __repr__ with invalid inputs
@pytest.mark.parametrize("finish, color, shading, bg, size, num_chars", invalid_inputs)
def test_invalid_repr(finish, color, shading, bg, size, num_chars):
    """Test __repr__ method for invalid inputs."""
    with pytest.raises((KeyError, ValueError)):
        invalid_score = Score(finish, color, shading, bg, size, num_chars)
        invalid_score.calculate()
        repr(invalid_score)  # Using built-in repr function

# Test __str__ with invalid inputs
@pytest.mark.parametrize("finish, color, shading, bg, size, num_chars", invalid_inputs)
def test_invalid_str(finish, color, shading, bg, size, num_chars):
    """Test __str__ method for invalid inputs."""
    with pytest.raises((KeyError, ValueError)):
        invalid_score = Score(finish, color, shading, bg, size, num_chars)
        invalid_score.calculate()
        str(invalid_score)  # Using built-in str function
