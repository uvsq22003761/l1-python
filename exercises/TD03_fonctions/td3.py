#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes = 0
    secondes = (temps [0] * 24 * 60 * 60) + (temps [1] * 60 * 60) + (temps [2] * 60) + temps [3] 
    return secondes

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))  

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de 
    seconde passé en argument"""

    jours = seconde // (24 * 60 * 60)
    heures = (seconde // (60 * 60)) - (jours * 24)
    minutes = (seconde // 60) - (heures * 60) - (jours * 24 * 60)
    secondes = seconde - (minutes * 60) - (heures * 60 * 60) - (jours * 24 * 60 *60)
    temps = (jours, heures, minutes, secondes)
    return temps
    
#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


def motAuPluriel(temps,mot):
    """Met un mot au pluriel, il faut que le mot soit au singulier. 
    La fonction ne détecte pas si le mot est à la base au singulier ou au pluriel"""

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

#afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    temps1 = tempsEnSeconde(temps1)
    temps2 = tempsEnSeconde(temps2)
    somme_secondes = temps1 + temps2

    secondeEnTemps(somme_secondes)

#sommeTemps((2,3,4,25),(5,22,57,1))
#afficheTemps(temps)

def proportionTemps(temps,proportion):
    tempsEnSecondes = tempsEnSeconde(temps)
    proportionTemps = int(tempsEnSecondes * proportion)
    proportionTemps = secondeEnTemps (proportionTemps)

    return proportionTemps

#afficheTemps(proportionTemps((2,0,36,0),0.2))
