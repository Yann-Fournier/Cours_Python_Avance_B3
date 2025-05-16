import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import plotly.express as px
import pandas as pd

class Pizza:
    def __init__(self, nom, ingredient=[], prix=7, type="Personnalisée"):
        self.nom = nom
        self.ingredient = ingredient
        self.prix = prix
        self.type = type
        
    def __str__(self):
        return f"PIZZA {self.nom} : {round(self.prix, 2)} € \n {', '.join(self.ingredient)}"
        
    def ajouter_ingredient_price(self):
        if self.type == "Personnalisée":
            self.prix += len(self.ingredient) * 1.2
            

pizzas = [
    Pizza("Hawai", ["tomate", "ananas", "oignons"], 9.5, "Classique"),
    Pizza("4 saisons", ["oeuf", "emmental", "tomate", "jambon", "olives"], 11, "Classique"),
    Pizza("Végétarienne", ["champignons", "tomate", "oignons", "poivrons"], 7.8, "Vegétarienne"),
]

st.title("App de gestion de pizzas")

# Création des onglets
onglet1, onglet2, onglet3, = st.tabs(["Composition", "Menu", "Analyse"])
    
# Contenu du premier onglet
with onglet1:
    st.header("Création d'une pizza personalisée :")
    st.write("Vous pouvez créer une pizza personnalisée en ajoutant des ingrédients.")
    nom = st.text_input("Entrez le nom de votre pizza :")
    ingredients = st.text_input("Entrez les ingrédients de votre pizza (séparés par des virgules) :")
    if st.button("Créer la pizza"):
        if nom and ingredients:
            pizzas_juste_add = Pizza(nom, [ingredient.lower().strip() for ingredient in ingredients.split(",")])
            pizzas_juste_add.ajouter_ingredient_price()
            pizzas.append(pizzas_juste_add)
            st.success(f"Votre pizza '{nom}' a été créée avec les ingrédients : {', '.join(pizzas_juste_add.ingredient)}")
        else:
            st.error("Veuillez entrer un nom et des ingrédients pour créer votre pizza.")
        
# Contenu du deuxième onglet
with onglet2:
    st.header("Menu des pizzas")
    st.write("Voici le menu de nos pizzas :")
    st.write("---")
    for pizza in pizzas:
        if pizza.type == "Vegétarienne":
            st.image("https://cdn-icons-png.flaticon.com/128/3778/3778979.png", width=30)
            st.write("Végétarienne")
        else:
            st.image("https://cdn-icons-png.flaticon.com/128/4058/4058751.png", width=30)
            st.write("Classique")
        st.write(pizza)
        st.write("---")

# Contenu du troisième onglet
with onglet3:
    st.header("Analyse de données")
    st.write("Voici quelques statistiques sur nos pizzas :")
    st.write("---")
    st.write(f"Nombre total de pizzas : {len(pizzas)}")
    
    st.write("---")
    st.write("### Prix :")
    prix_total = sum(pizza.prix for pizza in pizzas)
    st.write(f"Prix total des pizzas : {round(prix_total, 2)} €")
    st.write(f"Prix moyen des pizzas : {round(prix_total / len(pizzas), 2)} €")
    st.write(f"Prix le plus bas : {min(pizza.prix for pizza in pizzas)} €")
    st.write(f"Prix le plus élevé : {max(pizza.prix for pizza in pizzas)} €")
    
    st.write("---")
    st.write("### Ingrédients :")
    ingredients = [ingredient for pizza in pizzas for ingredient in pizza.ingredient]
    unique_ingredients = set(ingredients)
    moyenne_ingredients = sum(len(pizza.ingredient) for pizza in pizzas) / len(pizzas)
    st.write(f"Nombre total d'ingrédients : {len(unique_ingredients)}")
    st.write(f"Liste des ingrédients : {', '.join(unique_ingredients)}")
    st.write(f"Nombre moyen d'ingrédients par pizza : {moyenne_ingredients}")
    
    ingredient_counts = Counter(ingredients)
    # Optionnel : top N ingrédients les plus fréquents
    top_ingredients = ingredient_counts.most_common(10)  # top 10
    df = pd.DataFrame(top_ingredients, columns=["Ingrédient", "Occurrences"]) # Transformer en DataFrame
    # Affichage du graphique en barres
    fig = px.bar(df, x="Ingrédient", y="Occurrences", title="Top 10 des ingrédients les plus populaires")
    st.plotly_chart(fig)
    
    st.write("---")
    st.write("### Types de pizzas :")
    types = [pizza.type for pizza in pizzas]
    # Comptage
    type_counts = Counter(types)
    # Données pour le graphique
    labels = list(type_counts.keys())
    sizes = list(type_counts.values())
    # Création du graphique
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Pour un cercle parfait
    ax.set_title("Répartition des types de pizzas")
    st.pyplot(fig)
    st.write("---")


