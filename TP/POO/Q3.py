class Pizza:
    def __init__(self, nom, ingredient=[], prix=7, type="Personnalisée"):
        self.nom = nom
        self.ingredient = ingredient
        self.prix = prix
        self.type = type
        
    def __str__(self):
        print(f"PIZZA {self.nom} : {round(self.prix, 2)} €")
        print(f"{', '.join(self.ingredient)}")
        
    def ajouter_ingredient(self):
        if self.type == "Personnalisée":
            boucle = True
            while boucle:
                input_ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
                if input_ingredient == "" and len(self.ingredient) == 0:
                    print("Vous devez ajouter au moins un ingrédient à votre pizza.")
                    print()
                elif input_ingredient == "" and len(self.ingredient) > 0:
                    boucle = False
                else:
                    print(f"Vous avez 1 ingrédient(s) : {input_ingredient}")
                    self.ingredient.append(input_ingredient)
                    self.prix += 1.2
            print(f"Votre pizza {self.nom} a été créée avec succès ! Elle coûte {round(self.prix, 2)} €")


def bienvenue():
    boucle = True
    pizzas = [
        Pizza("Hawai", ["tomate", "ananas", "oignons"], 9.5, "Classique"),
        Pizza("4 saisons", ["oeuf", "emmental", "tomate", "jambon", "olives"], 11, "Classique"),
        Pizza("Végétarienne", ["champignons", "tomate", "oignons", "poivrons"], 7.8, "Classique")
    ]
    
    print("Bienvenue dans le programme de gestion de pizza !")
    print("Vous pouvez créer une pizza personnalisée ou voir la liste des pizzas disponibles.")
    print("Choisissez une option : ")
    print("1 - Créer une pizza personnalisée")
    print("2 - Voir la liste des pizzas")
    print("3 - Afficher les informations sur les prix")
    print("4 - Quitter le programme")
    
    while boucle:
        print()
        choix = input("Entrez votre choix (1, 2 ou 3) : ")
        if choix == "1":
            print()
            print("Vous avez choisi de créer une pizza personnalisée.")
            nom_correct = False
            while not nom_correct:
                nom = input("Entrez le nom de votre pizza : ")
                if len(nom) > 0:
                    nom_correct = True
                else:
                    print("Le nom de la pizza ne peut pas être vide.")
            pizza_personnalisee = Pizza(nom)
            pizza_personnalisee.ajouter_ingredient()
            pizzas.append(pizza_personnalisee)
        elif choix == "2":
            print()
            print("Voici la liste des pizzas disponibles :")
            for pizza in pizzas:
                print()
                pizza.__str__()
        elif choix == "3":
            print()
            print("Voici les informations sur les prix des pizzas personnalisée :")
            print("PRIX_DE_BASE : 7 €")
            print("PRIX_INGREDIENT : 1,2 €")
        elif choix == "4":
            print()
            print("Merci d'avoir utilisé le programme de gestion de pizza !")
            boucle = False
        else:
            print("Choix invalide. Veuillez réessayer.")

bienvenue()
