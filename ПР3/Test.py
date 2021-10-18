import unittest
import main

class Test_Chto_Bolit(unittest.TestCase):
    def test_chto_bolit1(self):
        self.assertEqual(self.chto_bolit(1), "голова")

    def test_chto_bolit2(self):
        self.assertEqual(self.chto_bolit(2), "грудь")

    def test_chto_bolit3(self):
        self.assertEqual(self.chto_bolit(3), "горло")


class Test_Grudi(unittest.TestCase):
    def test_grudi1(self):
        self.assertEqual(self.bolit_grudi("да"), "Обратись к кардиологу")
    def test_grudi2(self):
        self.assertEqual(self.bolit_grudi("нет", "да"), "Обратись к пульмологу")
    def test_grudi3(self):
        self.assertEqual(self.bolit_grudi("нет", "нет", "да"), "Сходите в травмпункт")
    def test_grudi4(self):
        self.assertEqual(self.bolit_grudi("нет", "нет", "нет"), "Симулянт")


if __name__ == '__main__':
    unittest.main()
