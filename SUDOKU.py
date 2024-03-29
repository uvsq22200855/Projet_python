import tkinter as tk
from tkinter import messagebox
import random
from tkinter import *

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Sudoku1Shot")

Canvas_Width = 740                 # Cela permet de bien rendre la fenetre avec de bonne couleur et les boutons et fond bien visible 
Canvas_Height = 400

fenetre.geometry("740x400")  #permet de s'assurer que la fenêtre a la bonne taille pour le canevas.

Sudoku_Canvas = Canvas(fenetre,bg='#CCCCCC', width= Canvas_Width, height= Canvas_Height) #paramètre bg fixé à "#CCCCCC" pour un fond gris clair
Sudoku_Canvas.grid(column=0,row=0,columnspan=20,rowspan=20) #Le widget canvas est placé dans la fenêtre tkinter à l'aide de la méthode grid()


grille_principale = []
nb_erreurs=0
def recommencer_parti():
    global grille_principale, nb_erreurs, temps #signifie que toute modification apportée à cette variable à l'intérieur de la fonction est sauvegarder
    global nb_contraintes, essais_user, nb_cliques, essaie_possible, essaie_utilise #affectera la variable globale du même nom à l'extérieur de la fonction.

    temps_label.config(text="Temps: 00:00")     # mettre à jour le label pour afficher le temps à 0
    nb_erreurs_label.config(text="Erreurs: 0")
    nb_contraintes_label.config(text="Contraintes: 0")
    essais_restants_label.config(text="Essais restants: 5")
    nb_aleatoire_label.config(text="Essais: 5")
    afficher_erreurs_bouton.config(state='normal')
    aide_bouton.config(state='normal')
    essais_user=0
    essaie_utilise=0
    temps = 0
    nb_erreurs=0
    nb_cliques=0
    essaie_possible=0
    nb_contraintes=0

    for ligne in grille_principale:    #itère sur chaque ligne de la grille du puzzle.
        for cellule in ligne:          #itère sur chaque cellule de la ligne courante.
            #efface le contenu de la cellule courante.         
            cellule.delete(0, tk.END)
            #définit la police de caractères de la cellule à "Arial" et la taille de police à 10 points. 
            cellule.config(font=("Arial", 10))
            #définit l'état de la cellule courante à "normal", ce qui signifie que le joueur peut y entrer une valeur
            cellule.config(state="normal") 
    grille_principale = cree_grille()  #génère une nouvelle grille de puzzle et l'assigne à "grille_principale".

# Ajout d'un bouton pour redémarrer le jeu
restart_bouton = tk.Button(fenetre, text="Redémarrer", command=recommencer_parti)
restart_bouton.grid(row=3, column=12)


nb_cliques = 0
essais_user=0
def afficher_contraintes():
    global grille_principale, nb_contraintes, nb_cliques, essais_user
    nb_contraintes = 0
    nb_cliques += 1
    essais_user += 1

    if nb_cliques == 5:
        afficher_erreurs_bouton.config(state=tk.DISABLED) #Désactiver le bouton lorsque on appuis 5 fois dessus.
    
    # Vérification des contraintes dans chaque ligne
    for l in range(9):
        colonne = []
        # Vérification des contraintes dans chaque colonne
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
                    colonne.append(valeur)  #permet de mémoriser pour plus tard ou sont placer les doublons
        
        ligne = []

        for c in range(9):
            valeur = grille_principale[l][c].get()
            if valeur == "" or not valeur.isdigit() or int(valeur) < 1 or int(valeur) > 9:  # vérifie si l'utilisateur a saisie une valeur correct 
                grille_principale[l][c].config(bg="red")
                nb_contraintes+=1
            else:
                grille_principale[l][c].config(bg="white") #la couleur de fond de la cellule est fixée au blanc pour indiquer qu'elle respecte les contraintes.

            if valeur != "":
                # La valeur existe déjà dans cette ligne
                if valeur in ligne:

                    for i in range(9):
                        if grille_principale[l][i].get() == valeur:
                            grille_principale[l][i].config(bg="red")
                            nb_contraintes+=1
                else:
                    # Si la valeur ne figure pas dans la liste de lignes, elle l'ajoute à la liste pour vérification ultérieure.
                    ligne.append(valeur) # permet de vérifier si une valeur apparaît déjà dans la ligne et dc pas de doublons.
                                         
        # Vérification des contraintes dans chaque carré
        carre = []
        ligne = (l // 3) * 3 #En divisant l par 3 à l'aide de la division entière on obtient l'indice du carré 3x3 correspondant.
        colonne = (l % 3) * 3 # En multipliant cette valeur par 3, on obtient l'indice de la ligne de départ de ce carré.

        for l in range(ligne, ligne + 3):
            for c in range(colonne, colonne + 3):
                valeur = grille_principale[l][c].get()
                if valeur != "":   #la cellule n'est pas vide
                    # La valeur existe déjà dans ce carre
                    if valeur in carre:
                        
                        for i in range(ligne, ligne + 3):
                            for j in range(colonne, colonne + 3):
                                if grille_principale[i][j].get() == valeur:
                                    grille_principale[i][j].config(bg="red")
                                    nb_contraintes+=1
                    else:
                        carre.append(valeur)

    nb_contraintes_label.config(text=f"Contraintes: {nb_contraintes}") # mettre à jour le label pour afficher le nombre de containtes à chaque appel de la fonction.
    essais_restants = 5 - essais_user
    essais_restants_label.config(text="Essais restants: {}".format(essais_restants))

# Création d'un bouton pour afficher les contraintes
afficher_erreurs_bouton = tk.Button(fenetre, text="Afficher les contraintes", command=afficher_contraintes)
afficher_erreurs_bouton.grid(row=8, column=12)

nb_contraintes_label = tk.Label(fenetre, text="Contraintes: 0")
nb_contraintes_label.grid(row=9, column=12)

essais_restants_label = tk.Label(fenetre, text="Essais restants: 5")
essais_restants_label.grid(row=6, column=12)


# Fonction pour mettre à jour le temps toutes les secondes
temps=0 # Ajout de la variable temps à zéro
def timer_maj():
    global temps
    temps += 1
    # les minutes obtenues par la division entière par 60 et les secondes étant le reste divisée par 60.
    temps_label.config(text="Temps: {:02d}:{:02d}".format(temps // 60, temps % 60))
    # planifie l'appel de la fonction timer_maj() toutes les secondes
    fenetre.after(1000, timer_maj)

# Lancer la fonction pour mettre à jour le temps toutes les secondes, garantit que c'est mise à jour toutes les secondes pour afficher le temps écoulé.
fenetre.after(1000, timer_maj)

# Ajout d'un label pour afficher le temps
temps_label = tk.Label(fenetre, text="Temps: 00:00")
temps_label.grid(row=0, column=12)


def creation_grille_aleatoire():
    base  = 3
    cote  = base*base

    # modèle de solution valable pour la ligne de base
    def grille_predefini(l,c): 
        return (base*(l%base)+l//base+c)%cote   # calcule l'indice d'une cellule en fonction de ses indices de ligne et de colonne.

    # choisir des valeurs aléatoire pour les lignes, les colonnes et les nombres
    def randint(s): 
        return random.sample(s,len(s)) # utilisée pour mélanger les indices de ligne et de colonne et les valeurs possibles des cellules par la suite.
    
    # Elle est utilisée pour générer les valeurs de ligne et de colonne pour chaque case de la grille.
    base_unique = range(base) 
    lignes  = [ j*base + l for j in randint(base_unique) for l in randint(base_unique) ] 
    colonnes  = [ j*base + c for j in randint(base_unique) for c in randint(base_unique) ]
    valeurs  = randint(range(1,base*base+1)) #  représente les valeurs possibles qui peuvent être remplies dans chaque cellule de la grille.

    # créer une grille de sudoku en utilisant un modèle de base aléatoire
    grille = [ [valeurs[grille_predefini(r,c)] for c in colonnes] for r in lignes ]
    return grille


# Fonction pour créer la grille de sudoku
def cree_grille():
    # Création d'une grille de 9x9 cases (celle de base dans le jeu sudoku)
    grille_cree = []
    # crée une liste de listes, où chaque liste représente une ligne de la grille et contient des widgets Entry individuels pour chaque cellule de la ligne.
    for ligne in range(9):
        # Créer une nouvelle ligne pour la grille
        ligne_cree = []

        for colonne in range(9):
            # Créer un nouveau compartiment pour la grille, pour chaque case de la grille, une entrée est créée
            compartiment = tk.Entry(fenetre, justify="center", width=6, font=("Arial", 10))

            # Calculer l'indice de la région  correspondant à la case
            region_ligne = ligne // 3
            region_colonne = colonne // 3
            region_ligne2 = ligne // 6
            region_colonne2 = colonne // 6
            region_ligne3 = ligne // 9
            region_colonne3 = colonne // 9

            # Le positionner dans la grille en fonction de son indice de région
            compartiment.grid(row=ligne + region_ligne + region_ligne2 + region_ligne3, column=colonne+region_colonne + region_colonne2 + region_colonne3, padx=4, pady=4)
            #Les entrées sont stockées dans une liste row pour chaque ligne, qui est ensuite ajoutée à la liste grid pour former la grille complète.
            
            # Ajouter la case à la ligne
            ligne_cree.append(compartiment)

        # Ajouter la ligne à la grille , la grille entière est construite ligne par ligne, chaque nouvelle ligne étant ajoutée à la liste grille_cree.
        grille_cree.append(ligne_cree)

    # Création de la grille de sudoku en ajoutant grille_principale a la fonction 
    grille_defini = creation_grille_aleatoire()

    # retirer aléatoirement des chiffres de la grille complétée pour créer une grille de Sudoku résoluble
    for i in range(81):
        # calculer les indices de colonne et de ligne pour chaque cellule de la grille en fonction de l'indice i
        colonne = i % 9 
        ligne = i // 9  # obtient la cellule correspondante dans la liste grille_cree à l'aide de ces indices.
        cellule = grille_cree[colonne][ligne]
        
        if random.random() < 0.4: 
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

        nombre_ligne = set()    #utilisé pour stocker les chiffres uniques trouvés dans une ligne particulière de la grille de Sudoku.
        nombre_colone = set()   #La fonction itère sur chaque cellule de la ligne et ajoute la valeur de chaque cellule à l'ensemble nombre colone...
        nombre_carre = set()    #trie dans l'ordre croissant une liste de chiffre et supprime les doublons

        for c in range(9):
            # Vérifier la colonne c

            if grille_principale[c][l].get() in nombre_colone:
                messagebox.showerror("Erreur", "Il y a une erreur dans la colonne {}.".format(l+1))
                nb_erreurs += 1
                
                # Mise à jour du nombre d'erreurs
                nb_erreurs_label.config(text="Erreurs: {}".format(nb_erreurs))
                return
            nombre_colone.add(grille_principale[c][l].get()) #ajoute la valeur de la cellule de la grille à "nombre_colone"

             # Vérifier la ligne l

            if grille_principale[l][c].get() in nombre_ligne:
                messagebox.showerror("Erreur", "Il y a une erreur dans la ligne {}.".format(l+1))
                nb_erreurs += 1
                
                # Mise à jour du nombre d'erreurs
                nb_erreurs_label.config(text="Erreurs: {}".format(nb_erreurs))
                return
            nombre_ligne.add(grille_principale[l][c].get())

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
            
 
    messagebox.showinfo("Tu as terminé en", "Temps: {:02d}:{:02d}".format(temps // 60, temps % 60))
    messagebox.showinfo("Erreurs", "Tu as fait {} erreur(s) durant cette parti.".format(nb_erreurs))
    messagebox.showinfo("Bien joué", "La grille de Sudoku est correcte !")

# Création du bouton de vérification
bouton_verif = tk.Button(fenetre, text="Vérifier", command=verifie_grille)
bouton_verif.grid(row=12, column=5)

nb_erreurs_label = tk.Label(fenetre, text="Erreurs: 0")
nb_erreurs_label.grid(row=13, column=5)


def couleur_de_base():
    global grille_principale
    for l in range(9):
        for c in range(9):
            grille_principale[l][c].config(bg="white")

base_couleur_bouton = tk.Button(fenetre, text="Rénitialiser les couleurs", command=couleur_de_base)
base_couleur_bouton.grid(row=11, column=12)


def quitter_partie():
    if messagebox.askyesno("J'arrete", "Veux-tu réelement quitter la parti ?"):      #Demander une question
        fenetre.destroy() # détruit la fenêtre principale de l'application et quitte le programme.

quitter_bouton = tk.Button(fenetre, text="Quitter", command=quitter_partie)
quitter_bouton.grid(row=12, column=7)

'''
def indice_aleatoire():
    global grille_principale

    # Choisir une cellule vide aléatoirement
    #crée une compréhension de liste qui parcourt toutes les cellules de la grille et ajoute les valeurs de toutes les cellules vides à la liste cellules_vides.
    cellules_vides = [(l, c) for l in range(9) for c in range(9) if grille_principale[l][c].get() == ""]

    if cellules_vides:
        ligne, colonne = random.choice(cellules_vides)
        # Insérer une valeur aléatoire entre 1 et 9
        valeur = random.randint(1, 9)
        grille_principale[ligne][colonne].insert(0, valeur)
        
    else:
        messagebox.showerror("Erreur", "Il n'y a plus de cases vides!")

indice_bouton = tk.Button(fenetre, text="Indices\npiégers", command=indice_aleatoire)
indice_bouton.grid(row=12, column=3)
'''

essaie_possible=0
essaie_utilise=0
def indice_juste():
    global grille_principale, essaie_possible, essaie_utilise
    essaie_possible+=1
    essaie_utilise+=1
    if essaie_possible == 5:
        aide_bouton.config(state=tk.DISABLED)

    # Trouver une cellule vide aléatoirement
    i = random.randint(0, 8)   #génèrent des indices aléatoires (i et j) jusqu'à ce qu'une cellule vide soit trouvée dans la grille_principale.
    j = random.randint(0, 8)
    while grille_principale[i][j].get() != "":
        i = random.randint(0, 8)

    # Trouver une valeur valide pour la cellule
    valeurs_correct = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for l in range(9):
        if grille_principale[l][j].get() in valeurs_correct:
            valeurs_correct.remove(grille_principale[l][j].get()) #indice l est utilisé pour sélectionner la ligne, et j pour la colonne.
        if grille_principale[i][l].get() in valeurs_correct:
            valeurs_correct.remove(grille_principale[i][l].get()) #grille_principale est une liste bidimensionnelle valide avec au moins l lignes et j colonne
            
    # Remplir la cellule avec la valeur choisie aléatoirement
    if valeurs_correct:
        valeur = random.choice(valeurs_correct)
        grille_principale[i][j].insert(0, valeur)

    nb_aleatoire = 5 - essaie_utilise
    nb_aleatoire_label.config(text="Essais: {}".format(nb_aleatoire))

# Ajout d'un bouton pour obtenir de l'aide
aide_bouton = tk.Button(fenetre, text="Valeurs", command=indice_juste)
aide_bouton.grid(row=12, column=3)

nb_aleatoire_label = tk.Label(fenetre, text="Essais: 5") 
nb_aleatoire_label.grid(row=13, column=3)


# Affichage de la fenêtre
fenetre.mainloop()