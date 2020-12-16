import tkinter as tk


def afficheLigne(event):
    global nb_clic
    global liste

    nb_clic += 1

    if nb_clic <= 8:
        cercle_rouge = canvas.create_oval((event.x - 50, event.y + 50),\
        (event.x + 50, event.y - 50), fill="red")
        liste.append(cercle_rouge)
    
    elif nb_clic == 9:
        for i in range((len(liste))):
            canvas.itemconfigure(liste[i], fill="yellow")

    elif nb_clic == 10:
        for i in range(8):
            canvas.delete(liste[i])
        nb_clic = 0
    



racine = tk.Tk() # Création de la fenêtre racine


#Création des canvas
canvas = tk.Canvas(racine, bg="black", height=500, width=500)

#Placement des canvas
canvas.grid()

#carre = canvas.create_rectangle((250 - 50, 250 + 50), (250 + 50, 250 - 50), outline="pink")


canvas.bind("<Button-1>", afficheLigne)

nb_clic = 0
liste = []


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 