
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """

    list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            list.append(n)
        elif n % 2 != 0:
            n = (n * 3) + 1    
            list.append(n)     

    return list

#print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range (1, n_max+1):
        syracuse(i)
    
    return True

#print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    syracuse(n)
    tempsVol = len(syracuse(n)) - 1
    return tempsVol
    

#print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    list_tempsVolListe = [tempsVol(i) for i in range(1, n_max + 1)]


    return list_tempsVolListe

#print(tempsVolListe(100))

def plusGrandTempsVol(x):
    listeTpsVol = tempsVolListe(x)
    m = max(listeTpsVol)
    print ("Le temps de vol le plus grand vaut pour n =", m, \
    "pour un temps de vol égal à", listeTpsVol.index(m))

#plusGrandTempsVol(10000)


#La suite ne fonctionne pas \/
def altitudeMax(n):
    list = syracuse(n)
    maxi = max(list)

    return maxi

def altitudeMaxPlusieursListes(n_max):
    liste_altitude_max = (altitudeMax(i) for i in range (1, n_max))
    p = max(liste_altitude_max)

    print("La plus grande altitude est", int(p), "atteint en")#liste_altitude_max.index(p))


altitudeMaxPlusieursListes(10000)




