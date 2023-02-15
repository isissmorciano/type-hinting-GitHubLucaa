def descrizione(nome, età):
    return f"{nome} ha {età} anni"

nome = input("Inserisci il nome: ")
età = int(input("Inserisci età: "))
print(descrizione(nome,età))