palavras = ('aprender', 'programar', 'linguagem', 'python',
            'Curso','gratis','Estudar','praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f"\nNa palavra {p} temos as vogais: ", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
