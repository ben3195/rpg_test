import unittest

from personnage import Personnage


class MyTestCase(unittest.TestCase):

    def test_initial_hp(self):
        personnage = Personnage()
        self.assertEqual(100, personnage._points_de_vie)  # add assertion here

    def test_est_mort(self):
        personnage = Personnage()
        personnage.tuer()
        self.assertEqual(0, personnage._points_de_vie)
        self.assertTrue(True, personnage.est_mort())

    def test_initialement_vivant(self):
        personnage = Personnage()
        self.assertFalse(personnage.est_mort())


if __name__ == '__main__':
    unittest.main()
