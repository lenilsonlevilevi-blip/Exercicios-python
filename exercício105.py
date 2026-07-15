def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Recebe uma ou mais notas do aluno
    :param sit: Para ver a situação do aluno (opcional)
    :return: retorna um dicionário com as informações do aluno.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['Situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['Situacao'] = 'RAZÓAVEL'
        else:
            r['Situacao'] = 'RUIM'
    return r

#programa principal
resp = notas(6.8,4.8,3,2.5, sit=True)
print(resp)
help(notas)
