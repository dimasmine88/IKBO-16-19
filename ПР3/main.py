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
        print("Температура выше 37.8?")
        if (g1 == "да"):
            return "Сходите к терапевту"
        elif (g1 == "нет"):
            print("Были ли травмы головы недавно?")
            if (g2 == "да"):
                return "Сходите в травмпункт"
            elif (g2 == "нет"):
                print("Головокружение есть?")
                if (g3 == "да"):
                    return "Сходите на МРТ"
                elif (g3 == "нет"):
                    print("Давление повышено?")
                    if (g4 == "да"):
                        return "Выпейте коньячку"
                    elif (g4 == "нет"):
                        return "Симулянт"


class Grudi():
    def bolit_grudi(self, r1, r2, r3):
        print("Болит сердце?")
        if (r1 == "да"):
            return "Обратитесь к кардиологу"
        elif (r1 == "нет"):
            print("Болят легкие?")
            if (r2 == "да"):
                return "Обратитесь к пульмологу"
            elif (r2 == "нет"):
                print("Ударялись ли грудной клеткой?")
                if (r3 == "да"):
                    return("Сходите в травмпункт")
                elif (r3 == "нет"):
                    return("Симулянт")

class Gorlo():
    def bolit_grudi(self, v1, v2, v3, v4, v5):
        print("Першит ли горло?")
        if (v1 == "да"):
            print("Кашель есть?")
            if (v2 == "нет"):
                return "Ангина"
            elif (v2 == "да"):
                print("Сухой или влажный?")
                if(v3 == "сухой"):
                    return "Тонзиллит"
                elif(v3 == "влажный"):
                    return "Бронхит"

        elif (v1 == "нет"):
            print("Напрягали ли вы голосовые связки?")
            if (v4 == "да"):
                return "Не напрягайте их в ближайшее время"
            elif (v4 == "нет"):
                print("Повреждали ли горло?")
                if (v5 == "да"):
                    return("Обратись к ЛОР-врачу")
                elif (v5 == "нет"):
                    return("Симулянт")