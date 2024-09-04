# Exibe o tabuleiro na saida
def imprimir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        i += 1
        if i == 1:
            print("   1    2    3 ")
        print(i.__str__() + " " + "  │  ".join(linha))
        if i < 3:
            print("  ———┼—————┼———")

