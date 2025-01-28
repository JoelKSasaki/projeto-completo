import csv

with open("times.CSV", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["time"])