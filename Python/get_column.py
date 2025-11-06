# Zidane IKHLEF
import csv

column = []

with open('experimentations_5G.csv', newline='', encoding='CP1252') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')  # Essaie aussi ',' si nécessaire
    for line in reader:
        column.append(line[2])  # Récupère la 3e colonne

# Affiche la colonne récupérée
print("Contenu de la colonne 3 :")
for value in column:
    print(value)
