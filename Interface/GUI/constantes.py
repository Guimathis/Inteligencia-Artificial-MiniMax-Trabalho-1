import pygame

pygame.font.init()

# Constantes utilizadas durante o jogo.

LARGURA = 600
ALTURA = 600

LINHAS = 3
COLUNAS = 3
SQSIZE = LARGURA // COLUNAS

LARGURA_LINHA = 15
LARGURA_CIRCULO = 15
LARGURA_CRUZ = 20

RADIUS = SQSIZE // 4

OFFSET = 50

# CORES
COR_BG = (28, 170, 156)
COR_LINHA = (23, 145, 135)
COR_CIRCULO = (239, 231, 200)
COR_CRUZ = (66, 66, 66)

# Define a fonte para o texto do botão
FONTE = pygame.font.Font(None, 36)

# Define as cores dos botões
COR_BOTAO = (0, 128, 255)
COR_TEXTO = (255, 255, 255)
