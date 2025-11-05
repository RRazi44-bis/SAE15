# Module qu'on utilise pour lire les fichiers csv
import csv

# Ouverture du fichier csv avec l'encodage CP1252et on met le fichier ouvert dans une variable csvfile
with open('data.csv', newline='', encoding='CP1252') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for line in spamreader:
        # Ligne mis dans une liste (chaque élément = une colonne)
        print(line[2])
    print(spamreader)



# Permet de récupérer les données sous la forme d'une liste de [département, valeur].
# def fonction_dont_je_connais_pas_le_nom(indice_valeur):
#	|-> Code
# Renvoie donnée sous la forme ([region, valeur],[region, valeur],[region, valeur])

# Permet de faire une moyenne par région et de le renvoyer dans une liste.
# def moyenne_per_region(liste de liste ([region, valeur])):
# 	|-> Code
# Renvoie moyenne par région
                                   
