import tkinter as tk


def afficheRouge(event):
    canvas.create_rectangle((event.x, event.y), (event.x, event.y),\
    fill ="red", width=0)


racine = tk.Tk() # Création de la fenêtre racine


#Création du canvas noir
canvas = tk.Canvas(racine, bg="black", height=500, width=500)

#Placement du canvas noir dans la fenetre tk
canvas.grid()
canvas.bind("<Button-1>", afficheRouge)


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 
