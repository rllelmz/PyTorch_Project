ÉTAPE 1: Créer un environnement virtuel Python ou bien un projet sous PyCharm 

ÉTAPE 2: Installer les packages nécessaires dans cet environnement (Conda ou pip) & Ouverture d'un nouveau fichier python:
    - Pytorch 
    - Pandas
    - Scikit-learn
    - Tkinter
    - Matplotlib 

ÉTAPE 3: Normaliser les labels avec le fichier Normalisation_generique.py
    - prend en compte que des fichiers CSV
    - encode les labels et les normalise 
    - normalise les variables numériques 
    - normalise pas les variables au format datetime 
    - lors de l'enregistrement des données normalisées, inutile de rajouter l'extension ".csv"
P.S : si un warning "SettingWithCopyWarning" ne pas tenir compte de ce message 

ÉTAPE 4: Choix du travail à faire
    - ANN_Pytorch_Classification.py: classification binaire et multi-classes; il suffit de compiler et suivre les instructions; 
    - ANN_Pytorch_Regression: régression, il suffit de compiler et suivre les instructions 
         - PER = float(input("Saisir le pourcentage de précision entre la valeur initiale et la valeur prédite par le modèle (ex: 0.15): ")) → exemple: si le prix cible dans les données d'apprentissage est de 400€ et le pourcentage de précision est de 20%, un prix prédit compris entre 320€ et 480€ sera considéré comme juste;
    - application d'un ANN pour la régression: ANN_Pytorch_ParisHousingPrice.py
    - application d'un ANN pour la classification: ANN_Pytorch_WaterQuality.py 



