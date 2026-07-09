num = (int(input('Digite um numero: ')),
       int(input('Digite outro número: ')),
       int(input("Digite mais um número: ")),
       int(input('Digite o último número: ')))

print(num)

if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f"O número 3 foi digitado na posição {num.index(3)+1}")
else:
    print("O valor 3 não foi digitado")
print(f"os números pares são",end=" ")
for n in num:
    if n % 2==0:
        print(n, end=" ")
        










