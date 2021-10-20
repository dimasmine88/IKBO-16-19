
class Chto_Bolit():
    def chto_bolit(self, a):
        if (a == 1):
            return "голова"
        elif (a == 2):
            return "грудь"
        elif (a == 3):
            return "горло"


class Golova():
    def bolit_golova(self, g1, g2, g3, g4):
        print("Температура выше 37.8?(да/нет)")
        g1 = str(input())
        if (g1 == "да"):
            return "Сходите к терапевту"
        elif (g1 == "нет"):
            print("Были ли травмы головы недавно?(да/нет)")
            g2 = str(input())
            if (g2 == "да"):
                return "Сходите в травмпункт"
            elif (g2 == "нет"):
                print("Головокружение есть?(да/нет)")
                g3 = str(input())
                if (g3 == "да"):
                    return "Сходите на МРТ"
                elif (g3 == "нет"):
                    print("Давление повышено?(да/нет)")
                    g4 = str(input())
                    if (g4 == "да"):
                        return "Выпейте коньячку"
                    elif (g4 == "нет"):
                        return "Симулянт"


class Grudi():
    def bolit_grudi(self, r1, r2, r3):
        print("Болит сердце?(да/нет)")
        r1 = str(input())
        if (r1 == "да"):
            return "Обратитесь к кардиологу"
        elif (r1 == "нет"):
            print("Болят легкие?(да/нет)")
            r2 = str(input())
            if (r2 == "да"):
                return "Обратитесь к пульмологу"
            elif (r2 == "нет"):
                print("Ударялись ли грудной клеткой?(да/нет)")
                r3 = str(input())
                if (r3 == "да"):
                    return ("Сходите в травмпункт")
                elif (r3 == "нет"):
                    return ("Симулянт")


class Gorlo():
    def bolit_gorlo(self, v1, v2, v3, v4, v5):
        print("Першит ли горло?(да/нет)")
        v1 = str(input())
        if (v1 == "да"):
            print("Кашель есть?(да/нет)")
            v2 = str(input())
            if (v2 == "нет"):
                return "Ангина"
            elif (v2 == "да"):
                print("Сухой или влажный?(сухой/влажный)")
                v3 = str(input())
                if (v3 == "сухой"):
                    return "Тонзиллит"
                elif (v3 == "влажный"):
                    return "Бронхит"
        elif (v1 == "нет"):
            print("Напрягали ли вы голосовые связки?(да/нет)")
            v4 = str(input())
            if (v4 == "да"):
                return "Не напрягайте их в ближайшее время"
            elif (v4 == "нет"):
                print("Повреждали ли горло?(да/нет)")
                v5 = str(input())
                if (v5 == "да"):
                    return "Обратись к ЛОР-врачу"
                elif (v5 == "нет"):
                    return "Симулянт"


def main():
    cht = Chto_Bolit()
    gol = Golova()
    gor = Gorlo()
    gru = Grudi()
    print("Что у вас болит(1.голова, 2.грудь или 3.горло)?")
    a = int(input())

    print(cht.chto_bolit(a))
    if cht.chto_bolit(a) == "голова":
        print(gol.bolit_golova(g1 = str(), g2 = str(), g3 = str(), g4 = str()), "\n")
    elif cht.chto_bolit(a) == "горло":
        print(gor.bolit_gorlo(v1 = str(), v2 = str(), v3=str, v4=str, v5=str), "\n")
    elif cht.chto_bolit(a) == "грудь":
        print(gru.bolit_grudi(r1=str, r2=str, r3=str), "\n")

if __name__ == '__main__':
    main()
