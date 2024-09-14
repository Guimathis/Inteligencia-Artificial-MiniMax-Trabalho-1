# Lê uma entrada do teclado e faz tratamento de exceções
# Trata exceção de entrada e de interrupção do teclado
def ler_entrada(dado):
    try:
        string = input(dado)
        if len(string) == 0: return None
        if len(string) > 0: return string
    except IOError:
        print("\nErro na leitura da opção: " + dado)
    except KeyboardInterrupt:
        print("\nEntrada do usuário interrompida. O programa será encerrado.")
    return None


# Lê a posição da jogada no formato (x y),
# separa cada número para um campo do dicionário usando split()
# retorna o dicionário com as posições
def ler_jogada(jogador):
    jogada = {'linha': None, 'coluna': None}
    entrada = input(f"\nJogador {jogador}, faça sua jogada (formato: x y): ")
    if len(entrada) == 0: return None
    jogada['linha'], jogada['coluna'] = int(entrada.split()[0]) - 1, int(entrada.split()[1]) - 1
    return jogada


# Recebe a opção de dificuldade do teclado
# testa se está dentro das opções e retorn o valor
def ler_dificuldade(dificuldade_anterior):
    index_dificuldade = ler_entrada('\nSelecione a dificuldade desejada:\n1: Fácil\n2: Média\n3: Difícil\nOpção: ')
    if index_dificuldade not in ('1', '2', '3'):
        print('\nEntrada inválida, insira um número entre 1 e 3.')
        return dificuldade_anterior
    print('\n')
    return int(index_dificuldade)
