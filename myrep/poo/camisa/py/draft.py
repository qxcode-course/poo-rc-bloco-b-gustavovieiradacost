class Roupa:
    def __init__(self):
        self.__tamanho: str = ""  

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor.upper() in tamanhos_validos:
            self.__tamanho = valor.upper()
        else:
            print(" Tamanho inválido!")
            print("Tamanhos permitidos: PP, P, M, G, GG, XG")


if __name__ == "__main__":
    roupa = Roupa()

    while roupa.getTamanho() == "":
        tamanho = input("Digite seu tamanho de roupa (PP, P, M, G, GG, XG): ").strip()
        roupa.setTamanho(tamanho)

    print(f" Parabéns! Você comprou uma roupa tamanho {roupa.getTamanho()}.")
