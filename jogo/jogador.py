# Lê a opção digitada e retorna-a para o loop de execuções
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
    jogada['linha'], jogada['coluna'] = int(entrada.split()[0])-1, int(entrada.split()[1])-1
    return jogada
