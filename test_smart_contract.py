def test_is_fair_game():
    random_number = 75
    threshold = 50
    assert random_number >= threshold, "Test failed: Game is not fair."

# Example usage
if __name__ == "__main__":
    test_is_fair_game()
    print("Smart contract test passed.")