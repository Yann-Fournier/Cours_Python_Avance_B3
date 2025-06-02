import time

def decompte(temps_min: int) -> None:
    """
    **Description :** \n
    Fonction de compte à rebours pour la cuisson des oeufs.
    
    -----------
    **input :** \n
    temps_min (int) : Temps de cuisson en minutes 
    
    ---------------
    **output :** \n
        None
    """
    cpt = 0
    print()
    print(f"Cuisson de {temps_min} minutes .............")
    for i in range(temps_min * 60, 0, -1):
        if cpt == 10:
            print(f"Temps restant : {int(i/60)}:{i%60} ...........")
            cpt = 0
        time.sleep(1)
        cpt += 1
    print("C'est prêt !")

a_choisi = False
input_choix = 0

print("Cuisson des oeufs")
print("1 - Oeuf à la coque : 3 minutes")
print("2 - Oeuf mollet : 6 minutes")
print("3 - Oeuf dur : 9 minutes")

while not a_choisi:
    try:
        input_choix = int(input("Votre choix (1, 2 ou 3) : "))
        if input_choix < 1 or input_choix > 3:
            print(f"Veuillez entrer un chiffre entre 1 et 3.")
        else:
            a_choisi = True
    except ValueError:
        print("ERREUR : Veuillez rentrer uniquement un chiffres entre 1 et 3")

# Appel de la fonction de compte à rebours
if input_choix == 1:
    decompte(3)
elif input_choix == 2:
    decompte(6)
elif input_choix == 3:
    decompte(9)
