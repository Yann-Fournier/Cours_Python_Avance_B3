NIVEAUX_DIFFICULTE = (
    {
        "titre": "Facile",
        "longueur_seq_initiale": 3,
        "duree_memorisation_sec": 4,
        "increment_sequence": 1,
        "nombre_essais": 2,
    },
    {
        "titre": "Normal",
        "longueur_seq_initiale": 4,
        "duree_memorisation_sec": 3,
        "increment_sequence": 1,
        "nombre_essais": 1,
    },
    {
        "titre": "Difficile",
        "longueur_seq_initiale": 5,
        "duree_memorisation_sec": 2,
        "increment_sequence": 2,
        "nombre_essais": 0,
    }
)

import time
import random
import os
 
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# Prototype à compléter par les étudiants
def demander_valeur_numerique_min_max(min, max):
    """
    Demande à l'utilisateur de saisir une valeur numérique entre min et max.
    Retourne la valeur saisie après s'assurer qu'elle est valide.
    """
    while True:
        try:
            valeur = int(input(f"Veuillez entrer un nombre entre {min} et {max}: "))
            if min <= valeur <= max:
                return valeur
            else:
                print(f"Erreur : la valeur doit être entre {min} et {max}.\n")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.\n")

# Prototype à compléter par les étudiants
def choix_niveau_difficulte(niveaux_difficulte):
    """
    Affiche les niveaux de difficulté et demande à l'utilisateur de choisir un niveau.
    Retourne le dictionnaire du niveau choisi.
    """
    print("Choisissez un niveau de difficulté:")
    print("1 - Facile")
    print("2 - Normal")
    print("3 - Difficile")
    
    choix_niveau = demander_valeur_numerique_min_max(1, 3)
    
    return niveaux_difficulte[choix_niveau - 1]

# Prototype à compléter par les étudiants
def generer_chiffre_(n):
    """
    Génère une séquence de chiffres aléatoires de longueur n.
    Retourne la séquence générée.
    """
    seq = ""
    for i in range(n):
        seq += str(random.randint(0, 9))
    return seq

# Prototype à compléter par les étudiants
def afficher_message_fin(score, sequence):
    """
    Affiche un message de fin de jeu avec le score et la séquence.
    """
    clear_screen()
    print("Fin du jeu!")
    print(f"Votre score est: {score}")
    print("Merci d'avoir joué!")

# Prototype à compléter par les étudiants
def jouer_jeu():
    """
    Fonction principale qui gère le déroulement du jeu.
    """
    scrore = 0
    clear_screen()
    
    choix_niveau = choix_niveau_difficulte(NIVEAUX_DIFFICULTE)
    
    longeure_seq_init = choix_niveau["longueur_seq_initiale"]
    nbr_essais = choix_niveau["nombre_essais"]
    duree_memorisation = choix_niveau["duree_memorisation_sec"]
    
    seq = generer_chiffre_(longeure_seq_init)
    
    clear_screen()
    
    while nbr_essais >= 0:
        print("Retenez la séquence suivante:")
        print(seq)
        time.sleep(duree_memorisation)
        
        clear_screen()
        print("Entrez la séquence:")
        reponse = input()
        
        if reponse == seq:
            print("Bravo! Vous avez trouvé la séquence.")
            scrore += 1
            seq += generer_chiffre_(1)
            time.sleep(5)
            clear_screen()
        else:
            print("Dommage! Mauvaise réponse.")
            print()
            nbr_essais -= 1
            if nbr_essais >= 0:
                print(f"Il vous reste {nbr_essais} essais.")
                time.sleep(5)
                clear_screen()
            else:
                print("Vous avez perdu!")
                print(f"La séquence était: {seq}")
                print(f"Votre reponse : {reponse}")
                time.sleep(5)
                clear_screen()
                afficher_message_fin(scrore, seq)
                break
    
    
# Appeler la fonction principale
jouer_jeu()
