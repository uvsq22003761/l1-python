import tkinter as tk
import random

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    #print("la fonction draw est activée")
    canvas.create_rectangle((i, j), (i, j), fill=color, width=0)
    


def ecran_aleatoire():
    i = 0
    j = 0

    while i != 256:

        if j != 256:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            couleur = get_color(r, g, b)
            draw_pixel(i, j, couleur)
            j += 1
           
        elif j == 256:
            j = 0
            i += 1


def degrade_gris():
    i = 0
    j = 0
    k = 0

    while i != 256:

        if j != 256:
            couleur = get_color(k, k, k)
            draw_pixel(i, j, couleur)
            j += 1
            k += 1
          
        elif j == 256:
            j = 0
            i += 1


def degrade_2D():
#Pas la bonne inclinaison

    i = 0
    j = 0
    bleu = 255
    rouge = 0

    while i != 256:

        if j != 256:
            couleur = get_color(rouge, 0, bleu)
            draw_pixel(i, j, couleur)
            j += 1
          
        elif j == 256:
            j = 0
            bleu -= 1
            rouge += 1
            i += 1


racine = tk.Tk() # Création de la fenêtre racine
label = tk.Label(racine)
label_aleatoire = tk.Button(racine, text="Aléatoire", fg="blue",\
bg="white", font="30", command=ecran_aleatoire)
label_degrade_gris = tk.Button(racine, text="Dégradé de gris", fg="blue",\
bg="white", font="30", command=degrade_gris)
label_degrade_2D = tk.Button(racine, text="Dégradé 2D", fg="blue",\
bg="white", font="30", command=degrade_2D)
canvas = tk.Canvas(racine, bg="black", height=256, width=256)

canvas.grid(column=1, row=0, rowspan=3)
label_aleatoire.grid(column=0, row=0)
label_degrade_gris.grid(column=0, row=1)
label_degrade_2D.grid(column=0, row=2)

#draw_pixel(128, 128, "red")

racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 


