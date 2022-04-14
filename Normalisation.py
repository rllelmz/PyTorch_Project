import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Choix du fichier csv à lire
root = tk.Tk()
root.withdraw()
file_type = [("csv files", "*.csv")]
file_path = filedialog.askopenfilename(title="Choisir un fichier", filetypes=file_type)

# Lire le fichier csv
df = pd.read_csv(file_path)
print(df.head(10))

# Fonction pour normaliser chaque colonne de la dataframe
def min_max_scaling(column):
    return round((column - column.min()) / (column.max() - column.min()), 3)

for col in df.columns:
    df[col] = min_max_scaling(df[col])
print(df.tail(10))


# Enregistrement de la dataframe normalisé dans un fichier csv
try:
    with filedialog.asksaveasfile(mode="w", defaultextension=".csv") as file:
        df.to_csv(file.name, index=False)
        print("Fichier crée !!")
except AttributeError:
    print("Fichier non sauvegardé !!")

root.destroy()  # Fermeture de la fenêtre
