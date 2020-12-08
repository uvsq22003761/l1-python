# chiffrer: qd on a la clef secrète. Texte clair vers un txt chiffré.

# Déchiffrer: qd on a la clé secrète. Txt chiffré vers txt clair.

# Décripter: qd on n a pas la clef secrète. Txt chiffré vers txt clair.

#Chiffre et déchiffre avec une clé k (entier pris entre 0 et 25)


def chiffreCesar(clef, clair):
    #Ici on suppose que clair ne contient que des A-Z
    """Clef est un entier compris entre 0 et 25. Clair est une chaine de caractère.
    Fonction qui va chiffrer une chaine de caractère choisie."""
    chiffre = ""
    for c in clair:
        tmp = ord(c) + clef
        #c est un caractère
        if (tmp > 90):
            tmp = ord(c) - 26 + clef
        chiffre = chiffre + chr(tmp)
    
    return chiffre

def dechiffreCesar(clef, chiffre):
    clair = ""
    for c in chiffre:
        tmp = ord(c) - clef
        if (tmp < 65):
            tmp = ord(c) + 26 - clef
        clair += chr(tmp)
    return clair

ch = "MESSAGE"
s = (chiffreCesar(5, ch))
print(dechiffreCesar(5, s))
#ord() donne le code ascii

