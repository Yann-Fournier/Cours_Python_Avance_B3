# Plan de test par fichier
---

### controller.py
---

Les seules fonction que l'on peut tester avec des tests unitaires sont les fonctions '_is_input_valid' et '_is_quit' car les autres fonctions dépendent d'autre fonction donc les tester reviendrait à ne pas faire des tests unitaires

- Essayer avec différents types d'input

### operators.py
---

Pour les focntions avec les noms des opérations :
- Vérifier qu'elles instencient bien les bonnes valeurs au bon endroit

Pour les fonctions de calculs :
- Verifier le calcule avec des valeurs positives
- Verifier le calcule avec des valeurs négatives
- Verifier le calcule avec des valeurs égale à 0
- Verifier le calcule avec plusieurs opérateur
- Verifier le calcule avec des opérateurs différents

Pour les fonctions de vérifications :
- Tester le plus de cas différents possible


### view.py
---

Je ne vois pas quels test unitaire on peut faire sur des prints et sur des inputs. En plus, il n'y a que des methodes statics à l'interieur du fichier.
