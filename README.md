
# SUDOKU Projet_python 

Le Sudoku est un jeu dans lequel le joueur joue sur une grille de 9 x 9 et chaque rangée, colonne et carré doit être rempli avec les numéros 1 a 9, sans répéter aucun nombre dans la rangée, la colonne ou le carré. Le but du jeu présenté est de le réalisé du premier coup par le joueur le plus rapidement possible et avec le moins d'aide. C'est une variante ou le joueur doit remplir toute les cases avant d'appuiyer sur le bouton "vérifier" sinon cela indiquera qu'une case st vide.


## 🚀 Auteur

Lien github du Projet: https://github.com/uvsq22200855/Projet_python

[Lien vers le code du Sudoku](https://github.com/uvsq22200855/Projet_python/blob/main/SUDOKU.py)

L1 MIASHS TD01 de Lichah,Lawson,Hnaoui et Saravanan


## 🔗 Lien et aide

- [Site de documentation général](https://docs.python.org/fr/3/library/functions.html)

- [Messagebox.showerror](https://docs.python.org/3/library/tkinter.messagebox.html)

- [Pour le set()](https://www.geeksforgeeks.org/python-set-method/)

- [Pour le .after()](https://www.geeksforgeeks.org/python-after-method-in-tkinter/)

- [Pour le .config()](https://coderslegacy.com/python/tkinter-config/)

- [Pour le .label()](https://www.tresfacile.net/le-widget-label-tkinter/)

- [Pour tk.Entry()](https://www.tutorialspoint.com/python/tk_entry.htm)

- [Pour grid()](https://waytolearnx.com/2020/07/la-methode-grid-tkinter-python-3.html) et plein d'autre information

- [lien avec beaucoup d'informartion (notamment bouton)](http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html) 


Youtube, le web, chatgpt et autre...

A noter que la fonction creation_grille_aleatoire a été prise sur internet du a la complicité de sa tache.

Pour le .format: le temps écoulé en minutes et en secondes à l'aide de la méthode format(). Le {:02d} est un spécificateur de format qui garantit que le nombre affiché comporte au moins deux chiffres et que des zéros sont ajoutés si nécessaire.
## Information utile

Cell est  le nom choisi pour référencer le widget.
Widget : c'est tout éléments qu'on rajoute dans la fenêtre

Entry est utilisé pour saisir un texte. Ce widget permet à l’utilisateur de saisir une ligne de texte. 

#### Fonction aléatoire: 

La variable lignes est définie comme une liste de compréhension qui génère tous les indices de ligne possibles pour les cellules de la grille. Pour ce faire, elle itère sur chaque indice de sous-grille (j), mélange les indices de ligne au sein de cette sous-grille, puis concatène les indices mélangés pour toutes les sous-grilles. Cela garantit que chaque ligne contient exactement une cellule de chaque sous-grille et que les cellules de chaque sous-grille sont ordonnées de manière aléatoire.

0,5 est le seuil de probabilité utilisé pour déterminer si une cellule de la grille de Sudoku doit être supprimée ou non, sur la base d'une valeur aléatoire générée par random.random().



## 🛠 Utilité général de chaque fonction

### def recommencer_parti

- Cette fonction réinitialise un certain nombre de variables globales à leurs valeurs initiales, et met à jour certaines étiquettes dans l'interface et recrée une grille aléatoire.

### def afficher_contrainte

- Cette fonction verifie dans chaque carré,colonne et ligne si une valeur ne respecte pas les contraintes du Sudoku, si ce n'est pas le cas elle l'affiche en rouge avec un sytème de conteur pour plusieur utilié différentes.

### def timer_maj 

- Fonction pour afficher un timeur donnée après l'écoulement d'un laps de temps spécifié (en millisecondes).

### def creation_grille_aleatoire 

- Cette fonction est utilisé pour générer une grille aléatoire en définissant une taille de base de 3 et en créant une solution modèle pour la ligne de base à l'aide d'une formule spécifique. Il choisit ensuite au hasard des valeurs pour les lignes, les colonnes et les nombres.
**Cette fonction a été prise sur internet**

### def cree_grille 

- Cette fonction cree la grille de Sudoku séparer 3x3 et en y ajoutant des valeurs aléatoire.

### def verifie_grille 

- Cette fonction vérifié si la grille respecte les contraintes du Sudoku en passant par les carre,colonne et ligne en les triants. Elle compte le nombre d'erreur également.

### def couleur_de_base

- Cette fonction met toute les case en blanc pour avoir une meilleur visibilité de jeu.

### def quitter_partie :

- Cette fonction permet de fermer la fenetre de jeu a l'aide d'une question poser a l'utilisateur.

### def indice_aleatoire 

- Cette fonction verifie sur une case est vide et sélectionne aléatoirement une cellule vide et insère une valeur aléatoire entre 1 et 9.

### def indice_juste 

- Globalement, cette fonction remplit les cellules vides d'une grille de Sudoku de manière aléatoire tout en s'assurant que les valeurs sont correctes et n'enfreignent aucune règle de Sudoku.


## 🤔 Modifier la difficulté de la grille 

#### Modifier la valeur (ci dessous). Plus la valeur est élévé plus la grille est compliqué à résoudre.


| Fonction| Ligne     | Description                |         
| :-------- | :------- | :------------------------- | 
| `cree_grille` | `228` | random.random <**valeur** | 


## 👩‍💻 Jouer au Sudoku

Vous pouver maintenant jouer a notre Sudoku comme vous le souhaiter. Amuser vous bien. 

- [Si vous etes bloquer vous avez qu'a a aller sur ce cite 🧠 :)](https://www.top-sudoku.com/sudoku/fr/rentrer-un-enonce-sudoku.php)
