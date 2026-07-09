print("  CONTROLE DE TERRENOS  ")
print('-'*30)

def area(larg, comp):
    a = larg * comp
    print(f'a área de um terreno {larg}x{comp} é de {a:.2f}')


larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))

area(larg, comp)

