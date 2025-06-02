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
    pass


def demander_valeur_numerique_utilisateur(valeur_min, valeur_max):
    """
    Demande à l'utilisateur de saisir une valeur numérique dans une plage spécifiée.

    Parameters:
    valeur_min (int): Valeur minimale autorisée.
    valeur_max (int): Valeur maximale autorisée.

    Returns:
    int: Valeur saisie par l'utilisateur.
    """
    pass


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
    pass

# Menu principal
def main():
    print("Ce programme vous permet d'effectuer des conversions d'unités")

    # Menu : choix de la conversion
    # .........
    

    # Demander les valeurs à convertir à l'utilisateur
    # .........

        
if __name__ == "__main__":
    main()
