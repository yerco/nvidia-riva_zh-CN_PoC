import numpy as np

# Example standard pronunciations (simplified)
# In practice, this should include tonal information and phoneme breakdown
standards = {
    "你好": "ni3 hao3",  # Standard phonetic and tonal representation
    # Add more words/phrases as needed
}

def calculate_phonetic_accuracy(user_input, standard_input):
    # Simple comparison - in practice, use phoneme comparison
    correct_phonemes = sum(1 for u, s in zip(user_input, standard_input) if u == s)
    total_phonemes = len(standard_input)
    accuracy = (correct_phonemes / total_phonemes) * 100
    return accuracy

def calculate_tonal_accuracy(user_input, standard_input):
    # Assuming user_input and standard_input include tonal information
    # This is a placeholder for a more complex tonal comparison logic
    correct_tones = sum(1 for u, s in zip(user_input, standard_input) if u == s)
    total_tones = len(standard_input)  # Simplified
    accuracy = (correct_tones / total_tones) * 100
    return accuracy

def evaluate_pronunciation(word, user_pronunciation):
    # Lookup the standard pronunciation
    standard_pronunciation = standards.get(word)

    if not standard_pronunciation:
        return "Word not in standard list"

    phonetic_accuracy = calculate_phonetic_accuracy(user_pronunciation, standard_pronunciation)
    tonal_accuracy = calculate_tonal_accuracy(user_pronunciation, standard_pronunciation)

    overall_accuracy = np.mean([phonetic_accuracy, tonal_accuracy])
    return overall_accuracy

# Example usage
user_input = "ni3 hao4"  # User's attempt
word = "你好"
score = evaluate_pronunciation(word, user_input)
print(f"Your pronunciation accuracy for '{word}' is: {score}%")
