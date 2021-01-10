import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine

racine.title("Calculatrice") 

def ajouteTexte():
    resultat.config(text= "test")


resultat = tk.Label(racine,text = "Résultat (à modifier)", width = 44, height = 5)
resultat.grid(column=0, row=0, columnspan = 4)

un = tk.Button(racine,text = "1",width = 10, height = 5, command=ajouteTexte)
un.grid(column=0, row=1)


deux = tk.Button(racine,text = "2", width = 10, height = 5)
deux.grid(column=1, row=1)

trois = tk.Button(racine,text = "3", width = 10, height = 5)
trois.grid(column=2, row=1)

quatre = tk.Button(racine,text = "4", width = 10, height = 5)
quatre.grid(column=0, row=2)

cinq = tk.Button(racine,text = "5", width = 10, height = 5)
cinq.grid(column=1, row=2)

six = tk.Button(racine,text = "6", width = 10, height = 5)
six.grid(column=2, row=2)

sept = tk.Button(racine,text = "7", width = 10, height = 5)
sept.grid(column=0, row=3)

huit = tk.Button(racine,text = "8", width = 10, height = 5)
huit.grid(column=1, row=3)

neuf = tk.Button(racine,text = "9", width = 10, height = 5)
neuf.grid(column=2, row=3)

zero = tk.Button(racine,text = "0", width = 10, height = 5)
zero.grid(column=1, row=4)

virgule = tk.Button(racine,text = ".", width = 10, height = 5)
virgule.grid(column=2, row=4)

plus = tk.Button(racine,text = "+", width =10, height = 5)
plus.grid(column=3, row=1)

fois = tk.Button(racine,text = "x", width =10, height = 5)
fois.grid(column=3, row=3)

diviser = tk.Button(racine,text = "/", width = 10, height = 5)
diviser.grid(column=3, row=4)

moins = tk.Button(racine,text = "-", width = 10, height = 5)
moins.grid(column=3, row=2)



racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 
