class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        print("Bienvenue dans le questionnaire !")
        print("Répondez aux questions suivantes :")
        score = 0
        for question in self.questions:
            question.display_question()
            reponse_utilisateur = input("Entrez le numéro de votre réponse : ")
            if question.choix[int(reponse_utilisateur) - 1] == question.reponse:
                score += 1
                print("Correct !")
            else:
                print(f"Incorrect ! La bonne réponse est : {question.reponse}")
        print()
        print(f"Votre score final est : {score}/{len(self.questions)}")
        print("Merci d'avoir participé !")
        
class Question:
    def __init__(self, question, choix, reponse):
        self.question = question
        self.choix = choix
        self.reponse = reponse
    
    def display_question(self):
        print()
        print("QUESTION")
        print(f"    {self.question}")
        for i, choix in enumerate(self.choix):
            print(f"        {i + 1} - {choix}")
        
            
Questionnaire(
    (
        Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
        Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
        Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()

    