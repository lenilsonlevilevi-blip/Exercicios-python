# laço de repetição - Estrutura FOR
#Contagem de 1- até um para fogos de artifícios
from time import sleep
import winsound

print("---CONTAGEM REGRESSIVA---")
for c in range(10,0,-1):
    print(c)
    sleep(1)
print("🎆🎆🎆 BOOOOM!!! 🎆🎆🎆")

sleep(1)

# som tipo "explosão" (beep rápido)
winsound.Beep(1000, 500)  # frequência, duração
winsound.Beep(800, 300)
winsound.Beep(1200, 700)
