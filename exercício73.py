camp_br=("Palmeiras","Flamengo","Fluminense","São Paulo","Athletico-PR","Bahia","Bragantino",
        "Coritiba","EC Vitória","Botafogo","Atlético-MG","Internacional","Vasco","Grêmio",
        "Cruzeiro","Santos","Corinthians","Mirassol","Remo","Chapecoense")

print("-=" * 40)
print(f"Tabela do Campeonato Brasileiro: {camp_br}")
print("-=" * 40)
print(f"Os 5 primeiros são: {camp_br[0:5]}")
print("-=" * 40)
print(f"Os 4 últimos são: {camp_br[16:20]}")
print("-=" * 40)
print("Times em ordem alfabética:",(sorted(camp_br)))
print("-=" * 40)
print(f"O chapecoense está na {camp_br.index('Chapecoense')+1}ª posição.")