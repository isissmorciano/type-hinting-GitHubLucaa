import random
def descrizione_eta_casuale(nome):
    età = random.randint(1,99)
    return f"{nome} ha {età} anni"

print(descrizione_eta_casuale("Luca"))