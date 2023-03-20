import tkinter as tk
from tkinter import messagebox

 
# Grille prédéfini

sudoku = [

    [8, 0, 0, 9, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 5],
    [6, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 3, 0, 0, 4]

]

 

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Sudoku")

 

# Fonction pour créer la grille de sudoku

def cree_grille():

    # Création d'une grille de 9x9 cases (celle de base dans le jeu sudoku)

    grid = []

    for l in range(9):

        row = []

        for c in range(9):

            cell = tk.Entry(fenetre, width=6)

            cell.grid(row=l, column=c)

            row.append(cell)

        grid.append(row)

    return grid

 

# Création de la grille de sudoku

grille_principale = cree_grille()

 

# Fonction pour charger le puzzle prédéfini

def sudoku_prédéfini(sudoku):

    # Mettre à jour la grille de sudoku avec les chiffres du puzzle prédéfini

    for row in range(9):

        for column in range(9):

            cell = sudoku[row][column]

            if cell != 0:

                cell_entry = grille_principale[row][column]

                cell_entry.delete(0, tk.END)

                cell_entry.insert(0, str(cell))

                         

# Charger la grille prédéfini

sudoku_prédéfini(sudoku)

 

# Fonction pour vérifier la grille de sudoku

def verifie_grille():

    for l in range(9):

        for c in range(9):

            value = grille_principale[l][c].get()

            # Vérifier si la case est vide ou contient une valeur invalide

            if value == "" or not value.isdigit() or int(value) < 1 or int(value) > 9:

                messagebox.showerror("Erreur", "La partie n'est pas terminé.")

                return

    # Vérifier si chaque ligne, colonne et carre 3x3 contient tous les nombres de 1 à 9

    for l in range(9):

        nombre_ligne = set()

        nombre_colone = set()

        nombre_carre = set()

        for c in range(9):

            # Vérifier la ligne l

            if grille_principale[l][c].get() in nombre_ligne:

                messagebox.showerror("Erreur", "La partie n'est pas terminé.")

                return

            nombre_ligne.add(grille_principale[l][c].get())

            # Vérifier la colonne c

            if grille_principale[c][l].get() in nombre_colone:

                messagebox.showerror("Erreur", "La partie n'est pas terminé.")

                return

            nombre_colone.add(grille_principale[c][l].get())

            # Vérifier le carre 3x3 (l // 3, l % 3)

            carre_ligne = (l // 3) * 3 + c // 3

            carre_colone = (l % 3) * 3 + c % 3

            if grille_principale[carre_ligne][carre_colone].get() in nombre_carre:

                messagebox.showerror("Erreur", "La partie n'est pas terminé.")

                return

            nombre_carre.add(grille_principale[carre_ligne][carre_colone].get())

    messagebox.showinfo("Juste", "La grille de Sudoku est correcte !")

# Création du bouton de vérification

check_button = tk.Button(fenetre, text="Go", command=verifie_grille)

check_button.grid(row=9, column=4)



# Affichage de la fenêtre

fenetre.mainloop()

