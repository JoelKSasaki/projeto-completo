import csv

with open("times.CSV", "r") as file:
    reader = csv.DictReader(file)
    for nome in reader:
        print(nome["Nome"])