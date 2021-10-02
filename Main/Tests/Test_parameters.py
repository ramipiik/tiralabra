# Execute the test class by running the following comman from command line:
# python3 -m unittest -v Tests.Test_parameters

from parameters import how_much_to_win, recursion_depth, closeness_weight
import unittest
from unittest.mock import patch


class Test_parameters_class(unittest.TestCase):
    def test_how_much_to_win(self):
        self.assertEquals(how_much_to_win(3), 3)
        self.assertEquals(how_much_to_win(4), 4)
        self.assertEquals(how_much_to_win(5), 4)
        self.assertEquals(how_much_to_win(7), 4)
        self.assertEquals(how_much_to_win(10), 5)
        self.assertEquals(how_much_to_win(15), 5)
        self.assertEquals(how_much_to_win(20), 5)
        self.assertEquals(how_much_to_win(100), 5)
        self.assertEquals(how_much_to_win(0), 5)
        self.assertEquals(how_much_to_win(-1), 5)
        self.assertEquals(how_much_to_win("-"), 5)

        with self.assertRaises(TypeError):
            how_much_to_win()

        with self.assertRaises(TypeError):
            how_much_to_win(3, 4)

    def test_recursion_depth(self):
        self.assertEquals(recursion_depth(3), 11)
        self.assertEquals(recursion_depth(4), 3)
        self.assertEquals(recursion_depth(5), 3)
        self.assertEquals(recursion_depth(100), 3)
        self.assertEquals(recursion_depth(0), 3)
        self.assertEquals(recursion_depth(-1), 3)
        self.assertEquals(recursion_depth("-"), 3)

        with self.assertRaises(TypeError):
            recursion_depth()

        with self.assertRaises(TypeError):
            recursion_depth(3, 4)

    def test_closeness_weight(self):
        self.assertEquals(closeness_weight(2), 0.25)
        self.assertEquals(closeness_weight(1), 0)
        self.assertEquals(closeness_weight(0), 0)
        self.assertEquals(closeness_weight(-1), 0)
        self.assertEquals(closeness_weight("-"), 0)

        with self.assertRaises(TypeError):
            closeness_weight()

        with self.assertRaises(TypeError):
            closeness_weight(3, 4)


if __name__ == "__main__":
    unittest.main()
