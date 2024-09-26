# Jogo da Velha com Minimax e Poda Alfa-Beta

Este repositório contém uma implementação do clássico jogo da velha (tic-tac-toe), utilizando o algoritmo Minimax com otimização de poda Alfa-Beta. O projeto foi desenvolvido como parte de um trabalho acadêmico para a disciplina de **Inteligência Artificial**.

## Funcionalidades
- **Interface textual**:
  -  Menu de opções e estados de jogo feitos com interface textual, com instruções para jogar.
  

- **Interface Gráfica**:
    - Possibilidade de escolher as jogadas e controlar opções através de uma interface gráfica simples.
    - **Botões**:
      - **Dificuldade**: Alterna entre as dificuldades
      - **Reinicio**: Reinicia o jogo com um novo tabuleiro, salvando as outras opções.
      - **Modo de jogo**: Alterna entre modo de jogo PvIA e PvP.
      

- **Modos de jogo**:
  - **PvP (Player vs Player)**: Dois jogadores humanos se enfrentam.
  - **PvIA (Player vs IA)**: O jogador humano enfrenta a IA, com três níveis de dificuldade.
  

- **Níveis de dificuldade**:
  - **Fácil**: Todas as jogadas da IA são aleatórias.
  - **Médio**: 33.33% das jogadas da IA são aleatórias e 66.66% utilizam o algoritmo Minimax com poda Alfa-Beta.
  - **Difícil**: Todas as jogadas da IA utilizam o algoritmo Minimax com poda Alfa-Beta, sem aleatoriedade.


- **IA com Minimax**: A IA utiliza o algoritmo Minimax para garantir os melhores movimentos.
- **Poda Alfa-Beta**: Otimização do Minimax, reduzindo a quantidade de nós analisados para aumentar a eficiência.
- **Heurística Personalizada**: Avaliação dos estados finais do jogo com uma função heurística.

## Requisitos

- Biblioteca math, random, deepcopy e pygame

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Guimathis/Inteligencia-Artificial-MiniMax-Trabalho-1.git
   
- Execute a partir do arquivo main.py para interface textual
- Execute a partir do arquivo GUIpygame.py para interface gráfica
- Recomendado utilizar a IDE Pycharm.