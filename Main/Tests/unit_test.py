import unittest
from unittest.mock import patch
from Start.players import get_players
from Start.start import start

def add(x,y):
   return x + y

def cuboid_volume(l):
    return (l*l*l)

class TestStart(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(4,5),9)
    
    @patch('builtins.input', side_effect=[1,2])
    def test_get_players(self, mock_input):
        result1=get_players()
        result2=get_players()
        self.assertEqual(result1,1)
        self.assertEqual(result2,2)

    @patch('builtins.input', side_effect=[1,'A', 1,1,''])
    def test_start(self, mock_input):
        result=start()
        self.assertEqual(result,(1,3,1,1))
 

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)
        self.assertAlmostEqual(cuboid_volume(5.5),166.375)

if __name__ == '__main__':
   unittest.main()