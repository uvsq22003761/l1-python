import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine

racine.title("Calculatrice") 

#Variables
type_de_calcul = ""
nb1 = ""
nb2 = ""
nb = ""
resultat = ""


#Fonctions


def ajoutCaractere(nb):
    global nb1
    nb1 += nb
    zone_affichage["text"] = nb1

    if nb2 != "" and type_de_calcul == 1:
        zone_affichage["text"] = nb2, "+", nb1

    elif nb2 != "" and type_de_calcul == 2:
        zone_affichage["text"] = nb2, "-", nb1
    
    elif nb2 != "" and type_de_calcul == 3:
        zone_affichage["text"] = nb2, "x", nb1
    
    elif nb2 != "" and type_de_calcul == 4:
        zone_affichage["text"] = nb2, "/", nb1



def un():
    ajoutCaractere("1")


def deux():
    ajoutCaractere("2")


def trois():
    ajoutCaractere("3")


def virgule():
    ajoutCaractere(".")


def plus():
    global type_de_calcul, nb1, nb2
    zone_affichage["text"] = nb1, "+"
    nb2 = nb1
    nb1 = ""
    type_de_calcul = 1


def moins():
    global type_de_calcul, nb1, nb2
    zone_affichage["text"] = nb1, "-"
    nb2 = nb1
    nb1 = ""
    type_de_calcul = 2


def multiplication():
    global type_de_calcul, nb1, nb2
    zone_affichage["text"] = nb1, "x"
    nb2 = nb1
    nb1 = ""
    type_de_calcul = 3


def division():
    global type_de_calcul, nb1, nb2
    zone_affichage["text"] = nb1, "/"
    nb2 = nb1
    nb1 = ""
    type_de_calcul = 4


def egal():
    global type_de_calcul, nb1, nb2, resultat

    nb1 = float(nb1)
    nb2 = float(nb2)
    
    if type_de_calcul == 1:
        resultat = nb2 + nb1
    elif type_de_calcul == 2:
        resultat = nb2 - nb1
    elif type_de_calcul == 3:
        resultat = nb2 * nb1
    elif type_de_calcul == 4:
        if nb1 == 0:
            resultat = "Erreur"
        else:
            resultat = nb2 / nb1

    zone_affichage["text"] = "=", resultat


def effacer():
    global nb1, nb2, type_de_calcul, nb, resultat
    type_de_calcul = ""
    nb1 = ""
    nb2 = ""
    nb = ""
    resultat = ""

    zone_affichage["text"] = "Tapper votre calcul"


#Interface graphique


zone_affichage = tk.Label(racine,text = "Tapper votre calcul", width = 44, height = 5)
zone_affichage.grid(column=0, row=0, columnspan = 4)


un = tk.Button(racine, text="1", width=10, height=5, command=un)
un.grid(column=0, row=1)


deux = tk.Button(racine,text = "2", width = 10, height = 5, command=deux)
deux.grid(column=1, row=1)

trois = tk.Button(racine,text = "3", width = 10, height = 5, command=trois)
trois.grid(column=2, row=1)

quatre = tk.Button(racine,text = "4", width = 10, height = 5)
quatre.grid(column=0, row=2)

cinq = tk.Button(racine,text = "5", width = 10, height = 5)
cinq.grid(column=1, row=2)

six = tk.Button(racine,text = "6", width = 10, height = 5)
six.grid(column=2, row=2)

sept = tk.Button(racine,text = "7", width = 10, height = 5)
sept.grid(column=0, row=3)

huit = tk.Button(racine, text = "8", width = 10, height = 5)
huit.grid(column=1, row=3)

neuf = tk.Button(racine, text = "9", width = 10, height = 5)
neuf.grid(column=2, row=3)

zero = tk.Button(racine, text = "0", width = 10, height = 5)
zero.grid(column=1, row=4)

virgule = tk.Button(racine,text =".", width=10, height=5, command=virgule)
virgule.grid(column=2, row=4)

plus = tk.Button(racine, text = "+", width =10, height = 5, command=plus)
plus.grid(column=3, row=1)

fois = tk.Button(racine, text="x", width =10, height = 5, command=multiplication)
fois.grid(column=3, row=3)

diviser = tk.Button(racine,text ="/", width = 10, height = 5, command=division)
diviser.grid(column=3, row=4)

moins = tk.Button(racine,text = "-", width = 10, height = 5, command=moins)
moins.grid(column=3, row=2)

egal = tk.Button(racine, text="=", width = 10, height = 5, command=egal)
egal.grid(column=3, row=5)


effacer = tk.Button(racine, text="effacer", width=10, height=5, command=effacer)
effacer.grid(column=2, row=5)


racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 
