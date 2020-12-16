import tkinter as tk


def afficheLigne(event):
    global nb_clic

    if nb_clic == 10:
        racine.destroy()
    
    elif nb_clic % 2 != 0:
        carre = canvas.create_rectangle((250 - 50, 250 + 50), (250 + 50, 250 - 50),\
        outline="pink", fill="black")

    elif nb_clic % 2 == 0:
        carre = canvas.create_rectangle((250 - 50, 250 + 50), (250 + 50, 250 - 50),\
        outline="pink", fill="pink")

    nb_clic += 1



racine = tk.Tk() # Création de la fenêtre racine


#Création des canvas
canvas = tk.Canvas(racine, bg="black", height=500, width=500)

#Placement des canvas
canvas.grid()

carre = canvas.create_rectangle((250 - 50, 250 + 50), (250 + 50, 250 - 50), outline="pink")


canvas.bind("<Button-1>", afficheLigne)

nb_clic = 0


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 