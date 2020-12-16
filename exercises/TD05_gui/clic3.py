import tkinter as tk


def afficheLigne(event):
    if event.x >= 0 and event.x < 250:
    

    elif event.x > 250 and event.x <= 500:
     

    #canvas.create_rectangle((event.x, event.y), (event.x, event.y),\
    #fill ="red", width=0)


racine = tk.Tk() # Création de la fenêtre racine


#Création des canvas
canvas = tk.Canvas(racine, bg="black", height=500, width=500)

#Placement des canvas
canvas.grid()

ligne = canvas.create_line((250,0), (250, 500), fill = "white")

canvas.bind("<Button-1>", afficheLigne)


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 