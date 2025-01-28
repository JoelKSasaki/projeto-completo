import csv

with open("times.CSV", "r") as file:
    reader = csv.DictReader(file)
    contador = {}
    for row in reader:
        favorite = row["time"]
        if favorite in contador:
            contador[favorite] += 1
        else:
            contador[favorite] = 1
        
for favorite in sorted(contador, key=contador.get, reverse=True):
    print(f'{favorite}: {contador[favorite]}')