tabuada = int(input("Quer ver a tabuada de qual valor: "))
while True:
    if tabuada <0:
        print("Programa Finalizado!")
        break
    contador = 1
    while contador <= 10:
        print(f"{tabuada} x {contador} = {tabuada * contador}")
        contador += 1
    tabuada = int(input("Quer ver a tabuada de qual valor: "))





