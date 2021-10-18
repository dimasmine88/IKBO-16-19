class Chto_Bolit:
    def chto_bolit(self, a):
        if (a == 1):
            return 'голова'
        elif (a == 2):
            return "грудь"
        elif (a == 3):
            return "горло"

class Golova:
    def golova(self, g1, g2, g3, g4):
        print("Температура выше 37.8?")
        if (g1 == "да"):
            return "Сходите к терапевту"
        elif (g1 == "нет"):
            print("Были ли травмы головы недавно?")
            if (g2 == "да"):
                return "Сходите в травмпункт"
            elif (g2 == "нет"):
                print("Головокружение есть?")


    chto = Chto_Bolit()