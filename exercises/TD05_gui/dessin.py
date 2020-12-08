import tkinter as tk
import random


def cercle():
    global color
    centre_x = random.randint(0, 500)
    centre_y = random.randint(0, 500)
    cercle = canvas.create_oval((centre_x + 50, centre_y - 50), (centre_x - 50, centre_y + 50),\
    fill=color)


def carre():
    global color
    centre_x = random.randint(0, 500)
    centre_y = random.randint(0, 500)
    carre = canvas.create_rectangle((centre_x + 50, centre_y - 50), (centre_x - 50, centre_y + 50),\
    fill=color)


def croix():
    global color
    centre_x = random.randint(0, 500)
    centre_y = random.randint(0, 500)
    trait1 = canvas.create_line((centre_x + 50, centre_y + 50), (centre_x - 50, centre_y - 50),\
    fill=color)
    trait2 = canvas.create_line((centre_x + 50, centre_y - 50), (centre_x - 50, centre_y + 50),\
    fill=color)
    #carre = canvas.create_rectangle((centre_x + 50, centre_y - 50), (centre_x - 50, centre_y + 50),\
    #outline="color")



def choixCouleur():
    global color
    color = str(input("Choisir la couleur des formes géométriques\
    entre: white, black, red, green, blue, cyan, yellow."))

    return color



color = "blue"

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") 
label = tk.Label(racine, height=5, width=5)

label_couleur = tk.Button(racine, text="Choisir couleur", font="Times",\
command=choixCouleur)
label_cercle = tk.Button(racine, text="Cercle", bg="red", font="Times", command=cercle)
label_carre = tk.Button(racine, text="Carré", bg="yellow", font="Times", command=carre)
label_croix = tk.Button(racine, text="Croix", bg="pink", font="Times", command=croix)


HEIGHT_CANVAS = 500
canvas = tk.Canvas(racine, bg="black", height=500, width=500, relief="raised", bd=10)


canvas.grid(column=1, row =1, rowspan=4)
label_couleur.grid(column = 1, row = 0)
label_cercle.grid(column = 0, row = 1, sticky="")
label_carre.grid(column = 0, row = 2, sticky="")
label_croix.grid(column = 0, row = 3, sticky="") 
#Voir comment placer les 3 labels de gauche à une distance homogène


racine.mainloop()# Lancement de la boucle principale