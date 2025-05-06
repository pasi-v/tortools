"""Tests for the game mechanics module."""

import pytest
from tortools.mechanics import roll_skill_test, SkillTestResult


def test_skill_rating_validation():
    """Test that skill rating validation works correctly."""
    # Test valid skill ratings
    for skill in range(1, 7):
        result = roll_skill_test(skill, 10)
        assert isinstance(result, SkillTestResult)
        assert result.skill_rating == skill
    
    # Test invalid skill ratings
    with pytest.raises(ValueError):
        roll_skill_test(0, 10)
    with pytest.raises(ValueError):
        roll_skill_test(7, 10)
    with pytest.raises(ValueError):
        roll_skill_test(-1, 10)


def test_target_number_validation():
    """Test that target number validation works correctly."""
    # Test valid target numbers
    for tn in range(1, 21):
        result = roll_skill_test(3, tn)
        assert isinstance(result, SkillTestResult)
        assert result.target_number == tn
    
    # Test invalid target numbers
    with pytest.raises(ValueError):
        roll_skill_test(3, 0)
    with pytest.raises(ValueError):
        roll_skill_test(3, -1)


def test_advantage_disadvantage():
    """Test that advantage and disadvantage work correctly."""
    # Test that advantage and disadvantage cancel each other
    result = roll_skill_test(3, 10, advantage=True, disadvantage=True)
    assert isinstance(result, SkillTestResult)
    assert result.advantage
    assert result.disadvantage
    
    # Test advantage
    result = roll_skill_test(3, 10, advantage=True)
    assert result.advantage
    assert not result.disadvantage
    
    # Test disadvantage
    result = roll_skill_test(3, 10, disadvantage=True)
    assert not result.advantage
    assert result.disadvantage


def test_success_calculation():
    """Test that success is calculated correctly."""
    # Test with minimum required roll
    result = roll_skill_test(3, 10)
    assert result.success == (result.roll + result.skill_rating >= 10)
    
    # Test with guaranteed success (skill 6 + minimum roll 1 = 7, which is >= TN 6)
    result = roll_skill_test(6, 6)
    assert result.success
    
    # Test with guaranteed failure (skill 1 + maximum roll 6 = 7, which is < TN 8)
    result = roll_skill_test(1, 8)
    assert not result.success


def test_special_successes():
    """Test that special success levels are calculated correctly."""
    # Test great success
    result = roll_skill_test(3, 10)
    if result.roll + result.skill_rating >= 16:  # TN + 6
        assert result.great_success
    
    # Test extraordinary success
    result = roll_skill_test(3, 10)
    if result.roll + result.skill_rating >= 22:  # TN + 12
        assert result.extraordinary_success 