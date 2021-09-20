from typing import Type
import unittest
import number_guessing


class TestMain(unittest.TestCase):

    def test_guess(self):
        name = 345
        result = number_guessing.create_user(name)
        self.assertEqual(result, TypeError)


if __name__ == '__main__':
    unittest.main()
