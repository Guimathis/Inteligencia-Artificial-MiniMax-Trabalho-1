from jogo.regras_jogo import *


def IA(tableiro, jogador):
    jogada = melhor_jogada(tableiro, jogador)


def heuristica(tabuleiro, jogador):
    return None


#        jogada atual       int                        jogador atual
def mini_max(tabuleiro, profundidade, alpha, beta, jogador):
    if profundidade == 0 or verificar_vitoria(tabuleiro, jogador):
        return heuristica(tabuleiro, jogador)
    if verificar_empate(tabuleiro):
        return 0

    jogadas = jogadas_possiveis(tabuleiro)
    if jogador == 'X':  # MAX
        valorMax = -999
        for i in jogadas:
            resultado = jogada(tabuleiro, jogadas[i], jogador)
            valor = mini_max(resultado, profundidade, alpha, beta, jogador='O' if jogador == 'X' else 'X')
            valorMax = max(valorMax, valor)
            alpha = max(alpha, valor)
            if beta <= alpha:
                break
        return valorMax
    else:  # MIN
        valorMin = 999
        for i in jogadas:
            resultado = jogada(tabuleiro, jogadas[i], jogador)
            valor = mini_max(resultado, profundidade, alpha, beta, jogador='O' if jogador == 'X' else 'X')
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
    for i in jogadas:
        resultado = jogada(tabuleiro, jogadas[i], jogador)
        valor = mini_max(resultado, 1, 0,0, jogador='O' if jogador == 'X' else 'X')
        if valor > melhor:
            melhor = valor
            melhor_j = jogadas[i]
    return melhor_j


def jogada(tabuleiro, posicao, jogador):
    tabuleiro_novo = tabuleiro
    tabuleiro_novo[posicao[0], posicao[1]] = jogador
    return tabuleiro_novo
