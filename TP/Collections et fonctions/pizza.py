def tri_personnalise(liste):
    """
    Trie une liste de chaînes de caractères par ordre croissant de leur longueur.
    Si deux chaînes ont la même longueur, elles sont triées par ordre alphabétique.
    
    Args:
        liste (list): Liste de chaînes de caractères à trier.
    
    Returns:
        list: Liste triée.
    """
    return sorted(liste, key=lambda x: (len(x), x))

def pizza_existe(pizza, liste_pizzas):
    """
    Vérifie si une pizza existe dans une liste de pizzas.
    
    Args:
        pizza (str): Nom de la pizza à vérifier.
        liste_pizzas (list): Liste de pizzas.
    
    Returns:
        bool: True si la pizza existe, False sinon.
    """
    return pizza in liste_pizzas

def ajouter_pizza_utilisateur(pizza, liste_pizzas):
    """
    Ajoute une pizza à une liste de pizzas si elle n'existe pas déjà.
    
    Args:
        pizza (str): Nom de la pizza à ajouter.
        liste_pizzas (list): Liste de pizzas.
    
    Returns:
        list: Liste mise à jour des pizzas.
    """
    if not pizza_existe(pizza, liste_pizzas):
        liste_pizzas.append(pizza)
    else:
        print( "ERREUR: Cette pizza existe déjà")
    return liste_pizzas

def afficher(liste_pizzas):
    """
    Affiche la liste des pizzas.
    
    Args:
        liste_pizzas (list): Liste de pizzas à afficher.
    """
    liste_pizzas_triee = tri_personnalise(liste_pizzas)
    print(f"---- Liste des pizzas ({len(liste_pizzas)}) : ----")
    for pizza in liste_pizzas:
        print(f"{pizza}")
        
    print()
    
    print("Pizza la plus courte :", liste_pizzas_triee[0])
    print("Pizza la plus longue :", liste_pizzas_triee[-1])
    print("Première pizza :", liste_pizzas[0])
    print("Dernière pizza :", liste_pizzas[-1])
    
if __name__ == "__main__":
    # Collection initiale de pizzas
    pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
    
    stop = False # Variable pour arrêter la boucle
    
    while not stop:
        # Input de l'utilisateur
        input_pizza = input("Pizza à ajouter ('q' pour sortir du programme) : ")
        
        if input_pizza == "q":
            stop = True
            print("Fin du programme")
            break
        
        # Ajout de la pizza à la collection
        pizzas = ajouter_pizza_utilisateur(input_pizza, pizzas)
        
        # Affichage de la collection
        afficher(pizzas)
    
    