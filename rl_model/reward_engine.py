
# === rl_model/reward_engine.py ===

import textstat
from difflib import SequenceMatcher

def evaluate_output_quality(original, final):
    print("\n>> Evaluating final output with RL scoring...")
    readability = textstat.flesch_reading_ease(final)
    similarity = SequenceMatcher(None, original, final).ratio()
    score = (readability / 100) * (1 - similarity)
    return round(score, 4)
