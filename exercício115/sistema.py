from time import sleep
from exercício115.lib.arquivo import *

arq ='CursoemVídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver Pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaint('idade: ')
        cadastrar (arq, nome, idade)
    elif resp == 3:
        print('Saindo do sistema! Até logo...')
        break
    else:
        print('\33[31mErro! Digite uma opção válida\33[m')
    sleep(2)
