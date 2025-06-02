"""
Collections
    - liste de conversions possibles

    - pouces -> cm (...)
    - cm -> m
    - km -> miles
"""

# unité de départ, unité d'arrivée, facteur de conversion
CONVERSIONS = (                #   choix   index      pair     (choix-1)//2
    ("pouces", "cm", 2.54),        # 1      0          F         0
                                   # 2      0 + R      T         0
    ("m", "cm", 100),              # 3      1                    1
                                   # 4      1 + R                1
    ("km", "miles", 0.621371),     # 5      2                    2
                                   # 6      2 + R                2
    ("yard", "m", 0.9144), 
    ("kg", "livres", 2.20462),    
)


def conversion_menu(conversions):
    """
    Affiche le menu des conversions et renvoie le choix de l'utilisateur.

    Parameters:
    conversions (tuple): Liste des conversions possibles.

    Returns:
    int: Choix de l'utilisateur.
    """
    print("Menu des Convertions:")
    cpt = 1
    for unit1, unit2, _ in conversions:
        print(f"{cpt}. {unit1} vers {unit2}")
        print(f"{cpt + 1}. {unit2} vers {unit1}")
        cpt += 2
    
    user_input = demander_valeur_numerique_utilisateur(1, len(conversions) * 2)
    while user_input == "N/A":
        user_input = demander_valeur_numerique_utilisateur(1, len(conversions) * 2)
    return user_input
    


def demander_valeur_numerique_utilisateur(valeur_min, valeur_max):
    """
    Demande à l'utilisateur de saisir une valeur numérique dans une plage spécifiée.

    Parameters:
    valeur_min (int): Valeur minimale autorisée.
    valeur_max (int): Valeur maximale autorisée.

    Returns:
    int: Valeur saisie par l'utilisateur.
    """
    user_input = input("Donnez une valeur entre 1 et 6 : ")
    try:
        choix = int(user_input)
        if valeur_min <= choix <= valeur_max:
            return choix
        else:
            print("Choix invalide. Veuillez réessayer.")
            return "N/A"
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return "N/A"


def demander_et_afficher_conversion(unit1, unit2, facteur, reverse=False):
    """
    Demande à l'utilisateur la valeur à convertir et affiche le résultat de la conversion.

    Parameters:
    unit1 (str): Unité de départ.
    unit2 (str): Unité d'arrivée.
    facteur (float): Facteur de conversion.
    reverse (bool, optional): Indique si la conversion inverse doit être effectuée. Par défaut, False.

    Returns:
    bool: True si l'utilisateur souhaite quitter, False sinon.
    """
    if reverse:
        user_input = input(f"Entrez la valeur en {unit2} à convertir en {unit1} (ou 'q' pour quitter): ")
    else:
        user_input = input(f"Entrez la valeur en {unit1} à convertir en {unit2} (ou 'q' pour quitter): ")
    
    if user_input.lower() == 'q':
        print("Merci d'avoir utilisé le programme de conversion. Au revoir!")
        return False
    try:
        valeur = float(user_input)
        if reverse:
            resultat = valeur / facteur
            print(f"Résultat de la convertion : {valeur} {unit2} équivaut à {resultat:.2f} {unit1}")
            return True
        else:
            resultat = valeur * facteur
            print(f"Résultat de la convertion : {valeur} {unit1} équivaut à {resultat:.2f} {unit2}")
            return True
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return True

# Menu principal
def main():
    print("Ce programme vous permet d'effectuer des conversions d'unités")

    # Menu : choix de la conversion
    choix = conversion_menu(CONVERSIONS)
    

    # Demander les valeurs à convertir à l'utilisateur
    boucle_continue = True
    while boucle_continue:
        boucle_continue = demander_et_afficher_conversion(
            CONVERSIONS[(choix - 1) // 2][0],
            CONVERSIONS[(choix - 1) // 2][1],
            CONVERSIONS[(choix - 1) // 2][2],
            reverse=(choix % 2 == 0)
        )

        
if __name__ == "__main__":
    main()
