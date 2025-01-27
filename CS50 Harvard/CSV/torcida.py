import csv

with open("times.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["time"])