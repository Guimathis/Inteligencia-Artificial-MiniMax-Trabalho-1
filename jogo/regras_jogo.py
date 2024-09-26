# método all(), retorna true apenas se
#   todas as comparações da iteração forem verdadeiras
from Interface.GUI.constantes import *


# Verifica se há um vencedor.
# Se existir retorna a figura do vencedor
# se não existir retorna nulo
def verificar_vitoria(tabuleiro):
    # Verifica as linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != ' ':
            return tabuleiro[i][0]

    # Verifica as colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != ' ':
            return tabuleiro[0][i]

    # Verifica a diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]

    # Verifica a diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    # Se não houver vencedor, retorna None
    return None


# Verifica se houve empate
# Percorre todas as posições do tabuleiro e verifica se estão vazias
# Se nenhuma posição estiver vazia temos um empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for coluna in linha:
            if coluna == ' ':
                return False
    return True
