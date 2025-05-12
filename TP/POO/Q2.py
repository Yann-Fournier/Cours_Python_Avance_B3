class EtreVivant:
    def __init__(self):
        pass
    
    def info_etre_vivant(self):
        print(f"Info être vivant : (être vivant non identifié)")
        
         
class Chat(EtreVivant):
    def __init__(self):
        pass
    
    def info_etre_vivant(self):
        print(f"Info être vivant : Chat (Mammifère félin)")    
     
        
class Personne2(EtreVivant):
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
    
    def info_travail(self, travail):
        print(f"Je suis {travail}") 

      
personne2_1 = Personne2('Jean', 30)
personne2_2 = Personne2('Paul', 15)
personne2_3 = Personne2('Zoe', 20)
print()
personne2_1.se_presenter()
personne2_1.est_majeur()
personne2_1.info_etre_vivant()
print()
personne2_2.se_presenter()
personne2_2.est_majeur()
personne2_2.info_etre_vivant()
print()
personne2_3.se_presenter()
personne2_3.est_majeur()
personne2_3.info_etre_vivant()
print()
chat = Chat()
chat.info_etre_vivant()
print()
chien = EtreVivant()
chien.info_etre_vivant()
print()
personne2_4 = Personne2('Marc', 22)
personne2_4.se_presenter()
personne2_4.est_majeur()
personne2_4.info_travail("etudiant en Ecole d'ingénieur en informatique")
personne2_4.info_etre_vivant()
print()
