import unittest
from main import Chto_Bolit
from main import Golova, Grudi


class Test_Chto_Bolit(unittest.TestCase):
    def setUp(self):
        self.chto = Chto_Bolit()

    def test_chto_bolit1(self):
        self.assertEqual(self.chto.chto_bolit(1), "голова")

    def test_chto_bolit2(self):
        self.assertEqual(self.chto.chto_bolit(2), "грудь")

    def test_chto_bolit3(self):
        self.assertEqual(self.chto.chto_bolit(3), "горло")

class Test_Grudi(unittest.TestCase):
    def setUp(self):
        self.gru = Grudi()
    def test_grudi1(self):
        self.assertEqual(self.gru.bolit_grudi("да", "", ""), "Обратитесь к кардиологу")

    def test_grudi2(self):
        self.assertEqual(self.gru.bolit_grudi("нет", "да", ""), "Обратитесь к пульмологу")

    def test_grudi3(self):
        self.assertEqual(self.gru.bolit_grudi("нет", "нет", "да"), "Сходите в травмпункт")

    def test_grudi4(self):
        self.assertEqual(self.gru.bolit_grudi("нет", "нет", "нет"), "Симулянт")


class Test_Gorlo(unittest.TestCase):
    def test_gorlo1(self):
        self.assertEqual(self.bolit_gorlo("да"), "Кашель есть?")

    def test_gorlo2(self):
        self.assertEqual(self.bolit_gorlo("да", "нет"), "Ангина")

    def test_gorlo3(self):
        self.assertEqual(self.bolit_gorlo("да", "да", "влажный"), "Бронхит")

    def test_gorlo4(self):
        self.assertEqual(self.bolit_gorlo("да", "да", "сухой"), "Тонзиллит")

    def test_gorlo5(self):
        self.assertEqual(self.bolit_gorlo("нет", "да"), "Не напрягайте их в ближайшее время")

    def test_gorlo6(self):
        self.assertEqual(self.bolit_gorlo("нет", "нет", "да"), "Обратись к ЛОР-врачу")

    def test_gorlo7(self):
        self.assertEqual(self.bolit_gorlo("нет", "нет", "нет"), "Симулянт")

class Test_Golova(unittest.TestCase):
    def setUp(self):
        self.gol = Golova()
    def test_golova1(self):
        self.assertEqual(self.gol.bolit_golova("да", "", "", ""), "Сходите к терапевту")

    def test_golova2(self):
        self.assertEqual(self.gol.bolit_golova("нет", "да", "", ""), "Сходите в травмпункт")

    def test_golova3(self):
        self.assertEqual(self.gol.bolit_golova("нет", "нет", "да", ""), "Сходите на МРТ")

    def test_golova4(self):
        self.assertEqual(self.gol.bolit_golova("нет", "нет", "нет", "да"), "Выпейте коньячку")

    def test_golova5(self):
        self.assertEqual(self.gol.bolit_golova("нет", "нет", "нет", "нет"), "Симулянт")




if __name__ == '__main__':
    unittest.main()
