class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def setTamanho(self,valor):
        tamanhos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = valor

    def __str__(self):
        return f"size: ({self.__tamanho})"


roupa = Roupa()

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "$end":
        break
    if line == "$show":
        print(roupa)
    elif line.startswith("$size"):
        parts = line.split()
        if len(parts) > 1:
            roupa.setTamanho(parts[1])
        else:
            print("fail: informe um tamanho")

