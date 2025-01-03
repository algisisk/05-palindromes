"""
Ce module contient une fonction pour vérifier si un mot est palindrome,
ainsi qu'une fonction principale pour afficher les mots palindromes dans la liste de test.
"""

import string
from unidecode import unidecode

#### Fonction secondaire
# La fonction ispalindrome() permet de renvoyer si le mot en paramètre est un palindrome

def ispalindrome(p):
    """
    Détermine si un mot est palindrome

    Paramètre:
    p (str): Le mot à vérifier

    Retourne:
    bool: True si le mot est un palindrome, False sinon
    """
    # unicode() enlève les accents des lettres
    # replace() enlève les espaces
    # translate(...) enlève les ponctuations
    # str[::-1] renverse la chaîne de caractère
    #
    #---Version normale---#
    #
    # p_normal = unidecode(p).lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))
    # p_invers = unidecode(p).lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))[::-1]
    #
    # return p_normal == p_invers

    #---Version récursive---#
    p = unidecode(p).lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))
    if len(p) <= 0:
        return True
    if p[0] == p[-1]:
        return ispalindrome(p[1:-1])
    return False
    #-----------------------#

#### Fonction principale
# Fonction principale qui fait tourner le code
# en testant si les mots mis dans la liste sont palindromes ou pas

def main():
    """
    Affiche les mots qui sont des palindromes
    """
    for s in ["radar", "kayak", "level", "rotor", "civique",
              "deifie","Oh ! cela te perd, répéta l'écho","12341321"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
