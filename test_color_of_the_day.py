import unittest
from color_of_the_day import color_of_the_day


class test_color_of_the_day(unittest.TestCase):

    def test_output(self):

        self.assertEqual(
            color_of_the_day(0),
            'Red')

        self.assertEqual(
            color_of_the_day(1),
            'Orange')

        self.assertEqual(
            color_of_the_day(5),
            'No Color')

        self.assertEqual(
            color_of_the_day(15),
            'Blue')


if __name__ == '__main__':
    unittest.main()
