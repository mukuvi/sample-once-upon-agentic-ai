from strands import Agent
# TODO: Import 'tool' from strands to use the @tool decorator
from strands import tool

# TODO: Add the decorator to transform your function into a tool
@tool
def roll_dice(faces: int = 6) -> int:

    # TODO: Modify the docstring with the args and return informations
    """
    🎲 Roll a dice with a specified number of faces.
    Args:
        faces (int): The number of faces on the dice. Must be at least 1. Default is 6.
    Returns:
        int: The result of the dice roll, a random integer between 1 and the number of faces.
    Raises: 
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)



dice_master = Agent(
    # TODO: Add the tool to the agent
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

# Test your dice master's abilities
dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")

