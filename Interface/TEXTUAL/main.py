from IA.IA import *
from jogo.jogador import ler_entrada, ler_jogada, ler_dificuldade, trocar_jogador
from jogo.tabuleiro import imprimir_tabuleiro, novo_tabuleiro


# Loop de execução que utiliza funções auxiliares para controlar o jogo
def loop_opções_execução():
    # Lista das dificuldades e váriavel para seleção da dificuldade
    dificuldades = {1: 'Fácil', 2: 'Média', 3: 'Difícil'}
    dificuldade = 3

    print('\nMenu inicial: Jogo da velha em python com IA')
    fim_de_jogo = False
    while not fim_de_jogo:  # Enquanto fim do jogo for falso, continua a execução
        print('Dificuldade: ' + dificuldades[dificuldade])
        tabuleiro = novo_tabuleiro()
        operação = ler_entrada \
            ('Opções:\n1: Jogar PvP \n2: Jogar PvIA \n3: Alterar Dificuldade\n<ENTER>: Encerrar\nOpção: ')
        if operação is None:
            print("Jogo encerrado.")
            break
        jogador_atual = 'X'  # primeiro jogador é X
        match operação:
            case '1':  # Jogar jogador x jogador
                print(f"\nO jogo Começou: Pressione ENTER com o console limpo para retornar ao menu.")
                jogador_vs_jogador(tabuleiro, jogador_atual)

            case '2':  # jogar jogador x IA
                print(f"\nO jogo Começou: Pressione ENTER com o console limpo para retornar ao menu.")
                jogador_vs_IA(tabuleiro, jogador_atual, dificuldades, dificuldade)

            case '3':  # Alterar a dificuldade
                dificuldade = ler_dificuldade(dificuldade)
            case _:
                print("Opção inválida.")


# Loop que permite jogar jogador contra jogador
def jogador_vs_jogador(tabuleiro, jogador_atual):
    while True:
        imprimir_tabuleiro(tabuleiro)
        ganhador = verificar_vitoria(tabuleiro)
        if ganhador is not None:
            print(f"\nParabéns {ganhador} você venceu!\n")
            break
        elif verificar_empate(tabuleiro):
            print("Empate!")
            break
        try:
            jogada = ler_jogada(jogador_atual)
            if jogada is None:
                print('\nPartida encerrada, voltando ao menu:\n')
                break
            if tabuleiro[jogada['linha']][jogada['coluna']] != " ":
                print("Posição já ocupada! Tente novamente.")
                continue
            tabuleiro[jogada['linha']][jogada['coluna']] = jogador_atual
            jogador_atual = trocar_jogador(jogador_atual)  # Altera o jogador para a proxima iteração
        except (ValueError, IndexError, TypeError):  # Tratamento de exceções para evitar encerramentos inesperados
            print("Entrada inválida, insira uma posição valida:")
            continue


# Loop que permite jogar jogador contra IA
def jogador_vs_IA(tabuleiro, jogador_atual, dificuldades, dificuldade):
    while True:
        print('\nDificuldade: ' + dificuldades[dificuldade])
        imprimir_tabuleiro(tabuleiro)
        ganhador = verificar_vitoria(tabuleiro)
        if ganhador is not None:
            print(f"\nParabéns {ganhador} você venceu!\n")
            break
        elif verificar_empate(tabuleiro):
            print("Empate!")
            break
        try:
            if jogador_atual == 'X':
                jogada = ler_jogada(jogador_atual)
                if jogada is None:
                    print('\nPartida encerrada, voltando ao menu:\n')
                    break
                if tabuleiro[jogada['linha']][jogada['coluna']] != " ":
                    print("Posição já ocupada! Tente novamente.")
                    continue
                tabuleiro[jogada['linha']][jogada['coluna']] = jogador_atual
            else:
                jogadaIA = melhor_jogadaIA(tabuleiro, dificuldade)
                tabuleiro[jogadaIA[0]][jogadaIA[1]] = jogador_atual

        except (ValueError, IndexError, TypeError):  # Tratamento de exceções para evitar encerramentos inesperados
            print("Entrada inválida, insira uma posição valida:")
            continue
        jogador_atual = trocar_jogador(jogador_atual)  # Altera o jogador para a proxima iteração


if __name__ == '__main__':
    loop_opções_execução()  # Inicia o jogo
