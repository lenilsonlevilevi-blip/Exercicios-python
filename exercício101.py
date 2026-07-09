from datetime import date


def voto(ano_nasc):
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 18 and idade <=65:
        return print(f'Com {idade} anos: Voto obrigatório!')
    elif idade > 65:
        return print(f'Com {idade} anos: Voto opcional!')
    elif idade <18:
        return print(f'Com {idade} anos: Voto Negado!')


#Programa principal
print('-='*18)
ano = int(input('Em que anos você nasceu? '))
voto('ano_nasc')