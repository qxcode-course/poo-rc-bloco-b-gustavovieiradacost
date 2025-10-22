class Watch:
    def _init_(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        
        self.setHoras(hora)
        self.setMin(minuto)
        self.setSeg(segundo)
    
    def getHoras(self):
        return self.__hora 

    def getMinutos(self):
        return self.__minuto 

    def getSegundos(self):
        return self.__segundo
    
    def setHoras(self, h: int):
        if h >= 0 and h <= 23:
            self.__hora = h
        else:
            print("fail: hora invalida")
        
    def setMin(self, m: int):
        if m >= 0 and m <=59:
            self.__minuto = m
        else:
            print("fail: minuto invalido")

    def setSeg(self, s: int):
        if s >=0 and s<= 59 :
            self.__segundo = s
        else:
            print("fail: segundo invalido")   
        
    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0

    def _str_(self):
        return f"{self._hora:02d}:{self.minuto:02d}:{self._segundo:02d}"