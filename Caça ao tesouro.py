import random

tamanho = 5

mapa = [["~" for _ in range(tamanho)] for _ in range(tamanho)]

linha_tesouro = random.randint(0, tamanho - 1)
coluna_tesouro = random.randint(0, tamanho - 1)
mapa[linha_tesouro][coluna_tesouro] = "T"

def mostrar_mapa(esconder_tesouro=True):
    print("\n    " + " ".join(str(c + 1) for c in range(tamanho)))
    for i, linha in enumerate(mapa):
        celulas = ["~" if (c == "T" and esconder_tesouro) else c for c in linha]
        print(f"{i + 1} | " + " ".join(celulas))
    print()

print("JOGO DA CAÇA AO TESOURO")
print("Um tesouro está escondido em um mapa 5x5. Encontre-o!")
print("Informe linha e coluna (de 1 a 5).")

tentativas = 0
encontrou = False

while not encontrou:
    mostrar_mapa()

    try:
        linha = int(input("Linha (1-5): ")) - 1
        coluna = int(input("Coluna (1-5): ")) - 1
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue

    if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
        print("Posição fora do mapa! Use valores de 1 a 5.")
        continue

    tentativas += 1

    if linha == linha_tesouro and coluna == coluna_tesouro:
        encontrou = True
    else:
        mapa[linha][coluna] = "X"
        distancia = abs(linha - linha_tesouro) + abs(coluna - coluna_tesouro)

        if distancia == 1:
            print("Dica: Muito perto")
        elif distancia <= 3:
            print("Dica: Perto")
        else:
            print("Dica: Longe")

mostrar_mapa(esconder_tesouro=False)
print(f"Parabéns! Você encontrou o tesouro em {tentativas} tentativa(s)!")
