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

def sudoku_predefini(sudoku):

    # Mettre à jour la grille de sudoku avec les chiffres du puzzle prédéfini

    for row in range(9):

        for column in range(9):

            cell = sudoku[row][column]

            if cell != 0:

                cell_entry = grille_principale[row][column]

                cell_entry.delete(0, tk.END)

                cell_entry.insert(0, str(cell))

                         

# Charger la grille prédéfini

sudoku_predefini(sudoku)


# Affichage de la fenêtre

fenetre.mainloop()