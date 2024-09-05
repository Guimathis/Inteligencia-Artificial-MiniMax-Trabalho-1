from jogo.jogador import ler_entrada, ler_jogada
from jogo.tabuleiro import imprimir_tabuleiro, novo_tabuleiro
from IA.IA import *
def loop_opções_execução(tabuleiro):
    global jogador_atual
    print('Menu inicial: '
          'Jogo da velha em python com IA\nOpções: ')
    # 'Dificuldade: ' + dificuldade)
    sair_loop = False
    while not sair_loop:
        tabuleiro = novo_tabuleiro()
        operação = ler_entrada \
            ('1. Jogar PvP \n2: Jogar PvIA \n3: Alterar Dificuldade\n<ENTER>: Encerrar\nOpção:')
        if operação is None:
            print("Jogo encerrado.")
            break
        match operação:
            case '1':
                print("O jogo Começou:\n")
                jogador_atual = 'X'
                while True:
                    imprimir_tabuleiro(tabuleiro)
                    try:
                        jogada = ler_jogada(jogador_atual)
                        if jogada is None:
                            print('Partida encerrada, voltando ao menu:')
                            break
                        if tabuleiro[jogada['linha']][jogada['coluna']] != " ":
                            print("Posição já ocupada! Tente novamente.")
                            continue
                        tabuleiro[jogada['linha']][jogada['coluna']] = jogador_atual
                        if verificar_vitoria(tabuleiro, jogador_atual):
                            imprimir_tabuleiro(tabuleiro)
                            print(f"Parabéns {jogador_atual} você venceu!")
                            break
                        if verificar_empate(tabuleiro):
                            imprimir_tabuleiro(tabuleiro)
                            print("Empate!")
                            break
                        jogador_atual = "O" if jogador_atual == "X" else "X"
                    except (ValueError, IndexError):
                        print("Entrada inválida, insira uma posição valida:")

            case '2':
                print("O jogo Começou:\n")
                jogador_atual = 'X'
                while True:
                    imprimir_tabuleiro(tabuleiro)
                    try:
                        print(jogador_atual)
                        if jogador_atual == 'X':
                                print(jogadas_possiveis(tabuleiro))
                                jogada = ler_jogada(jogador_atual)
                                if tabuleiro[jogada['linha']][jogada['coluna']] != " ":
                                    print("Posição já ocupada! Tente novamente.")
                                    continue
                                tabuleiro[jogada['linha']][jogada['coluna']] = jogador_atual
                                if verificar_vitoria(tabuleiro, jogador_atual):
                                    imprimir_tabuleiro(tabuleiro)
                                    print(f"\nParabéns {jogador_atual} você venceu!\n")
                                    break
                                if verificar_empate(tabuleiro):
                                    imprimir_tabuleiro(tabuleiro)
                                    print("Empate!")
                                    break
                                jogador_atual = "O" if jogador_atual == "X" else "X"
                        else:
                            print(jogadas_possiveis(tabuleiro))
                            jogada_IA = IA(tabuleiro, jogador_atual)
                            if tabuleiro[jogada_IA[0]][jogada_IA[1]] != " ":
                                print("Posição já ocupada! Tente novamente.")
                                continue
                            tabuleiro[jogada_IA[0]][jogada_IA[1]] = jogador_atual
                            if verificar_vitoria(tabuleiro, jogador_atual):
                                imprimir_tabuleiro(tabuleiro)
                                print(f"\nParabéns {jogador_atual} você venceu!\n")
                                break
                            if verificar_empate(tabuleiro):
                                imprimir_tabuleiro(tabuleiro)
                                print("Empate!")
                                break
                            jogador_atual = "O" if jogador_atual == "X" else "X"
                    except (ValueError, IndexError):
                        print("Entrada inválida, insira uma posição valida:")
            case '3':
                pass
            case _:
                print("Opção inválida.")


if __name__ == '__main__':
    tabuleiro_vazio = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
    loop_opções_execução(tabuleiro_vazio)
    # imprimir_tabuleiro(tabuleiro)
