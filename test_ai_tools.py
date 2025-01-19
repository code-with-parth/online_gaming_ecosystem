import unittest
from src.ai_tools.skill_index import calculate_skill_index

class TestSkillIndex(unittest.TestCase):
    def test_calculate_skill_index(self):
        scores = [80, 85, 90, 95, 100]
        skill_index = calculate_skill_index(scores)
        self.assertGreater(skill_index, 0)

if __name__ == "__main__":
    unittest.main()