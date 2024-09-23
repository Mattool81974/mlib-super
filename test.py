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

fenetre = Fenetre(630, 328)

moteur_raycast = fenetre.nouveau_raycast()

mur = moteur_raycast.nouveau_materiel(1)
mur.set_couleur_2d((255, 0, 0))

moteur_raycast.generer_map_depuis_texte_chemin_acces("assets/map.txt")

rafale = moteur_raycast.nouvel_objet_dynamique("rafale")
rafale.set_materiel_par_id(1)

raycast = fenetre.nouvel_enfant("raycast", "raycast", 0, 0, 500, 328)
raycast.set_couleur_arriere_plan((0, 0, 255))
raycast.set_raycast_moteur(moteur_raycast)

while fenetre.continuer():
    fenetre.maj_evenements()

    if fenetre.touche_pressee("d"): rafale.set_x(rafale.x() + 5.0 * fenetre.delta_time())
    if fenetre.touche_pressee("q"): rafale.set_x(rafale.x() - 5.0 * fenetre.delta_time())
    if fenetre.touche_pressee("s"): rafale.set_y(rafale.y() + 5.0 * 500.0/328.0 * fenetre.delta_time())
    if fenetre.touche_pressee("z"): rafale.set_y(rafale.y() - 5.0 * 500.0/328.0 * fenetre.delta_time())

    fenetre.maj_rendu()