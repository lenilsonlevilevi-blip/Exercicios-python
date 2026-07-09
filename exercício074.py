from random import randint
n = tuple(randint (1,10) for _ in range(5))
print("Valores sorteados",n)
print(f"maior: {max(n)}")
print(f"menor: {min(n)}")