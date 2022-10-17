import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(particle_swarm(), '\b\w\b'+'.png')


if __name__ == '__main__':
    unittest.main()
