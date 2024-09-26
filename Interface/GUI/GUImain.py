from pygame import *

from IA.IA import *
from Interface.GUI.constantes import *
from Interface.TEXTUAL.main import jogada_IA
from jogo.jogador import trocar_jogador
from jogo.tabuleiro import novo_tabuleiro

# Inicializa o Pygame
pygame.init()
pygame.font.init()

altura_janela = 600
largura_janela = 700
janela = display.set_mode((altura_janela, largura_janela))
pygame.display.set_caption('Jogo da Velha IA')


# Desenha o tabuleiro
def desenhar_tabuleiro(tabuleiro):
    # Linhas verticais
    pygame.draw.line(janela, COR_LINHA, (200, 0), (200, 600), 10)
    pygame.draw.line(janela, COR_LINHA, (400, 0), (400, 600), 10)
    # Linhas horizontais
    pygame.draw.line(janela, COR_LINHA, (0, 200), (600, 200), 10)
    pygame.draw.line(janela, COR_LINHA, (0, 400), (600, 400), 10)

    # Desenha as figuras
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] != " ":
                x = coluna * 200 + 100
                y = linha * 200 + 100
                if tabuleiro[linha][coluna] == "X":
                    pygame.draw.line(janela, COR_CRUZ, (x - 80, y - 80), (x + 80, y + 80), 10)
                    pygame.draw.line(janela, COR_CRUZ, (x + 80, y - 80), (x - 80, y + 80), 10)
                elif tabuleiro[linha][coluna] == "O":
                    pygame.draw.circle(janela, COR_CIRCULO, (x, y), 80, 10)


# Verifica se há um vencedor.
# Se existir faz uma linha na sequencia vencedora
# se não existir retorna nulo
def verificar_vitoria_gui(tabuleiro, mostrar_gui):
    # Verifica as linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] and tabuleiro[linha][0] != ' ':
            # cria linha na tela
            if mostrar_gui:
                cor = COR_CIRCULO if tabuleiro[linha][0] == 'X' else COR_CRUZ
                iPos = (20, linha * SQSIZE + SQSIZE // 2)
                fPos = (LARGURA - 20, linha * SQSIZE + SQSIZE // 2)
                pygame.draw.line(janela, cor, iPos, fPos, LARGURA_LINHA)
            return tabuleiro[linha][0]

        # Verifica as colunas
        for coluna in range(3):
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
                if mostrar_gui:
                    cor = COR_CIRCULO if tabuleiro[0][coluna] == 'X' else COR_CRUZ
                    iPos = (coluna * SQSIZE + SQSIZE // 2, 20)
                    fPos = (coluna * SQSIZE + SQSIZE // 2, ALTURA - 20)
                    pygame.draw.line(janela, cor, iPos, fPos, LARGURA_LINHA)
                return tabuleiro[0][coluna]

        # Verifica a diagonal principal
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
            if mostrar_gui:
                cor = COR_CIRCULO if tabuleiro[1][1] == 'X' else COR_CRUZ
                iPos = (20, 20)
                fPos = (LARGURA - 20, ALTURA - 20)
                pygame.draw.line(janela, cor, iPos, fPos, LARGURA_CRUZ)
            return tabuleiro[0][0]

        # Verifica a diagonal secundária
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
            if mostrar_gui:
                cor = COR_CIRCULO if tabuleiro[1][1] == 'X' else COR_CRUZ
                iPos = (20, ALTURA - 20)
                fPos = (LARGURA - 20, 20)
                pygame.draw.line(janela, cor, iPos, fPos, LARGURA_CRUZ)
            return tabuleiro[0][2]

    # Se não houver vencedor, retorna None
    return None


# Função para desenhar um botão
def desenhar_botao(texto, cor, x, y, largura, altura):
    # Desenha o retângulo do botão
    botao_rect = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(janela, cor, botao_rect)

    # Renderiza o texto
    texto_renderizado = FONTE.render(texto, True, COR_TEXTO)

    # Centraliza o texto no botão
    texto_rect = texto_renderizado.get_rect(center=botao_rect.center)
    janela.blit(texto_renderizado, texto_rect)

    return botao_rect  # Retorna o retângulo do botão para verificar cliques


# Verifica se o jogo chegou a um estado final: vitória ou empate.
def fim_de_jogo(tabuleiro):
    return verificar_vitoria_gui(tabuleiro, True) or verificar_empate(tabuleiro)


# Verifica em qual botão foi o evento de clique.
def verificar_clique_botoes(pos, botao_reiniciar, botao_dificuldade, botao_modo):
    # Verifique se o clique foi dentro da área do botão de reiniciar
    if botao_reiniciar.collidepoint(pos):
        return 'reiniciar'
    elif botao_dificuldade.collidepoint(pos):
        return 'alterar_dificuldade'
    elif botao_modo.collidepoint(pos):
        return 'alternar_pvp'
    return None


# Recebe a nova dificuldade e altera o botão para ela.
def alterar_dificuldade(dificuldade):
    if dificuldade == 3:
        mainGUI(novo_tabuleiro(), 1, 'X')
    elif dificuldade == 1:
        mainGUI(novo_tabuleiro(), 2, 'X')
    elif dificuldade == 2:
        mainGUI(novo_tabuleiro(), 3, 'X')


# Recebe a ação solicitada e executa a opção desejada
def acao_botoes(acao, dificuldade, modo_de_jogo):
    if acao == 'alterar_dificuldade':  # Alterna entre dificuldades
        print('Dificuldade alterada.')
        alterar_dificuldade(dificuldade)

    elif acao == 'reiniciar':  # Reinicia o jogo
        print('Jogo reiniciado.')
        mainGUI(novo_tabuleiro(), dificuldade, 'X', modo_de_jogo)

    elif acao == 'alternar_pvp':  # Alterna entre modos de jogo
        print('Modo de jogo alterado.')
        if modo_de_jogo == 'P x IA':
            mainGUI(novo_tabuleiro(), dificuldade, 'X', 'P x P')
        elif modo_de_jogo == 'P x P':
            mainGUI(novo_tabuleiro(), dificuldade, 'X', 'P x IA')


# Função princípal que desenha o tabuleiro, botões, captura os eventos e executa as jogadas
def mainGUI(tabuleiro, dificuldade, jogador_atual='X', modo_de_jogo='P x IA'):
    # Preenche o fundo com azul
    janela.fill(COR_BG)

    # Desenha o tabuleiro
    desenhar_tabuleiro(tabuleiro)

    # Desenha os botões na tela
    if dificuldade == 3:
        botao_dificuldade = desenhar_botao('Dificíl', COR_LINHA, 25, 625, 150, 50)
    elif dificuldade == 2:
        botao_dificuldade = desenhar_botao('Médio', COR_LINHA, 25, 625, 150, 50)
    elif dificuldade == 1:
        botao_dificuldade = desenhar_botao('Fácil', COR_LINHA, 25, 625, 150, 50)

    botao_reiniciar = desenhar_botao('Reiniciar', COR_LINHA, 225, 625, 150, 50)

    botao_modo = desenhar_botao(modo_de_jogo, COR_LINHA, 425, 625, 150, 50)

    # Loop principal da interface gráfica
    rodando = True
    jogando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
                pygame.quit()
                return

            # Captura evento de clique do mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = evento.pos

                # Verifica se um botão foi clicado
                acao = verificar_clique_botoes(pos, botao_reiniciar, botao_dificuldade, botao_modo)
                if acao is not None:
                    acao_botoes(acao, dificuldade, modo_de_jogo)

                # Se não clicou em nenhum botão, processa a jogada
                elif jogando and pos[1] < 600:
                    linha, coluna = pos[1] // SQSIZE, pos[0] // SQSIZE

                    # Verifica se a posição está vazia
                    if tabuleiro[linha][coluna] != " ":
                        print("Posição já ocupada! Tente novamente.")
                        continue

                    # Realiza a jogada do jogador humano
                    if jogador_atual == 'X' and rodando is True or modo_de_jogo != 'P x IA':
                        tabuleiro[linha][coluna] = jogador_atual
                        desenhar_tabuleiro(tabuleiro)
                        if fim_de_jogo(tabuleiro):
                            jogando = False
                        jogador_atual = trocar_jogador(jogador_atual)

            if modo_de_jogo == 'P x IA':
                # Jogada da IA se for a vez do jogador 'O'
                if jogando and jogador_atual == 'O' and jogadas_possiveis(tabuleiro):

                    jogada_IA(tabuleiro, dificuldade, jogador_atual)  # Executa a jogada da IA com base na dificuldade
                    desenhar_tabuleiro(tabuleiro)
                    if fim_de_jogo(tabuleiro):
                        jogando = False
                    jogador_atual = trocar_jogador(jogador_atual)

        # Atualiza a tela após cada iteração
        pygame.display.update()


# Lista das dificuldades e váriavel para seleção da dificuldade
dificuldades = {1: 'Fácil', 2: 'Média', 3: 'Difícil'}
dificuldade = 3

# Inicia o jogo
mainGUI(novo_tabuleiro(), dificuldade, 'X')
