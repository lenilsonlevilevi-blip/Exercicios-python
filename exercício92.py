from datetime import date

cadastro = {}

cadastro ['nome']=input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year
cadastro['idade'] = ano_atual - ano_nasc
cadastro['ctps'] = int(input("Carteira de trabalho (0 não tem): "))
if cadastro['ctps'] == 0:
    for k, v in cadastro.items():
        print(f"{k} tem o valor {v}")
else:
    ano_contratacao = int(input("Ano de contratação: "))
    cadastro['ano_contratacao'] = ano_contratacao
    cadastro['salário'] = float(input("Salário: R$ "))

    r = ano_atual - ano_contratacao
    r2 = 35 - r
    aposentadoria = r2 + cadastro['idade']
    cadastro['aposentadoria'] = aposentadoria

    for k, v in cadastro.items():
        if k == 'salário':
            print(f"{k} tem o valor R$ {v:.3f}")
        else:
            print(f"{k} tem o valor {v}")
