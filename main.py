"""
Ce module contient une fonction pour vérifier si un mot est palindrome,
ainsi qu'une fonction principale pour afficher les mots palindromes dans la liste de test.
"""

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
    #return p == "".join(list(p).slit().reverse())
    return p == p[::-1]


#### Fonction principale
# Fonction principale qui fait tourner le code en testant si les mots mis dans la liste sont palindromes

def main():
    """
    Affiche les mots qui sont des palindromes
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()