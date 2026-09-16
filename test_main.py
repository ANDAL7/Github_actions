import unittest
from main import treasure_game


class TestTreasureGame(unittest.TestCase):

    def test_treasure_found(self):
        result = treasure_game("left", "wait", "green")
        self.assertEqual(result, "You found the TREASURE!")

    def test_red_door(self):
        result = treasure_game("left", "wait", "red")
        self.assertEqual(result, "Game Over!")

    def test_blue_door(self):
        result = treasure_game("left", "wait", "blue")
        self.assertEqual(result, "Game Over!")

    def test_swimming(self):
        result = treasure_game("left", "swim", "green")
        self.assertEqual(result, "Game Over!")

    def test_right_path(self):
        result = treasure_game("right", "wait", "green")
        self.assertEqual(result, "Game Over!")

    def test_invalid_choice(self):
        result = treasure_game("left", "wait", "yellow")
        self.assertEqual(result, "Invalid choice!")


if __name__ == "__main__":
    unittest.main()