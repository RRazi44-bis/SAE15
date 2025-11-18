import tkinter as tk                    #Hugo
from tkinter import ttk
from PIL import Image, ImageTk          #importation des modules nécéssaires
import os

fenetre=tk.Tk()
fenetre.title("Interface graphique")
fenetre.geometry("720x640")            # création de la fenêtre 

frm=ttk.Frame(fenetre)
frm.grid()

titre=ttk.Label(frm,text="Ensemble des diagrammes")
titre.grid(column=0,row=0,pady=20)                        #titre 

#----------------------------------------------------------------------------------------------------------------------------------------------------------

frequence=ttk.Label(frm,text="Diagramme de l'utilisation des fréquences")                   #Création du texte pour les diagrammes
frequence.grid(column=0,row=1,pady=0,padx=0)

region=ttk.Label(frm,text="Diagramme des régions les plus représentés")                     #Création du texte pour les diagrammes
region.grid(column=0,row=2,pady=0,padx=0)

experimentateur=ttk.Label(frm,text="Diagramme des expérimentateurs les plus représentés")   #Création du texte pour les diagrammes
experimentateur.grid(column=0,row=3,pady=0,padx=0)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def action_frequence():
    os.system("start Diagramme_des_fréquences.html")            #fonction qui fera apparaitre le diagramme avec du html

def action_region():
    os.system("start Diagramme_des_régions.html")             #fonction qui fera apparaitre le diagramme avec du html

def action_experimentateur():
    os.system("start Diagramme_des_expérimentateurs.html")            #fonction qui fera apparaitre le diagramme avec du html

#----------------------------------------------------------------------------------------------------------------------------------------------------------

boutonfrequence=ttk.Button(frm,text="Ouvrir",command=action_frequence)
boutonfrequence.grid(column=1,row=1)

boutonregion=ttk.Button(frm,text="Ouvrir",command=action_region)
boutonregion.grid(column=1,row=2)

boutonexperimentateur=ttk.Button(frm,text="Ouvrir",command=action_experimentateur)      #Création des bouton pour afficher les diagrammes
boutonexperimentateur.grid(column=1,row=3)

#----------------------------------------------------------------------------------------------------------------------------------------------------------


fenetre.mainloop()
