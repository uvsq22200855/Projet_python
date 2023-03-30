import tkinter as tk
from tkinter import messagebox
import random


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Sudoku1Shot")

def creation_grille_complete():
    base  = 3
    cote  = base*base

    # modèle de solution valable pour la ligne de base
    def grille_predefini(l,c): 
        return (base*(l%base)+l//base+c)%cote

    # choisir des valeurs aléatoire pour les lignes, les colonnes et les nombres
    def randint(s): 
        return random.sample(s,len(s))
    
    # Elle est utilisée pour générer les valeurs de ligne et de colonne pour chaque case de la grille.
    base_unique = range(base) 
    lignes  = [ j*base + l for j in randint(base_unique) for l in randint(base_unique) ] 
    colonnes  = [ j*base + c for j in randint(base_unique) for c in randint(base_unique) ]
    valeurs  = randint(range(1,base*base+1))

    # créer une grille de sudoku en utilisant un modèle de base aléatoire
    grille = [ [valeurs[grille_predefini(r,c)] for c in colonnes] for r in lignes ]
    return grille

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

    # Création de la grille de sudoku en ajoutant grille_principale a la fonction 
    grille_defini = creation_grille_complete()

    # retirer aléatoirement des chiffres de la grille complétée pour créer une grille de Sudoku résoluble
    for i in range(81):
        row = i // 9
        colonne = i % 9
        cellule = grid[row][colonne]
        
        if random.random() < 0.5:
            cellule.delete(0, tk.END)
        else:
            cellule.insert(0, str(grille_defini[row][colonne]))
            cellule.config(state="disabled")

    # retourné la grille 
    return grid

# Création de la grille de sudoku en ajoutant grille_principale a la fonction
grille_principale = cree_grille()

 
# Fonction pour vérifier la grille de sudoku

def verifie_grille():
    for l in range(9):
        for c in range(9):

            valeur = grille_principale[l][c].get()
            if valeur == "" or not valeur.isdigit() or int(valeur) < 1 or int(valeur) > 9:

                messagebox.showerror("Erreur", "Il y a une erreur dans la case ({}, {}).".format(l+1, c+1))   #vide ou valeur invalide
                return

    for l in range(9):

        nombre_ligne = set()    #trie dans l'ordre croissant une liste de chiffre et supprime les doublons
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
bouton_verif = tk.Button(fenetre, text="Go", command=verifie_grille)
bouton_verif.grid(row=9, column=4)

# Création de la zone de texte pour entrer le chiffre
bouton_aide = tk.Entry(fenetre, width=4)
bouton_aide.grid(row=9, column=0)

 
# Fonction pour afficher les cases contenant un chiffre donné
def aide_chiffre(chiffre):

    # Réinitialiser la couleur d'arrière-plan de toutes les cellules en blanc pour chaque chiffre saisi (peut être supprimée si nécessaire)
    for ligne in range(9):
        for colonne in range(9):
            grille_principale[ligne][colonne].configure(bg="white")

    # Parcourir chaque case de la grille
    for ligne in range(9):
        for colonne in range(9):

            cell = grille_principale[ligne][colonne]
            valeur = cell.get()

            # Si la valeur de la case est égale au chiffre entré
            if valeur == chiffre:

                # Changer la couleur de fond de la case
                cell.configure(bg="turquoise")

    # Si aucune case ne contient le chiffre entré mettre un message d'erreur
    if all(cell["bg"] != "turquoise" for row in grille_principale for cell in row):

        messagebox.showerror("Erreur", "Aucune case ne contient ce chiffre.")

 
# Création du bouton d'aide

aide_bouton = tk.Button(fenetre, text="Aide", command=lambda: aide_chiffre(bouton_aide.get()))
aide_bouton.grid(row=9, column=1)
#Le lambda est utilisé pour créer une fonction anonyme 
#qui prendra en paramètre la valeur entrée dans aide_entry.get et la passera à la fonction aide_chiffre lorsque le bouton est cliqué.
 
# Affichage de la fenêtre
fenetre.mainloop()