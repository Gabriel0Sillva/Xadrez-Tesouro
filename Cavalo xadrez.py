tamanho = 8

movimentos = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2),  (1, 2),
    (2, -1),  (2, 1),
]

def criar_tabuleiro():

    return [["." for _ in range(tamanho)] for _ in range(tamanho)]

def ler_posicao():

    while True:
        try:
            linha = int(input("Digite a linha inicial do cavalo (0 a 7): "))
            coluna = int(input("Digite a coluna inicial do cavalo (0 a 7): "))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.\n")
            continue

        if 0 <= linha < tamanho and 0 <= coluna < tamanho:
            return linha, coluna
        print("Posição fora do tabuleiro! Os valores devem estar entre 0 e 7.\n")

def dentro_do_tabuleiro(linha, coluna):

    return 0 <= linha < tamanho and 0 <= coluna < tamanho

def calcular_movimentos(linha, coluna):

    validos = []
    for dl, dc in movimentos:
        nova_linha = linha + dl
        nova_coluna = coluna + dc
        if dentro_do_tabuleiro(nova_linha, nova_coluna):
            validos.append((nova_linha, nova_coluna))
    return validos

def exibir_tabuleiro(tabuleiro):

    print()
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

def main():
    tabuleiro = criar_tabuleiro()

    linha, coluna = ler_posicao()

    for nl, nc in calcular_movimentos(linha, coluna):
        tabuleiro[nl][nc] = "*"

    tabuleiro[linha][coluna] = "C"

    exibir_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()
