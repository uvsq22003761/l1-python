import tkinter as tk


def afficheLigne():
    
    global i

    if (liste_coordonées[0] >= 0 and liste_coordonées[0] < 250 \
    and liste_coordonées[2] >= 0 and liste_coordonées[2] < 250) or\
    (liste_coordonées[0] > 250 and liste_coordonées[0] <= 500 \
    and liste_coordonées[2] > 250 and liste_coordonées[2] <= 500) :

        ligne_bleue = canvas.create_line((liste_coordonées[0], liste_coordonées[1]),\
        liste_coordonées[2], liste_coordonées[3], fill="blue")
        i = 0

    else:
        ligne_bleue = canvas.create_line((liste_coordonées[0], liste_coordonées[1]),\
        liste_coordonées[2], liste_coordonées[3], fill="red")
        i = 0


    for j in range(4):
        del liste_coordonées[0]

    #elif event.x > 250 and event.x <= 500:
     
def coordonnées(event):
    global liste_coordonées
    global i
    i += 1
    liste_coordonées.append(event.x)
    liste_coordonées.append(event.y)

    if i == 2:
        afficheLigne()


racine = tk.Tk() # Création de la fenêtre racine


#Création des canvas
canvas = tk.Canvas(racine, bg="black", height=500, width=500)

#Placement des canvas
canvas.grid()

ligne = canvas.create_line((250,0), (250, 500), fill = "white")

canvas.bind("<Button-1>", coordonnées)
liste_coordonées = []
i = 0


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 