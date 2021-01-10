import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine

def deplacement(event):

    global compteur

    if event.x < x_ligne_gauche:
        canvas.move(ligne_gauche, -10, 0)
        if compteur % 2 == 0:
            canvas.itemconfigure(ligne_gauche, fill="blue")
        else:
            canvas.itemconfigure(ligne_gauche, fill="yellow")
    
    if event.x > x_ligne_gauche:
        canvas.move(ligne_gauche, 10, 0)
        if compteur % 2 == 0:
            canvas.itemconfigure(ligne_gauche, fill="blue")
        else:
            canvas.itemconfigure(ligne_gauche, fill="yellow")

    if event.x < x_ligne_droite:
        canvas.move(ligne_droite, -10, 0)
        if compteur % 2 == 0:
            canvas.itemconfigure(ligne_droite, fill="yellow")
        else:
            canvas.itemconfigure(ligne_droite, fill="blue")
    
    if event.x > x_ligne_droite:
        canvas.move(ligne_gauche, 10, 0)
        if compteur % 2 == 0:
            canvas.itemconfigure(ligne_droite, fill="yellow")
        else:
            canvas.itemconfigure(ligne_droite, fill="blue")
    
    compteur += 1


def bouton():

    canvas.coords(ligne_gauche, 200, 0, 200, 600)
    canvas.coords(ligne_droite, 400, 0, 400, 600)




canvas = tk.Canvas(racine, bg = "black", width = 600, height = 600)
canvas.grid(column=0, row=1)

recommencer = tk.Button(racine, text= "Recommencer", command = bouton)
recommencer.grid(column=0, row=0)

x_ligne_gauche = 200
x_ligne_droite = 400

ligne_gauche = canvas.create_line((x_ligne_gauche, 0), (x_ligne_gauche, 600), fill = "yellow")

ligne_droite = canvas.create_line((x_ligne_droite, 0), (x_ligne_droite, 600), fill = "blue")

compteur = 0

canvas.bind("<Button-1>", deplacement)


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 
