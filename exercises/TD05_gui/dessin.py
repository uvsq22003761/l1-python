import tkinter as tk
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") 
label = tk.Label(racine, height=5, width=5)

label_couleur = tk.Button(racine, text="Choisir couleur", font="Times")
label_cercle = tk.Button(racine, text="Cercle", bg="red", font="Times")
label_carre = tk.Button(racine, text="Carré", bg="yellow", font="Times")
label_croix = tk.Button(racine, text="Croix", bg="pink", font="Times")


HEIGHT_CANVAS = 500
canvas = tk.Canvas(racine, bg="black", height=600, width=500, relief="raised", bd=10)


canvas.grid(column=1, row =1, rowspan=4)
label_couleur.grid(column = 1, row = 0)
label_cercle.grid(column = 0, row = 1, sticky="")
label_carre.grid(column = 0, row = 2, sticky="")
label_croix.grid(column = 0, row = 3, sticky="") 
#Voir comment placer les 3 labels de gauche à une distance homogène


centre = random.randint(0, 300)
cercle = canvas.create_oval((centre + 50 , centre - 50), (centre - 50,centre + 50), fill="blue") 
#reste à mettre la commande

racine.mainloop()# Lancement de la boucle principale