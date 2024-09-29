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

raycast = fenetre.nouvel_enfant("raycast", "raycast", 0, 0, 328, 328)
raycast.set_couleur_arriere_plan((0, 0, 255))
raycast.set_raycast_moteur(moteur_raycast)

moteur_raycast.camera().set_x(5)
moteur_raycast.camera().set_y(5)
moteur_raycast.camera().set_z(2)

while fenetre.continuer():
    fenetre.maj_evenements()

    if fenetre.touche_pressee("z"): moteur_raycast.camera().avancer(5.0 * fenetre.delta_time())
    if fenetre.touche_pressee("s"): moteur_raycast.camera().avancer(-5.0 * fenetre.delta_time())

    if fenetre.touche_pressee("fd"): moteur_raycast.camera().set_rotation_y(moteur_raycast.camera().rotation_y() - (3.1415) * fenetre.delta_time())
    if fenetre.touche_pressee("fg"): moteur_raycast.camera().set_rotation_y(moteur_raycast.camera().rotation_y() + (3.1415) * fenetre.delta_time())

    if fenetre.touche_pressee("espace"): moteur_raycast.camera().set_z(moteur_raycast.camera().z() + 5 * fenetre.delta_time())
    if fenetre.touche_pressee("shift"): moteur_raycast.camera().set_z(moteur_raycast.camera().z() - 5 * fenetre.delta_time())

    fenetre.maj_rendu()