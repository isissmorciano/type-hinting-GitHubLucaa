import random
def descrizioe_casuale():
    nomi = ["Luca", "Francesco", "Marco", "Luigi", "Pierpaolo", "Vincenzo"]
    nome = nomi[random.randint(0,(len(nomi)-1))]
    età = random.randint(1,99)
    return f"{nome} ha {età} anni"
descrizioe_casuale()
print(descrizioe_casuale())