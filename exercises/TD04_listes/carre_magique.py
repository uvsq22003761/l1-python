carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 3, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    L = carre
    print (L[0])
    print (L[1])
    print (L[2])
    print (L[3])

#afficheCarre(carre_mag)
#afficheCarre(carre_pas_mag)

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes
    les lignes ont la même somme, et -1 sinon """
    L = carre

    somme_ligne0 = L[0][0] + L[0][1] + L[0][2] + L[0][3]
    somme_ligne1 = L[1][0] + L[1][1] + L[1][2] + L[1][3]
    somme_ligne2 = L[2][0] + L[2][1] + L[2][2] + L[2][3]
    somme_ligne3 = L[3][0] + L[3][1] + L[3][2] + L[3][3]

    if somme_ligne0 == somme_ligne1 == somme_ligne2 == somme_ligne3:
        return (somme_ligne0)

    else:
        return -1

#print(testLignesEgales(carre_mag))
#print(testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre
    si toutes les colonnes ont la même somme, et -1 sinon """
    L = carre
    somme_colonne0 = 0
    somme_colonne1 = 0
    somme_colonne2 = 0
    somme_colonne3 = 0

    for i in range (0, 4):
        somme_colonne0 += L[i][0]
    
    for i in range (0, 4):
        somme_colonne1 += L[i][1]

    for i in range (0, 4):
        somme_colonne2 += L[i][2]

    for i in range (0, 4):
        somme_colonne3 += L[i][3]

    if somme_colonne0 == somme_colonne1 == somme_colonne2 == somme_colonne3:
        return somme_colonne0

    else:
        return -1


#print(testColonnesEgales(carre_mag))
#print(testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 
    2 diagonales ont la même somme, et -1 sinon """

    L = carre

    somme_diagonale_gauche = L[0][0] + L[1][1] + L[2][2] + L[3][3]
    somme_diagonale_droite =L[0][3] + L[1][2] + L[2][1] + L[3][0]

    if somme_diagonale_droite == somme_diagonale_gauche:
        return somme_diagonale_droite

    else:
        return -1
   
#print(testDiagonalesEgales(carre_mag))
#print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""

    if testLignesEgales(carre) != -1 and testColonnesEgales != -1 and testDiagonalesEgales != -1:
        return True

    else:
        return False


#print(estCarreMagique(carre_mag))
#print(estCarreMagique(carre_pas_mag))

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
    du carré, et False sinon """

    n = len(carre[1])

    for i in range(1, (n**2) +1):
        if i not in carre[0] and i not in carre[1] and i not in carre[2] \
        and i not in carre[3]:
            return False

    return True

#print(estNormal(carre_mag))
#print(estNormal(carre_pas_mag))