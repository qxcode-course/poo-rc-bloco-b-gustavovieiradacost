class Watch:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def setHora(self, valor):
        if 0 <= valor <= 23:
            self.__hora = valor
        else:
            print("fail: hora invalida")

    def setMinuto(self, valor):
        if 0 <= valor <= 59:
            self.__minuto = valor
        else:
            print("fail: minuto invalido")

    def setSegundo(self, valor):
        if 0 <= valor <= 59:
            self.__segundo = valor
        else:
            print("fail: segundo invalido")

    def getHora(self):
        return self.__hora

    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):
        return self.__segundo

    