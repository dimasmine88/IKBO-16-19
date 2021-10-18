import unittest
import main

class Test_Chto_Bolit(unittest.TestCase):
    def test_chto_bolit1(self):
        self.assertEqual(self.chto_bolit(1), "голова")

    def test_chto_bolit2(self):
        self.assertEqual(self.chto_bolit(2), "грудь")

    def test_chto_bolit3(self):
        self.assertEqual(self.chto_bolit(3), "горло")


if __name__ == '__main__':
    unittest.main()
