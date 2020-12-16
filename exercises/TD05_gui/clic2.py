import tkinter as tk


def afficheCercle(event):
    if event.x >= 0 and event.x < 250:
        cercle_bleu = canvas.create_oval((event.x - 50, event.y + 50),\
        (event.x + 50, event.y - 50), fill="blue")

    elif event.x > 250 and event.x <= 500:
        cercle_rouge = canvas.create_oval((event.x - 50, event.y + 50),\
        (event.x + 50, event.y - 50), fill="red")

    #canvas.create_rectangle((event.x, event.y), (event.x, event.y),\
    #fill ="red", width=0)


racine = tk.Tk() # Création de la fenêtre racine


#Création des canvas
canvas = tk.Canvas(racine, bg="black", height=500, width=500)

#Placement des canvas
canvas.grid()

ligne = canvas.create_line((250,0), (250, 500), fill = "white")

canvas.bind("<Button-1>", afficheCercle)


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 