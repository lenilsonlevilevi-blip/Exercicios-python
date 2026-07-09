cadastro = []
mulheres = []
pess_acima_da_media = []
media = 0
total_idade = 0

while True:
    pessoa = {}

    pessoa['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()[0].strip()
    while sexo not in 'MF':
        print('ERROR! Por favor digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F]: ')).upper()[0].strip()
        continue
    pessoa['Sexo'] = sexo
    if sexo == 'F':
        mulheres.append(pessoa['Nome'])


    idade = int(input('Idade: '))
    total_idade += idade  # soma das idades
    pessoa['Idade'] = idade

    cadastro.append(pessoa.copy())

    resp = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    while resp not in 'SN':
        print('ERROR! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()

    if resp == "N":
        break

media = total_idade / len(cadastro)
for p in cadastro:
    if p['Idade'] > media:
        pess_acima_da_media.append(p)

print("-=" * 30)
print(f"- O grupo tem {len(cadastro)} pessoas.")
print(f"- A média de idade é {media:.2f} anos.")

print(f"- As mulheres cadastradas foram: ", end='')
for m in mulheres:
    print(f'{m}, ',end='')

print(f"\n- Lista das pessoas que estão acima da média: ")
for p in pess_acima_da_media:
    print(f"- Nome = {p['Nome']}; Sexo = {p['Sexo']}; Idade = {p['Idade']}")

print('>>> ENCERRADO <<<')

