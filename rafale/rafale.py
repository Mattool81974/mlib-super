#******************
#
# rafale.py
#
#******************
# Presentation :
#
# MLib Super is the last version of the Pytho, "MLib project".
# It is made in purpose to be used in the "Trophées NSI" project.
#
# Ce fichier contient le programme principal du projet NSI test de MLib Super : "Rafale".
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

# Bidouiller le programme pour obtenir la bonne librairie
import sys, os.path
path_to_add = os.path.abspath(os.path.join(__file__, os.pardir))
path_to_add = os.path.abspath(os.path.join(path_to_add, os.pardir))
sys.path.append(path_to_add)

from math import sqrt, pow
from rafale_fenetre import *

#******************
#
# Programme principal
#
#******************

fenetre = Rafale_Fenetre(400, 400)

while fenetre.continuer():
    fenetre.maj_evenements()

    fenetre.maj_rafale()

    fenetre.maj_rendu()