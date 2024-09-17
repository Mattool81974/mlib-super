#******************
#
# mlib_window.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient la classe "Fenetre", et tout le nécessaire pour l'utiliser.
#
#******************
#
# License (GPL V3.0) :
#
# Copyright (C) 2024 par Mattéo.
# This file is part of MLib Super.
# MLib Super is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# MLib Super is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with MLib Super. If not, see <https:#www.gnu.org/licenses/>.
#

# Importer MLib_Objet pour utiliser les objets MLib
from mlib_objet import *

#******************
#
# La classe "Fenetre"
#
#******************

class Fenetre :
    """Classe représentant une fenêtre MLib"""
    
    def __init__(self, largeur: int, hauteur: int) -> None:
        """Constructeur de "Fenetre"

        Arguments:
            largeur (int): Largeur de la fenêtre
            hauteur (int): Hauteur de la fenêtre
        """

        # Définition des attributs de base
        self.__continue = True
        self.__couleur_arriere_plan = (255, 255, 255)
        self.__hauteur = hauteur
        self.__ecran = 0
        self.__enfants = []
        self.__evenements = 0
        self.__largeur = largeur

        # Mise en place de Pygame
        pygame.init()
        self.__ecran = pygame.display.set_mode((largeur, hauteur))

    def __del__(self) -> None:
        """Destructeur de "Fenetre"""
        self.__enfants.clear()

    def maj_evenements(self) -> None :
        """Fonction exécutée avant chaque mise à jour de la fenêtre, pour gérer les évènements"""

        # On navigue dans chaques évènements
        self.__evenements = pygame.event.get()
        for evenement in self.__evenements:
            if evenement.type == pygame.QUIT:
                # On repère l'évènement pour quitter le programme
                self.__continue = False

        # Appliquer les évènements graphiques de base
        self.__ecran.fill(self.__couleur_arriere_plan)

    def maj_rendu(self) -> None:
        """Fonction exécutée pour mettre la fenêtre graphique à jour"""

        # Ajoute chaque enfants sur la surface
        for enfant in self.__enfants:
            enfant.maj_rendu(self.__ecran)

        # On affiche l'écran
        pygame.display.flip()

    def __nouvel_enfant_creer(self, nom: str, type: str) -> Objet:
        """Crée l'enfant, avec le type nécessaire selon "type

        Args:
            nom (str): Nom de l'enfant
            type (str): Type de l'enfant

        Returns:
            Objet: Enfant crée
        """

        # Création d'un texte
        if type == "text" or type == "texte": return Texte(nom)

        # Création avec le type de base
        return Objet(nom)

    def nouvel_enfant(self, nom: str, type: str, x: int, y: int, largeur: int, hauteur: int) -> Objet:
        """Crée et retourne un nouvel enfant dans la fenêtre

        Arguments:
            nom (str): Nom du nouvel enfant
            x (int): Position X du nouvel enfant
            y (int): Position Y du nouvel enfant
            largeur (int): Largeur du nouvel enfant
            hauteur (int): Hauteur du nouvel enfant

        Retour:
            Objet: Objet crée
        """

        # Création de l'enfant
        nouvel_objet = self.__nouvel_enfant_creer(nom, type)
        nouvel_objet.set_hauteur(hauteur)
        nouvel_objet.set_largeur(largeur)
        nouvel_objet.set_x(x)
        nouvel_objet.set_y(y)
        self.__enfants.append(nouvel_objet)

        return nouvel_objet

    # Getters et setters
    def continuer(self) -> bool:
        """Retourne si la classe continue de marcher"""
        return self.__continue