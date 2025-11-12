import tkinter as tk

from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import csv

SEPARATOR = "#######################################################"
CSV_FILE_NAME = "data.csv"

# Abdoul Hakim
def average(list_valeur):
    if list_valeur:
        return sum(list_valeur) / len(list_valeur)
    else:
        return 0

# Hugo
def action_frequence():
    canvas = tk.Canvas(fenetre, width=300, height=200)
    canvas.grid()
    canvas.create_image(0, 0, image=photo, anchor="nw")  # fonction qui fera apparaitre le diagramme

# Hugo
def action_region():
    canvas = tk.Canvas(fenetre, width=300, height=200)
    canvas.grid()
    canvas.create_image(0, 0, image=photo, anchor="nw")  # fonction qui fera apparaitre le diagramme

# Hugo
def action_experimentateur():
    canvas = tk.Canvas(fenetre, width=300, height=200)
    canvas.grid()
    canvas.create_image(0, 0, image=photo, anchor="nw")  # fonction qui fera apparaitre le diagramme

# Razi
def generate_pie_chart(data_dict, fig_name):
    list_used = []
    list_frequency = []

    for frequency, used in data_dict.items():
        assert type(used) == int, "The type of the data in the list must me int"

    for frequency, used in data_dict.items():
        list_frequency.append(frequency)
        list_used.append(used)

    plt.pie(list_used, labels=list_frequency)
    fig = plt.figure(figsize=(10, 7))
    fig.savefig(fig_name)
    plt.close(fig)
    plt.show()

def generate_bar_chart(data_dict, fig_name):
    list_key = []
    list_value = []

    for key, value in data_dict.items():
        assert type(value) == int, "The type of the data in the list must me int"

    for key, value in data_dict.items():
        list_key.append(key)
        list_value.append(value)

    plt.bar(list_key, list_value)
    fig = plt.figure(figsize=(10, 7))
    fig.savefig(fig_name)
    plt.close(fig)
    plt.show()

# Zidane
def get_column(indice_x):
    column = []
    with open(CSV_FILE_NAME, newline='', encoding='CP1252') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Essaie aussi ',' si nécessaire
        for line in reader:
            column.append(line[indice_x])  # Récupère la 3e colonne
    return column

# Malik
def get_raw(num_ligne):
    assert type(num_ligne) == int, "The type of num_ligne must be int"
    i = 0
    with open(CSV_FILE_NAME, newline='', encoding='CP1252') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Essaie ',' si nécessaire
        for line in reader:
            if i == num_ligne:
                return line
            i += 1
    return None

# Razi
def get_cell(x, y):
    row = get_raw(y)
    if row is not None and 0 <= x < len(row):
        return row[x]
    else:
        return None

# Razi
def count(column_indice):
    dict_item = {}
    list_item = get_column(column_indice)
    for i in range(len(list_item)):
        if i != 0: # Permet de ne pas récupérer le nom de la colonne
            dict_item[list_item[i]] = dict_item.get(list_item[i], 0) + 1
    return dict_item


# Razi
def count_frequency():
    """ # --> Garder pour montrer aux autres
    dict_frequency = {} # Clé : fréquence, valeur : nb_iteration
    list_region = get_column(1) # Récupérer la colonne des fréquence
    for i in range(len(list_region)):
        if i != 0:
            # Deuxième argument de .get est la valeur par défaut si l'objet n'est pas trouvé dans le dictionnaire, ici 0
            dict_frequency[list_region[i]] = dict_frequency.get(list_region[i], 0) + 1
    return dict_frequency # Return du dictionnaire"""
    return count(1)

# Razi
def count_region():
    """ # --> Garder pour montrer aux autres
    dict_region = {}
    list_region = get_column(11)
    for i in range(len(list_region)):
        if i != 0:
            dict_region[list_region[i]] = dict_region.get(list_region[i], 0) + 1
    return dict_region
    """
    return count(11)


if __name__ == "__main__":

    print(count_frequency())
    print(SEPARATOR)
    print(count_region())
    print(SEPARATOR)

    generate_pie_chart(count_frequency(), "pie_frequency.png")
    generate_bar_chart(count_region(), "bar_region.png")

    fenetre = tk.Tk()
    fenetre.title("Interface graphique")
    fenetre.geometry("1280x720")   #création de la fenêtre

    frm = ttk.Frame(fenetre)
    frm.grid()

    titre = ttk.Label(frm, text="Ensemble des diagrammes")
    titre.grid(column=0, row=0, pady=50)  # titre

    frequence = ttk.Label(frm,
                          text="Diagramme de l'utilisation des fréquences")  # Création du texte pour les diagrammes
    frequence.grid(column=0, row=1, pady=0, padx=0)

    region = ttk.Label(frm, text="Diagramme des régions les plus représentés")  # Création du texte pour les diagrammes
    region.grid(column=0, row=2, pady=0, padx=0)

    experimentateur = ttk.Label(frm,
                                text="Diagramme des expérimentateurs les plus représentés")  # Création du texte pour les diagrammes
    experimentateur.grid(column=0, row=3, pady=0, padx=0)

    img = Image.open("chat.jpg")
    img = img.resize((300, 200))
    photo = ImageTk.PhotoImage(img)  # création de l'image

    boutonfrequence = ttk.Button(frm, text="Ouvrir", command=action_frequence)
    boutonfrequence.grid(column=1, row=1)

    boutonregion = ttk.Button(frm, text="Ouvrir", command=action_region)
    boutonregion.grid(column=1, row=2)

    boutonexperimentateur = ttk.Button(frm, text="Ouvrir",
                                       command=action_experimentateur)  # Création des bouton pour afficher les diagrammes
    boutonexperimentateur.grid(column=1, row=3)

    fenetre.mainloop()

