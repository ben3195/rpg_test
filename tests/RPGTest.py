import unittest

from personnage import Personnage


class MyTestCase(unittest.TestCase):

    def test_initial_hp(self):
        personnage = Personnage()
        self.assertEqual(100, personnage.health_point)  # add assertion here


if __name__ == '__main__':
    unittest.main()
