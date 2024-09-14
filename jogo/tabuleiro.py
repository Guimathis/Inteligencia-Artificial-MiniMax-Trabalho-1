# Lib usada para copiar o valor de uma variável
from copy import deepcopy


# Exibe o tabuleiro na saida
def imprimir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        i += 1
        if i == 1:
            print("   1    2    3 ")
        print(i.__str__() + " " + "  │  ".join(linha))
        if i < 3:
            print("  ———┼—————┼———")


# Retorna um tabuleiro vazio
def novo_tabuleiro():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


# Recebe um estado de jogo (tabuleiro)
# e retorna as possiveis jogadas a partida daquele estado
def jogadas_possiveis(tabuleiro):
    # Lista jogadas possíveis
    jogadas = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':  # Verifica se a posição está vazia
                jogadas.append((i, j))
    return jogadas


# Copia o tabulerio em outra variável
# que pode ser alterada sem afetar o tabuleiro original
# recebe uma jogada que será executada no novo tabuleiro
def simular_jogada(tabuleiro, jogada):
    new_tabuleiro = deepcopy(tabuleiro)
    new_tabuleiro[jogada[0]][jogada[1]] = 'O'
    return new_tabuleiro
