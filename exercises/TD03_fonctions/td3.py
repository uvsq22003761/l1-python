# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes = 0
    secondes = (temps [0] * 24 * 60 * 60) + (temps [1] * 60 * 60) + (temps [2] * 60) + temps [3] 
    return secondes

# temps = (3,23,1,34)
# print(type(temps))
# print(tempsEnSeconde(temps)) 


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de 
    seconde passé en argument"""

    jours = seconde // (86400)
    heures = (seconde // (3600)) - (jours * 24)
    minutes = (seconde // 60) - (heures * 60) - (jours * 1440)
    secondes = seconde - (minutes * 60) - (heures * 3600) - (jours * 86400)
    temps = (jours, heures, minutes, secondes)
    return temps
   
# temps = secondeEnTemps(100000)
# print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


def motAuPluriel(temps, mot):
    """ Met un mot au pluriel, il faut que le mot soit au singulier. 
    La fonction ne détecte pas si le mot est à la base au singulier ou au pluriel """

    if temps > 1:
        return mot + "s"
    elif temps == 1:
        return mot
    else:
        return ""   
  

def afficheTemps(temps):
    """Permet d'afficher un temps """

    print ("Temps:", temps[0], motAuPluriel(temps[0],"jour"), \
    temps [1], motAuPluriel(temps[1],"heure"), temps [2], motAuPluriel(temps[2],"minute"), \
    temps[3], motAuPluriel(temps[3],"seconde")) 
    #Message pour afficher le temps, avec utilisation de la fonction motAuPluriel.


def demandeTemps():
    """Demande à l'utilisateur de rentrer un temps. Si l'utilisateur entre un temps incorrect
    la fonction renvoie un message d'erreur et lui demande de rentrer une nouvelle valeur correcte """

    jours = int(input("Entrer le temps, en commencant par le(s) jours(s):"))
    
    heures = int(input("Entrer le nombre d'heure(s):"))
    while heures >= 24:
        heures = int(input("Erreur votre nombre n'est pas réduit au maximum, rentrer une nouvelle valeur svp."))

    minutes = int(input("Entrer le nombre de minute(s):"))
    while minutes >= 60:
        minutes = int(input("Erreur votre nombre n'est pas réduit au maximum, rentrer une nouvelle valeur svp."))

    secondes = int(input("Entrer le nombre de minute(s):"))
    while secondes >= 60:
        secondes = int(input("Erreur votre nombre n'est pas réduit au maximum, rentrer une nouvelle valeur svp."))

    temps = (jours, heures, minutes, secondes)
    return temps 

# afficheTemps(demandeTemps())


def sommeTemps(temps1, temps2):
    """Permet de faire la somme de temps. """
    temps1 = tempsEnSeconde(temps1)
    temps2 = tempsEnSeconde(temps2)
    somme_secondes = temps1 + temps2

    secondeEnTemps(somme_secondes)

# sommeTemps((2,3,4,25),(5,22,57,1))
# afficheTemps(temps)


def proportionTemps(temps, proportion):
    """Permet de connaitre la proportion d'un temps. """
    tempsEnSecondes = tempsEnSeconde(temps)
    proportionTemps = int(tempsEnSecondes * proportion)
    proportionTemps = secondeEnTemps (proportionTemps)

    return proportionTemps

#afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))

def tempsEnDate(temps):
    """Fonction qui donne la date sous la forme (année, mois, jours, heures, minutes, secondes)"""

    """Rappel, la fonction secondeEnTemps est de la forme temps = (jours, heures, minutes, 
    secondes)"""

    jours = temps[0]
    heures = temps[1]
    minutes = temps[2]
    secondes = temps[3]
    années = 1970

    while jours > 366: 
        if (années % 4 == 0 and années % 100 != 0) or (années % 400 == 0):#Si c'est une année bissextile
            années += 1
            jours -= 366
        elif (années % 4 != 0) or (années % 100 == 0 and années % 400 != 0): 
        # si ce n'est pas une année bissextile
            années += 1
            jours -= 365

    date = (années, jours, heures, minutes, secondes)
    print(date)
    return date


def afficheDate(date):
    """Permet d'afficher une date """
    """On rapelle que temps [0] = années; temps [1] = jours; temps [2] = heures; 
    temps [3] = minutes et temps [4] = secondes"""

    print ("Date:", date[0], motAuPluriel(date[0], "an"), date[1],\
    motAuPluriel(date[1], "jour"), date[2], motAuPluriel(date[2], "heure"),\
    date[3], motAuPluriel(date[3], "minute"), date[4], motAuPluriel(date[4],"seconde"))


#temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()


def bissextile(jours):
    """Renvoie les années bissextiles depuis 1 janvier 2020 à 00:00:00 jusqu'à la fin de 
    ces jours """

    années = 2020

    while jours > 366: 
        if (années % 4 == 0 and années % 100 != 0) or (années % 400 == 0):#Si c'est une année bissextile
            print (années)
            jours -= 366
            années += 1
        elif (années % 4 != 0) or (années % 100 == 0 and années % 400 != 0): 
        # si ce n'est pas une année bissextile
            années += 1
            jours -= 365

#bissextile(20000)

def nombreBisextile(jours):
    """Compte le nombre d'année bissextile depuis 1970 jusqu'aux nombres de jours donnés. """

    compteur_année_bissextile = 0
    années = 1970

    while jours > 366: 
        if (années % 4 == 0 and années % 100 != 0) or (années % 400 == 0):#Si c'est une année bissextile
            compteur_année_bissextile += 1
            jours -= 366
            années += 1
        elif (années % 4 != 0) or (années % 100 == 0 and années % 400 != 0): 
        # si ce n'est pas une année bissextile
            années += 1
            jours -= 365

    return compteur_année_bissextile


def tempsEnDateBisextile(temps):
    """Fonction qui donne la date sous la forme (année, mois, jours, heures, minutes, secondes)"""

    années = 1970
    nombreBisextile(temps[0])
    jours = temps [0] 

    while compteur_année_bissextile != 0:
        années += 1
        jours -= 366
        
    while temps[0] >= 365:
        années += 1
        jours -= 365

    date = (années, jours, temps[1], temps[2], temps[3])
    return date

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))