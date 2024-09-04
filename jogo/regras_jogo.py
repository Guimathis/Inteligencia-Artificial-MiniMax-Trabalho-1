# método all(), retorna true apenas se
#   todas as comparações da iteração forem verdadeiras


# Verifica se há um vencedor.
def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, se todas as posições da linha são iguais retorna true(vitória do jogador atual)
    for linha in tabuleiro:
        if all([posicao == jogador for posicao in linha]):
            return True

    # Verifica as colunas, se todas as posições da coluna são iguais retorna true(vitória do jogador atual)
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True

    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    # Não há vencedor
    return False


# Verifica se houve empate
# Percorre todas as posições do tabuleiro e verifica se estão vazias
# Se nenhuma posição estiver vazia temos um empate
def verificar_empate(tabuleiro):
    return all([posicao != " " for linha in tabuleiro for posicao in linha])
