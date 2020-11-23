def calculValeur (argument):
    "La fonction affiche quatre fois la valeur de son argument moins 2 si l'argument est supérieur à 1 et affiche -2 sinon. La fonction ne retourne rien."

    if argument > 1:
        argument = (4  *argument) - 2
        print (argument)
    else:
        print ("-2")

help (calculValeur)
    
#calculValeur (3)