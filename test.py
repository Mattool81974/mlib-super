#******************
#
# test.py
#
#******************
# Presentation :
#
# MLib Super is the last version of the Pytho, "MLib project".
# It is made in purpose to be used in the "Trophées NSI" project.
#
# This file is made to test the MLib Super library.
#
#******************
#
# License (GPL V3.0) :
#
# Copyright (C) 2024 by Mattéo
# This file is part of MLib Super.
# MLib Super is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# MLib Super is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with MLib Super. If not, see <https:#www.gnu.org/licenses/>.
#

from math import sqrt, pow
from mlib import *

#******************
#
# Programme principal
#
#******************

fenetre = Fenetre(500, 500)

# Stockage des données
attributs_tanks = ["Nom", "Pays", "Création"]
tanks = [["Leclerc", "France", 1991],
           ["M1A2 Abrams", "USA", 1992]]
# Création de la base de données
bdd = Base_De_Donnees("tanks.db")
bdd.creer_table("Sandwich", (("Nom_Sandwich", "str"), ("Prix", "float")))

# Création d'un titre principal
titre = fenetre.nouvel_enfant("titre_principal", "text", 0, 0, fenetre.largeur(), fenetre.hauteur() / 7.0)
titre.set_police_taille(50)
titre.set_texte("Base de données")

while fenetre.continuer():
    fenetre.maj_evenements()

    

    fenetre.maj_rendu()