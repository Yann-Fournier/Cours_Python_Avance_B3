# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions


def demander_reponse_numerique_utlisateur(min, max):
    """
        input => min = 1
                 max = nbre des reponses
        output => reponse utilisateur
    """
    while True:
        try:
            reponse = int(input("Votre réponse : "))
            if reponse < min or reponse > max:
                print(f"Veuillez entrer un nombre entre {min} et {max}.")
            else:
                return reponse
        except ValueError:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
    

def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    """
    input : question
                titre = "Quelle est la capitale de la France ?"
                reponses = ("Marseille", "Nice", "Paris", "Nantes")
                bonne_reponse = "Paris"
    output : boolean resultat_response_correcte
    """
    print("Question :")
    print("    ", question[0])
    for i, reponse in enumerate(question[1]):
        print(f"        {i+1} - {reponse}")

def lancer_questionnaire(questionnaire):
    '''
    input :     questionnaire[]
                    question
                        titre = "Quelle est la capitale de la France ?"
                        reponses = ("Marseille", "Nice", "Paris", "Nantes")
                        bonne_reponse = "Paris"
    output : print("Score final :", score, "sur", len(questionnaire))
    '''
    score = 0
    
    for question in questionnaire:
        poser_question(question)
        reponses = question[1]
        bonne_reponse = question[2]
        
        reponse_utilisateur = demander_reponse_numerique_utlisateur(1, len(reponses))
        
        if reponses[reponse_utilisateur - 1] == bonne_reponse:
            print("Bonne réponse !")
            score += 1
        else:
            print("Mauvaise réponse.")
            print("La bonne réponse est :", bonne_reponse)
        print()
    print("Score final :", score, "sur", len(questionnaire))

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)


