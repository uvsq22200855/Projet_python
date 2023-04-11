import tkinter as tk
from tkinter import messagebox
import random

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Sudoku1Shot")

# Ajout d'un label pour afficher le temps
temps_label = tk.Label(fenetre, text="Temps: 00:00")
temps_label.grid(row=3, column=10)

# Ajout d'un label pour afficher le nombre d'erreurs
nb_erreurs_label = tk.Label(fenetre, text="Erreurs: 0")
nb_erreurs_label.grid(row=9, column=8)

# Ajout d'un label pour afficher le nombre de contraintes
nb_contraintes_label = tk.Label(fenetre, text="Contraintes: 0")
nb_contraintes_label.grid(row=10, column=10)


grille_principale = []
nb_erreurs=0
def recommencer_parti():
    global grille_principale #signifie que toute modification apportée à cette variable à l'intérieur de la fonction
    global nb_erreurs           #affectera la variable globale du même nom à l'extérieur de la fonction.
    global temps

    temps = 0
    nb_erreurs=0
    temps_label.config(text="Temps: 00:00")     # mettre à jour le label pour afficher le temps à 0
    nb_erreurs_label.config(text="Erreurs: 0")  # mettre à jour le label pour afficher le nombre d'erreurs à 0

    for ligne in grille_principale:    #itère sur chaque ligne de la grille du puzzle.
        for cellule in ligne:          #itère sur chaque cellule de la ligne courante.
            #efface le contenu de la cellule courante.         
            cellule.delete(0, tk.END)
            #définit l'état de la cellule courante à "normal", ce qui signifie que le joueur peut y entrer une valeur
            cellule.config(state="normal") 
    grille_principale = cree_grille()  #génère une nouvelle grille de puzzle et l'assigne à "grille_principale".

# Ajout d'un bouton pour redémarrer le jeu
restart_bouton = tk.Button(fenetre, text="Redémarrer", command=recommencer_parti)
restart_bouton.grid(row=2, column=10)

nb_contraintes=0
nombre_cliques = 0
def afficher_contraintes():
    global grille_principale
    global nb_contraintes
    global nombre_cliques
    nb_contraintes = 0
    nombre_cliques += 1
    if nombre_cliques == 5:
        afficher_erreurs_bouton.config(state=tk.DISABLED) #Désactiver le bouton lorsque on appuis 5 fois dessus.
    
    # Vérification des contraintes dans chaque ligne
    for l in range(9):
        ligne = []

        for c in range(9):
            valeur = grille_principale[l][c].get()
            if valeur == "" or not valeur.isdigit() or int(valeur) < 1 or int(valeur) > 9:  # vérifie si l'utilisateur a saisie une valeur
                grille_principale[l][c].config(bg="red")
                nb_contraintes+=1
            else:
                grille_principale[l][c].config(bg="white") #la couleur de fond de la cellule est fixée au blanc pour indiquer qu'elle respecte les contraintes.

            if valeur != "":
                # La valeur existe déjà dans cette colonne
                if valeur in ligne:

                    for i in range(9):
                        if grille_principale[l][i].get() == valeur:
                            grille_principale[l][i].config(bg="red")
                            nb_contraintes+=1
                else:
                    # Si la valeur ne figure pas dans la liste de lignes, elle l'ajoute à la liste pour vérification ultérieure.
                    ligne.append(valeur) # permet de vérifier si une valeur apparaît déjà dans la ligne et dc pas de doublons.
                                         
        # Vérification des contraintes dans chaque colonne
        colonne = []

        for c in range(9):
            valeur = grille_principale[c][l].get()
            if valeur != "":
                # La valeur existe déjà dans cette colonne
                if valeur in colonne:

                    for i in range(9):
                        if grille_principale[i][l].get() == valeur:
                            grille_principale[i][l].config(bg="red")
                            nb_contraintes+=1
                else:
                    colonne.append(valeur)
                    
        # Vérification des contraintes dans chaque carré
        carre = []
        ligne = (l // 3) * 3
        colonne = (l % 3) * 3

        for r in range(ligne, ligne + 3):
            for c in range(colonne, colonne + 3):
                valeur = grille_principale[r][c].get()
                if valeur != "":
                    # La valeur existe déjà dans cette colonne
                    if valeur in carre:
                        
                        for i in range(ligne, ligne + 3):
                            for j in range(colonne, colonne + 3):
                                if grille_principale[i][j].get() == valeur:
                                    grille_principale[i][j].config(bg="red")
                                    nb_contraintes+=1
                    else:
                        carre.append(valeur)

    nb_contraintes_label.config(text=f"Contraintes: {nb_contraintes}") # mettre à jour le label pour afficher le nombre de containtes à chaque appel de la fonction.

# Création d'un bouton pour afficher les contraintes
afficher_erreurs_bouton = tk.Button(fenetre, text="Afficher les erreurs", command=afficher_contraintes)
afficher_erreurs_bouton.grid(row=5, column=10)

# Fonction pour mettre à jour le temps toutes les secondes
temps=0 # Ajout de la variable temps à zéro
def timer_maj():
    global temps
    temps += 1
    temps_label.config(text="Temps: {:02d}:{:02d}".format(temps // 60, temps % 60))
    fenetre.after(1000, timer_maj)

# Lancer la fonction pour mettre à jour le temps toutes les secondes
fenetre.after(1000, timer_maj)


def creation_grille_aleatoire():
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
    grille_cree = []

    for ligne in range(9):
        # Créer une nouvelle ligne pour la grille
        ligne_cree = []

        for colonne in range(9):
            # Créer un nouveau compartiment pour la grille
            compartiment = tk.Entry(fenetre, width=6)

            # le positioner dans la grille
            compartiment.grid(row=ligne, column=colonne)

            # Ajouter la case à la ligne
            ligne_cree.append(compartiment)

        # Ajouter la ligne à la grille
        grille_cree.append(ligne_cree)

    # Création de la grille de sudoku en ajoutant grille_principale a la fonction 
    grille_defini = creation_grille_aleatoire()

    # retirer aléatoirement des chiffres de la grille complétée pour créer une grille de Sudoku résoluble
    for i in range(81):
        ligne = i // 9
        colonne = i % 9
        cellule = grille_cree[ligne][colonne]
        
        if random.random() < 0.5:
            # supprimer des nombres sélectionnés au hasard dans une grille de Sudoku complétée afin de créer une grille résoluble.
            cellule.delete(0, tk.END) # supprimer le contenu de la cellule, en commençant par l'index 0 jusqu'à tk.END
        else:  
            #utilisée pour insérer une valeur dans un widget Tkinter, utilisée pour insérer un nombre dans la cellule, à partir de l'index 0.                       
            cellule.insert(0, str(grille_defini[ligne][colonne])) 
            #définir l'option state du widget cellule sur "disabled", ce qui empêche l'utilisateur de modifier la valeur de la cellule.
            cellule.config(state="disabled")

    # retourné la grille 
    return grille_cree

# Création de la grille de sudoku en ajoutant grille_principale a la fonction
grille_principale = cree_grille()


# Fonction pour vérifier la grille de sudoku
def verifie_grille():
    global nb_erreurs
    
    for l in range(9):
        for c in range(9):
            
            valeur = grille_principale[l][c].get()
            if valeur == "" or not valeur.isdigit() or int(valeur) < 1 or int(valeur) > 9:
                messagebox.showerror("Erreur", "Il manque une valeur dans la case ou elle ne respecte pas les contrainte du jeu ({}, {}).".format(l+1, c+1))   #vide ou valeur invalide
                nb_erreurs += 1
                
                # Mise à jour du nombre d'erreurs
                nb_erreurs_label.config(text="Erreurs: {}".format(nb_erreurs))
                return

    for l in range(9):

        nombre_ligne = set()    #trie dans l'ordre croissant une liste de chiffre et supprime les doublons
        nombre_colone = set()
        nombre_carre = set()

        for c in range(9):
            # Vérifier la ligne l

            if grille_principale[l][c].get() in nombre_ligne:
                messagebox.showerror("Erreur", "Il y a une erreur dans la ligne {}.".format(l+1))
                nb_erreurs += 1
                
                # Mise à jour du nombre d'erreurs
                nb_erreurs_label.config(text="Erreurs: {}".format(nb_erreurs))
                return
            nombre_ligne.add(grille_principale[l][c].get())

            # Vérifier la colonne c

            if grille_principale[c][l].get() in nombre_colone:
                messagebox.showerror("Erreur", "Il y a une erreur dans la colonne {}.".format(l+1))
                nb_erreurs += 1
                
                # Mise à jour du nombre d'erreurs
                nb_erreurs_label.config(text="Erreurs: {}".format(nb_erreurs))
                return
            nombre_colone.add(grille_principale[c][l].get())

            # Vérifier le carre 3x3 (l // 3, l % 3)
            carre_ligne = (l // 3) * 3 + c // 3
            carre_colone = (l % 3) * 3 + c % 3

            if grille_principale[carre_ligne][carre_colone].get() in nombre_carre:
                messagebox.showerror("Erreur", "Il y a une erreur dans le carre ({}, {}).".format(l // 3 + 1, l % 3 + 1))
                nb_erreurs += 1
                
                # Mise à jour du nombre d'erreurs
                nb_erreurs_label.config(text="Erreurs: {}".format(nb_erreurs))
                return
            nombre_carre.add(grille_principale[carre_ligne][carre_colone].get())
            
 
    messagebox.showinfo("Erreurs", "Tu as fait {} erreur(s) durant cette parti.".format(nb_erreurs))
    messagebox.showinfo("Tu as terminé en seulement", "Temps: {:02d}:{:02d}".format(temps // 60, temps % 60))
    messagebox.showinfo("Bien joué", "La grille de Sudoku est correcte !")

# Création du bouton de vérification
bouton_verif = tk.Button(fenetre, text="Vérification", command=verifie_grille)
bouton_verif.grid(row=9, column=3)


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


def quitter_partie():
    if messagebox.askyesno("J'en ai marre", "Tu es un looser ouuuuu ?"):      #Demander une question
        fenetre.destroy() # détruit la fenêtre principale de l'application et quitte le programme.

quitter_bouton = tk.Button(fenetre, text="J'en ai marre", command=quitter_partie)
quitter_bouton.grid(row=9, column=5)


# Affichage de la fenêtre
fenetre.mainloop()