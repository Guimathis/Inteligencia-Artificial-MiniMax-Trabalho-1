# lib usada para calcular o valor do tabuleiro na heuristica
import math
# lib usada para gerar numeros aletórios
import random

from jogo.regras_jogo import *
from jogo.tabuleiro import jogadas_possiveis, simular_jogada


# Verifica em todas as posições, se uma jogada irá gerar um vencedor iminente
# Se sim retorna true, se não False
def verificar_vitoria_iminente(tabuleiro, jogador):
    # Compara se existem 3 posições seguidas com a figura do jogador
    def vitoria_iminente(l1, l2, l3, j):
        return (l1 == j and l2 == j and l3 == j) or \
            (l1 == j and l3 == j and l2 == j) or \
            (l2 == j and l3 == j and l1 == j)

    # Linhas/colunas
    for i in range(3):
        if vitoria_iminente(tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2], jogador):
            return True
        if vitoria_iminente(tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i], jogador):
            return True

    # Diagonais
    if vitoria_iminente(tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2], jogador):
        return True
    if vitoria_iminente(tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0], jogador):
        return True


# Função heuristica que estima o valor do tabuleiro num nó folha
# Utiliza os valores 0 ou 1 gerados pelas comparações para estimar um valor para a linha/coluna/diagonal
# incrementa h para dar mais valor e decrementa para diminuir o valor do tabuleiro
# quanto mais figuras iguais na mesma linha maior é o valor incrementado ou decrementado
def heuristica(tabuleiro, jogador):
    h = 0
    oponente = 'O' if jogador == 'X' else 'X'

    # Verifica as linhas
    for i in range(3):
        if oponente not in (tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2]):
            #  Soma a quantidade de figuras iguais na mesma linha e eleva ao quadrado
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
            h -= math.pow((tabuleiro[i][0] == oponente) + (tabuleiro[i][1] == oponente) + (tabuleiro[i][2] == oponente),
                          2)

    for i in range(3):
        if jogador not in (tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i]):
            h -= math.pow((tabuleiro[0][i] == oponente) + (tabuleiro[1][i] == oponente) + (tabuleiro[2][i] == oponente),
                          2)

    if jogador not in (tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]):
        h -= math.pow((tabuleiro[0][0] == oponente) + (tabuleiro[1][1] == oponente) + (tabuleiro[2][2] == oponente), 2)

    if jogador not in (tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]):
        h -= math.pow((tabuleiro[0][2] == oponente) + (tabuleiro[1][1] == oponente) + (tabuleiro[2][0] == oponente), 2)
    return h


# Algoritmo Minimax, que escolhe recursivamente qual jogada será executada
def minimax(tabuleiro, eh_max, alfa, beta):
    vencedor = verificar_vitoria(tabuleiro)

    # Condições de parada da recursão, retornam o valor do tabuleiro
    if vencedor == 'O': return heuristica(tabuleiro, 'O')
    if vencedor == 'X': return heuristica(tabuleiro, 'x')
    if verificar_empate(tabuleiro): return 0

    jogadas = jogadas_possiveis(tabuleiro)

    if eh_max:  # MAX, busca o valor máximo
        maior_valor = float('-inf')
        for jogada in jogadas:
            tabuleiro[jogada[0]][jogada[1]] = 'O'
            valor = minimax(tabuleiro, False, alfa, beta)
            tabuleiro[jogada[0]][jogada[1]] = ' '
            if valor > maior_valor:
                maior_valor = valor

            # Realiza a poda alfabeta
            alfa = max(alfa, valor)
            if beta <= alfa:
                break
        return maior_valor

    else:  # MIN, busca o valor mínimo
        menor_valor = float('inf')
        for jogada in jogadas:
            tabuleiro[jogada[0]][jogada[1]] = 'X'
            valor = minimax(tabuleiro, True, alfa, beta)
            tabuleiro[jogada[0]][jogada[1]] = ' '
            if valor < menor_valor:  # Mantém o menor valor
                menor_valor = valor

            # Realiza a poda alfabeta
            beta = min(beta, valor)
            if beta <= alfa:
                break
        return menor_valor


# Função que processa as possibilidades de jogadas e escolhe a de maior valor para a IA(MAX)
# Executa abordagens diferentes dependendo da dificuldade selecionada
def melhor_jogadaIA(tabuleiro, dificuldade):
    melhor_jogada = None
    valor = 0
    maior_valor = -999
    jogadas = jogadas_possiveis(tabuleiro)
    print('\nJogadas possiveis para IA: \n', jogadas)
    for jogada in jogadas:
        tabuleiro[jogada[0]][jogada[1]] = 'O'  # simula a jogada

        # Jogada aleatória
        if dificuldade == 1:
            melhor_jogada = jogada_aleatória(tabuleiro)

        # Se estiver no médio, chance de 66.66% para chamar o Minimax
        rng = random.randrange(0, 3)
        if dificuldade == 2 and rng in (0, 1):
            valor = minimax(tabuleiro, False, float('-inf'), float('inf'))
        elif dificuldade == 2:  # 33.33% de chance de jogar aleatóriamente
            melhor_jogada = jogada_aleatória(tabuleiro)

        # Se estiver no difícil usa sempre o minimax para escolher a jogada
        if dificuldade == 3:
            valor = minimax(tabuleiro, False, float('-inf'), float('inf'))

        tabuleiro[jogada[0]][jogada[1]] = ' '  # Desfaz a jogada simulada

        # Se o valor da última jogada for o maior, escolhe-a como melhor jogada
        if valor > maior_valor:
            maior_valor = valor
            melhor_jogada = jogada

        # Se duas jogadas tiverem o mesmo valor, verifica e escolhe a que gera uma vitória para a IA
        elif valor == maior_valor:
            copia_tabuleiro = simular_jogada(tabuleiro, jogada)
            if verificar_vitoria_iminente(copia_tabuleiro, 'O'):
                melhor_jogada = jogada

        print('Valor da jogada ' + jogada.__str__() + ': ' + valor.__str__())

    print(f'IA escolheu marcar O na posição {melhor_jogada} com um valor de: {maior_valor}\n')
    return melhor_jogada  # (i, j)


# Retorna uma jogada aleaória dentre as possiveis
def jogada_aleatória(tabuleiro):
    jogadas = jogadas_possiveis(tabuleiro)
    return jogadas[random.randrange(0, len(jogadas))]
