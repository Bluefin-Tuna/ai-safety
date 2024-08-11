from enum import Enum
from textwrap import dedent

PROMPTS_PATH = "constitutional-ai/resources/prompts"

class Prompt(Enum):
    CritiqueRevisionFewShotPrompts = f"{PROMPTS_PATH}/CritiqueRevisionFewShotPrompts.json"
    CritiqueRevisionInstructions = f"{PROMPTS_PATH}/CritiqueRevisionInstructions.json"
    RLMadisonFewShotPrompts = f"{PROMPTS_PATH}/RLMadisonFewShotPrompts.json"
    RLMadisonPrecogFewShotPrompts = f"{PROMPTS_PATH}/RLMadisonPrecogFewShotPrompts.json"
    RLMadisonInstructions = f"{PROMPTS_PATH}/RLMadisonInstructions.json"

GENERAL_CRITIQUE = dedent('''\
CritiqueRequest: With respect to the following principles, p
''')