# método all(), retorna true apenas se
#   todas as comparações da iteração forem verdadeiras


# Verifica se há um vencedor.
# Se existir retorna a figura do vencedor
# se não existir retorna nulo
def verificar_vitoria(board):
    # Verifica as linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]

    # Verifica as colunas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Verifica a diagonal principal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    # Verifica a diagonal secundária
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

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
