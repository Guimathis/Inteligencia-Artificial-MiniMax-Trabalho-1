from copy import deepcopy
import math
from jogo.regras_jogo import *


def IA(tableiro, jogador):
    return melhor_jogada(tableiro, jogador)

def heuristica(tabuleiro, jogador):
    # Estima valor do tabuleiro
    h = 0
    oponente = 'O' if jogador == 'X' else 'X'

    # Verifica as linhas
    for i in range(3):
        if oponente not in (tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2]):
            h += math.pow((tabuleiro[i][0] == jogador) + (tabuleiro[i][1] == jogador) + (tabuleiro[i][2] == jogador), 2)

    # Verifica as colunas
    for i in range(3):
        if oponente not in (tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i]):
            h += math.pow((tabuleiro[0][i] == jogador) + (tabuleiro[1][i] == jogador) + (tabuleiro[2][i] == jogador), 2)

    # Verifica a diagonal principal
    if oponente not in (tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]):
        h += math.pow((tabuleiro[0][0] == jogador) + (tabuleiro[1][1] == jogador) + (tabuleiro[2][2] == jogador), 2)

    # Verifica a diagonal secundária
    if oponente not in (tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]):
        h += math.pow((tabuleiro[0][2] == jogador) + (tabuleiro[1][1] == jogador) + (tabuleiro[2][0] == jogador), 2)

    # Subtrai os valores para o oponente
    for i in range(3):
        if jogador not in (tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2]):
            h -= math.pow((tabuleiro[i][0] == oponente) + (tabuleiro[i][1] == oponente) + (tabuleiro[i][2] == oponente), 2)

    for i in range(3):
        if jogador not in (tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i]):
            h -= math.pow((tabuleiro[0][i] == oponente) + (tabuleiro[1][i] == oponente) + (tabuleiro[2][i] == oponente), 2)

    if jogador not in (tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]):
        h -= math.pow((tabuleiro[0][0] == oponente) + (tabuleiro[1][1] == oponente) + (tabuleiro[2][2] == oponente), 2)

    if jogador not in (tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]):
        h -= math.pow((tabuleiro[0][2] == oponente) + (tabuleiro[1][1] == oponente) + (tabuleiro[2][0] == oponente), 2)

    return h
# def heuristica(tabuleiro, jogador):
#     # Verifica linhas, colunas e diagonais para vitória
#     for linha in tabuleiro:
#         if linha[0] == linha[1] == linha[2]:
#             if linha[0] == 'X':
#                 return 10
#             elif linha[0] == 'O':
#                 return -10
#
#     for col in range(3):
#         if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col]:
#             if tabuleiro[0][col] == 'X':
#                 return 10
#             elif tabuleiro[0][col] == 'O':
#                 return -10
#
#     if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
#         if tabuleiro[0][0] == 'X':
#             return 10
#         elif tabuleiro[0][0] == 'O':
#             return -10
#
#     if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
#         if tabuleiro[0][2] == 'X':
#             return 10
#         elif tabuleiro[0][2] == 'O':
#             return -10
#
#     # Verifica se há dois em linha e o terceiro espaço vazio
#     for linha in tabuleiro:
#         if linha.count('X') == 2 and linha.count(' ') == 1:
#             return 5  # Bom para X
#         elif linha.count('O') == 2 and linha.count(' ') == 1:
#             return -5  # Bom para O
#
#     for col in range(3):
#         coluna = [tabuleiro[0][col], tabuleiro[1][col], tabuleiro[2][col]]
#         if coluna.count('X') == 2 and coluna.count(' ') == 1:
#             return 5  # Bom para X
#         elif coluna.count('O') == 2 and coluna.count(' ') == 1:
#             return -5  # Bom para O
#
#     # Nenhum resultado final, jogo em andamento ou empate
#     return 0


def mini_max(tabuleiro, profundidade, alpha, beta, jogador):
    if profundidade == 0 or verificar_vitoria(tabuleiro, jogador):
        return heuristica(tabuleiro, jogador)
    if verificar_empate(tabuleiro):
        return 0

    jogadas = jogadas_possiveis(tabuleiro)
    if jogador == 'O':  # MAX
        valorMax = -999
        for jogada in jogadas:
            resultado = proxima_jogada(tabuleiro, jogada, jogador)
            valor = mini_max(resultado, profundidade-1, alpha, beta, jogador='O' if jogador == 'X' else 'X')
            valorMax = max(valorMax, valor)
            alpha = max(alpha, valor)
            if beta <= alpha:
                break
        return valorMax
    else:  # MIN
        valorMin = 999
        for jogada in jogadas:
            resultado = proxima_jogada(tabuleiro, jogada, jogador)
            valor = mini_max(resultado, profundidade-1, alpha, beta, jogador='O' if jogador == 'X' else 'X')
            valorMin = min(valorMin, valor)
            beta = min(beta, valor)
            if beta <= alpha:
                break
        return valorMin


# Retorna uma lista com os indices de todas as jogadas possiveis
def jogadas_possiveis(tabuleiro):
    jogadas = []
    for i, linha in enumerate(tabuleiro):
        for j, posicao in enumerate(linha):
            if posicao == ' ':
                jogadas.append([i, j])
    return jogadas


def melhor_jogada(tabuleiro, jogador):
    jogadas = jogadas_possiveis(tabuleiro)
    melhor = -999
    melhor_j = None
    for jogada in jogadas:
        resultado = proxima_jogada(tabuleiro, jogada, jogador)
        valor = mini_max(resultado, 1, 0, 0, jogador='O' if jogador == 'X' else 'X')
        if valor > melhor:
            melhor = valor
            melhor_j = jogada
    return melhor_j


def proxima_jogada(tabuleiro, posicao, jogador):
    tabuleiro_novo = deepcopy(tabuleiro)
    tabuleiro_novo[posicao[0]][posicao[1]] = jogador
    return tabuleiro_novo
