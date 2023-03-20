# Projet_python
Lien github du Projet: https://github.com/uvsq22200855/Projet_python

L1 MIASHS TD01 de Lichah,Lawson,Hnaoui et Sweth


https://docs.python.org/fr/3/library/functions.html

import tkinter as tk:
bibliothèque d'interface graphique [des fenêtres, des widgets (boutons, zones de texte, cases à cocher, …), des évènements (clavier, souris, …) ]

from tkinter import messagebox: type de boîtes de dialogue les alertes

fenetre = tk.Tk(): fonction de la librairie tkinter Tk() créée la fenêtre racine

Syntaxe globale:
ma_variable = UnWidget(widget_parent, parametre="une_valeur")

Cell est  le nom choisi pour référencer le widget

Widget : c'est tout éléments qu'on rajoute dans la fenêtre

Entry est utilisé pour saisir un texte. Ce widget permet à l’utilisateur de saisir une ligne de texte.

tk.entry une méthode qui permet la saisie dans la fenêtre principale


#def cree_grille()

#Pour chaque case de la grille, une entrée est créée en utilisant la fonction tk.Entry().

#Chaque entrée est placée dans la fenêtre principale root à l'aide de la méthode grid().

#Les entrées sont stockées dans une liste row pour chaque ligne, qui est ensuite ajoutée à la liste grid pour former la grille complète.

#la grille est renvoyée en tant que liste de listes de widgets Entry.

#https://waytolearnx.com/2020/07/la-methode-grid-tkinter-python-3.html pour grid()

#https://www.tutorialspoint.com/python/tk_entry.htm pour tk.Entry
