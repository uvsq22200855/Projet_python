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

    for ligne in range(9):

        # Créer une nouvelle ligne pour la grille

        row = []

        for colonne in range(9):

            # Créer un nouveau compartiment pour la grille

            compartiment = tk.Entry(fenetre, width=6)

            # le positioner dans la grille

            compartiment.grid(row=ligne, column=colonne)

            # Ajouter la case à la ligne

            row.append(compartiment)

        # Ajouter la ligne à la grille

        grid.append(row)

    # Renvoyer la grille complète

    return grid

 

# Création de la grille de sudoku en ajoutant grille_principale a la fonction 

grille_principale = cree_grille()

 

# Fonction pour charger la grille prédéfini

def sudoku_prédéfini(sudoku):

    # Mettre à jour la grille de sudoku avec les chiffres de la grille prédéfini

    for row in range(9):
        for column in range(9):

            cell = sudoku[row][column]
            if cell != 0:

                cell_entry = grille_principale[row][column]

                

                #permet d'afficher les chiffres autre que zero dans les cases
                cell_entry.insert(0, str(cell))

                         

# Charger la grille prédéfini
sudoku_prédéfini(sudoku)

 
# Fonction pour vérifier la grille de sudoku

def verifie_grille():
    for l in range(9):
        for c in range(9):

            value = grille_principale[l][c].get()
            if value == "" or not value.isdigit() or int(value) < 1 or int(value) > 9:

                messagebox.showerror("Erreur", "Il y a une erreur dans la case ({}, {}).".format(l+1, c+1))   #vide ou valeur invalide
                return

    for l in range(9):

        nombre_ligne = set()
        nombre_colone = set()
        nombre_carre = set()

        for c in range(9):
            # Vérifier la ligne l

            if grille_principale[l][c].get() in nombre_ligne:
                messagebox.showerror("Erreur", "Il y a une erreur dans la ligne {}.".format(l+1))
                return
            nombre_ligne.add(grille_principale[l][c].get())

            # Vérifier la colonne c

            if grille_principale[c][l].get() in nombre_colone:
                messagebox.showerror("Erreur", "Il y a une erreur dans la colonne {}.".format(l+1))
                return
            nombre_colone.add(grille_principale[c][l].get())

            # Vérifier le carre 3x3 (l // 3, l % 3)

            carre_ligne = (l // 3) * 3 + c // 3
            carre_colone = (l % 3) * 3 + c % 3

            if grille_principale[carre_ligne][carre_colone].get() in nombre_carre:
                messagebox.showerror("Erreur", "Il y a une erreur dans le carré({}, {}).".format(carre_ligne+1, carre_colone+1))
                return
            nombre_carre.add(grille_principale[carre_ligne][carre_colone].get())

    messagebox.showinfo("Juste", "La grille de Sudoku est correcte !")


# Création du bouton de vérification

check_button = tk.Button(fenetre, text="Go", command=verifie_grille)
check_button.grid(row=9, column=4)

 
# Création de la zone de texte pour entrer le chiffre

aide_entry = tk.Entry(fenetre, width=4)
aide_entry.grid(row=9, column=0)

 
# Fonction pour afficher les cases contenant un chiffre donné

def aide_chiffre(chiffre):

    # Parcourir chaque case de la grille

    for row in range(9):

        for column in range(9):

            cell = grille_principale[row][column]
            value = cell.get()

            # Si la valeur de la case est égale au chiffre entré
            if value == chiffre:
                
                # Changer la couleur de fond de la case
                cell.configure(bg="turquoise")

    # Si aucune case ne contient le chiffre entré

    if all(cell["bg"] != "turquoise" for row in grille_principale for cell in row):

        messagebox.showerror("Erreur", "Aucune case ne contient ce chiffre.")

 
# Création du bouton d'aide

aide_bouton = tk.Button(fenetre, text="Aide", command=lambda: aide_chiffre(aide_entry.get()))
aide_bouton.grid(row=9, column=1)
#Le lambda est utilisé pour créer une fonction anonyme 
#qui prendra en paramètre la valeur entrée dans aide_entry.get et la passera à la fonction aide_chiffre lorsque le bouton est cliqué.
 
# Affichage de la fenêtre
fenetre.mainloop()
