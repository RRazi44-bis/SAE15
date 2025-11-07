# Zidane IKHLEF
import csv


def get_column(indice_x):
    column = []
    with open('experimentations_5G.csv', newline='', encoding='CP1252') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Essaie aussi ',' si nécessaire
        for line in reader:
            column.append(line[indice_x])  # Récupère la 3e colonne
    return column
    
# Affiche la colonne récupérée
print("Contenu de la colonne 3 :")
for value in get_column(2):
    print(value)
