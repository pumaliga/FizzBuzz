import unittest
from main import FizzBuzzDetector


class TestFizzBuzzDetector(unittest.TestCase):
    def setUp(self):
        s = 'В своём стремлении повысить качество жизни они забывают'
        self.FizzBuzz = FizzBuzzDetector(s)

    def test_fizz(self):
        self.assertEqual(self.FizzBuzz.fizz(), 'Fizz count: 2')

    def test_buzz(self):
        self.assertEqual(self.FizzBuzz.buzz(), 'Buzz count: 4')

    def test_size_more(self):
        test_s = self.FizzBuzz.s
        self.assertTrue(len(test_s) >= 7, True)

    def test_size_small(self):
        test_s = self.FizzBuzz.s
        self.assertTrue(len(test_s) <= 100, True)

    def test_split(self):
        test_s = self.FizzBuzz.s
        s = ' '.join(test_s)
        self.assertTrue(type(s) == str, True)


if __name__ == "__main__":
    unittest.main()
