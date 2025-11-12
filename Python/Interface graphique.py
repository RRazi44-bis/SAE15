import tkinter as tk                    #Hugo
from tkinter import ttk
from PIL import Image, ImageTk          #importation des modules nécéssaires

fenetre=tk.Tk()
fenetre.title("Interface graphique")
fenetre.geometry("1280x720")            # création de la fenêtre 

frm=ttk.Frame(fenetre)
frm.grid()

titre=ttk.Label(frm,text="Ensemble des diagrammes")
titre.grid(column=0,row=0,pady=50)                        #titre 

frequence=ttk.Label(frm,text="Diagramme de l'utilisation des fréquences")                   #Création du texte pour les diagrammes
frequence.grid(column=0,row=1,pady=0,padx=0)

region=ttk.Label(frm,text="Diagramme des régions les plus représentés")                     #Création du texte pour les diagrammes
region.grid(column=0,row=2,pady=0,padx=0)

experimentateur=ttk.Label(frm,text="Diagramme des expérimentateurs les plus représentés")   #Création du texte pour les diagrammes
experimentateur.grid(column=0,row=3,pady=0,padx=0)

img=Image.open("chat.jpg")
img=img.resize((300,200))
photo=ImageTk.PhotoImage(img)                        #création de l'image 

def actionfrequence():
    canvas = tk.Canvas(fenetre,width=300,height=200)
    canvas.grid()
    canvas.create_image(0, 0, image=photo, anchor="nw")            #fonction qui fera apparaitre le diagramme

def actionregion():
    canvas = tk.Canvas(fenetre,width=300,height=200)
    canvas.grid()
    canvas.create_image(0, 0, image=photo, anchor="nw")             #fonction qui fera apparaitre le diagramme    

def actionexperimentateur():
    canvas = tk.Canvas(fenetre,width=300,height=200)
    canvas.grid()
    canvas.create_image(0, 0, image=photo, anchor="nw")             #fonction qui fera apparaitre le diagramme


boutonfrequence=ttk.Button(frm,text="Ouvrir",command=actionfrequence)
boutonfrequence.grid(column=1,row=1)

boutonregion=ttk.Button(frm,text="Ouvrir",command=actionregion)
boutonregion.grid(column=1,row=2)

boutonexperimentateur=ttk.Button(frm,text="Ouvrir",command=actionexperimentateur)      #Création des bouton pour afficher les diagrammes
boutonexperimentateur.grid(column=1,row=3)



fenetre.mainloop()
