print('-'*30)
def ficha():
    n = str(input('Nome do jogador: '))
    if n == '':
        n = '<desconhecido>'
    g = str(input('Quantidade de gols: '))
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato')




ficha()