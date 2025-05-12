class Personne1:
    def __init__(self, prenom, age):
        self.age = age
        self.prenom = prenom
        print(f"Constructeur Personne {self.prenom}")

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom}, j'ai {self.age} ans.")
    
    def demander_nom(self):
        print(f"Quel est votre nom ?")
    
    def est_majeur(self):
        if self.age >= 18:
            print("Je suis majeur.")
        else:
            print("Je suis mineur.")
    
    def info_etre_vivant(self):
        print(f"Info être vivant : Humain (Mammifère Homo sapiens)")
        
personne1_1 = Personne1('Jean', 30)
personne1_2 = Personne1('Paul', 15)
personne1_3 = Personne1('Zoe', 20)
print()
personne1_1.se_presenter()
personne1_1.est_majeur()
personne1_1.info_etre_vivant()
print()
personne1_2.se_presenter()
personne1_2.est_majeur()
personne1_2.info_etre_vivant()
print()
personne1_3.se_presenter()
personne1_3.est_majeur()
personne1_3.info_etre_vivant()
