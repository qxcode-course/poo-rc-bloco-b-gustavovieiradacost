class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def setTamanho(self, valor):
        tamanhos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = valor

    def __str__(self):
        return f"size: ({self.__tamanho})"


roupa = Roupa()

