"""Game mechanics for The One Ring RPG."""

from dataclasses import dataclass
from typing import Optional, Tuple
import random


@dataclass
class SkillTestResult:
    """Result of a skill test in The One Ring RPG."""
    success: bool
    roll: int
    feat_roll: int
    target_number: int
    skill_rating: int
    advantage: bool
    disadvantage: bool
    great_success: bool = False
    extraordinary_success: bool = False
    gandalf_rune: bool = False
    sauron_rune: bool = False


def roll_d6() -> int:
    """Roll a single d6."""
    return random.randint(1, 6)


def roll_d12() -> int:
    """Roll a single d12."""
    return random.randint(1, 12)


def roll_skill_test(skill_rating: int, target_number: int, 
                   advantage: bool = False, disadvantage: bool = False) -> SkillTestResult:
    """
    Resolve a skill test in The One Ring RPG.
    
    Args:
        skill_rating: The character's skill rating (1-6)
        target_number: The target number for the test
        advantage: Whether the character has advantage
        disadvantage: Whether the character has disadvantage
    
    Returns:
        SkillTestResult containing the test outcome and details
    """
    if not 1 <= skill_rating <= 6:
        raise ValueError("Skill rating must be between 1 and 6")
    
    if target_number < 1:
        raise ValueError("Target number must be positive")
    
    # Roll the skill dice (d6)
    skill_roll = roll_d6()
    
    # Roll the feat dice (d12)
    feat_roll = roll_d12()
    
    # Apply advantage/disadvantage
    if advantage and disadvantage:
        # They cancel each other out
        pass
    elif advantage:
        # Roll an additional skill die and take the best
        second_roll = roll_d6()
        skill_roll = max(skill_roll, second_roll)
    elif disadvantage:
        # Roll an additional skill die and take the worst
        second_roll = roll_d6()
        skill_roll = min(skill_roll, second_roll)
    
    # Calculate total
    total = skill_roll + skill_rating
    
    # Check for special results
    gandalf_rune = skill_roll == 6 and feat_roll == 12
    sauron_rune = skill_roll == 1 and feat_roll == 1
    
    # Determine success level
    success = total >= target_number
    great_success = success and (total >= target_number + 6)
    extraordinary_success = success and (total >= target_number + 12)
    
    return SkillTestResult(
        success=success,
        roll=skill_roll,
        feat_roll=feat_roll,
        target_number=target_number,
        skill_rating=skill_rating,
        advantage=advantage,
        disadvantage=disadvantage,
        great_success=great_success,
        extraordinary_success=extraordinary_success,
        gandalf_rune=gandalf_rune,
        sauron_rune=sauron_rune
    ) 