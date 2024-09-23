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

class Client:
    
    __caisse = 0

    # Retourne la caisse de la banque
    def afficher_caisse() -> None: print(Client.__caisse)

    # Constructeur de la classe client
    def __init__(self, nom_client: str, solde: float) -> None:
        # Création des attributs
        self.solde = solde
        self.nom_client = nom_client

    # Retourne le solde de la banque
    def afficher_solde(self) -> None: print(self.solde)

    # Dépose des thunes dans le solde de la banque
    def depot(self, valeur_deposee: float) -> None:
        self.solde += valeur_deposee

    # Retire des thunes dans le solde du client
    def retrait(self, valeur_retiree: float) -> None:
        if self.solde > valeur_retiree: valeur_retiree = self.solde
        self.solde -= valeur_retiree

    # Vire des thunes dans le solde de la banque
    def virement(self, client_viree, valeur_viree: float) -> None:
        if self.solde > valeur_viree: valeur_viree = self.solde
        self.retrait(valeur_viree)
        client_viree.depot(valeur_viree)

jean = Client("Jean", 1000)
lou = Client("Lou", 5000)
jean.depot(500)
jean.virement(lou, 2000)
lou.retrait(500)
lou.retrait(2000)

class Point :
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Cercle:

    __pi = 3.1415

    def __init__(self, a: float, b: float, r: float) -> None:
        self.a = a
        self.b = b
        self.r = r

    # Retourne le périmètre du cercle
    def perimetre(self) -> float: return self.r * 2 * Cercle.__pi

    # Retourne la surface du cercle
    def surface(self) -> float: return self.r * self.r * Cercle.__pi

    # Retourne si un point appartient à un cercle
    def test_appartenance(self, p: Point) -> float: return sqrt(pow(p.x - self.a, 2) + pow(p.y - self.b, 2)) <= self.r

#******************
#
# La classe "Voiture"
#
#******************

class Voiture :

    # Constructeur de "Voiture"
    def __init__(self, nom: str, modele: str, couleur: str) -> None:
        # Définition des attributs de base
        self.__couleur = couleur
        self.__modele = modele
        self.__nom = nom

    def __str__(self) -> str:
        return self.__nom

fenetre = Fenetre(500, 500)

texture = fenetre.charger_texture_chemin_acces("F15", "/home/matto/Images/arme.png")

titre = fenetre.nouvel_enfant("texte", "text", 0, 0, 500, 100)
titre.set_bordure_couleur((200, 0, 0))
titre.set_bordure_largeur_entier(2)
titre.set_couleur_arriere_plan((255, 0, 0))
titre.set_police_taille(100)
titre.set_texte("Leclerc")
titre.set_texte_alignement_horizontal(1)

v1 = Voiture("Leclerc", "SXXI", "Camouflage jungle")
print(v1)
print(id(v1))

while fenetre.continuer():
    fenetre.maj_evenements()

    fenetre.maj_rendu()