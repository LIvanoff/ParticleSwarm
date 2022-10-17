import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_particle_swarm(self):
        self.assertEqual(particle_swarm(), '\b\w\b'+'.gif')

    def test_creat_gif(self):
        self.assertEqual(particle_swarm(), '\b\w\b'+'.gif')
    def test_print_particle(self):
        self.assertEqual(particle_swarm(), '\b\w\b'+'.gif')


if __name__ == '__main__':
    unittest.main()
