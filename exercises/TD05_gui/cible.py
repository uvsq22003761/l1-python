import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine

couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]

nb_cercles = int(input("Entrez le nombre de cercles souhaité"))
taille_fenetre = int(input("Entrez la taille de fenetre dérisée"))

canvas = tk.Canvas(racine, bg="black", height=taille_fenetre, width=taille_fenetre)

centre = taille_fenetre/2

c = 0
compteur = 0
x = nb_cercles
taille_fenetre_cste = taille_fenetre
#for i in range(nb_cercles):
while nb_cercles > compteur:

    if c >= (len(couleurs)):
        c = 0

    elif c < (len(couleurs)):
        cercle = canvas.create_oval((centre - taille_fenetre/2, centre + taille_fenetre/2),\
        (centre + taille_fenetre/2, centre - taille_fenetre/2), fill=couleurs[c])
        c += 1
        compteur +=1
        taille_fenetre -= taille_fenetre_cste / nb_cercles
        # taille_fenetre = ((nb_cercles - x) * taille_fenetre) / nb_cercles 
        # x -= 1



canvas.grid()

racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 
