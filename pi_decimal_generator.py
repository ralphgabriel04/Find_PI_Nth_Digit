import math

# Fonction pour calculer Pi avec un nombre précis de décimales
def pi_digits(n):
    """
    Génère Pi tronqué à n décimales.
    
    Arguments :
    n (int) : Le nombre de chiffres après la virgule.

    Retour :
    float : La valeur de Pi tronquée à n décimales.
    """
    factor = 10 ** n  # Multiplier Pi par 10^n pour décaler les décimales
    pi_tronque = math.trunc(math.pi * factor) / factor  # Tronquer Pi et le ramener à l'échelle initiale
    return pi_tronque

# Fonction pour demander à l'utilisateur combien de décimales il souhaite
def demander_nb_decimal_voulu():
    """
    Demande à l'utilisateur un nombre entier positif représentant 
    le nombre de décimales de Pi qu'il souhaite générer.

    Retour :
    int : Nombre de décimales entré par l'utilisateur (valide).
    """
    while True:  # Boucle tant que l'utilisateur n'entre pas une valeur valide
        nb_decimal_voulu = input("Combien de décimales de Pi voulez-vous ? ")
        if nb_decimal_voulu.isdigit():  # Vérifie que l'entrée est un entier positif
            return int(nb_decimal_voulu)
        else:
            print("Veuillez entrer un nombre entier positif : ")

# Point d'entrée principal du programme
if __name__ == "__main__":
    """
    Boucle principale pour interagir avec l'utilisateur. 
    Permet de générer et d'afficher Pi avec un nombre choisi de décimales,
    puis de décider de continuer ou de quitter le programme.
    """
    while True:
        # Demander combien de décimales de Pi afficher
        n = demander_nb_decimal_voulu()
        
        # Afficher Pi avec les décimales demandées
        print(f"PI avec {n} décimales : {pi_digits(n)}")
        
        # Demander si l'utilisateur souhaite continuer
        choix = input("Voulez-vous générer un autre nombre de décimales de Pi ? (O/N) ").strip().upper()
        
        # Vérifier la réponse pour continuer ou arrêter le programme
        if choix == "N":
            print("Au revoir!")  # Message d'adieu
            break  # Quitter la boucle principale
        elif choix != "O":
            print("Veuillez entrer une réponse valide")  # En cas de saisie invalide