class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor % 2 == 0 and 20 <= valor <= 50:
            self.__tamanho = valor
        else:
            print(" Tamanho inválido! Digite um número PAR entre 20 e 50.")

chinela = Chinela()

while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela:")
    try:
        tamanho = int(input())
        chinela.setTamanho(tamanho)
    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números inteiros.")

print(" Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())
