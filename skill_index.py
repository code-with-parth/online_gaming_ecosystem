import numpy as np

def calculate_skill_index(player_scores):
    """Calculate Skill Index based on player scores."""
    if not player_scores:
        return 0
    return np.mean(player_scores) / np.std(player_scores)

# Example usage
if __name__ == "__main__":
    scores = [80, 85, 90, 95, 100]
    skill_index = calculate_skill_index(scores)
    print(f"Skill Index: {skill_index}")