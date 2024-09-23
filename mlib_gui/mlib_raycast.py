#******************
#
# mlib_raycast.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient le nécessaire à l'utilisation du Raycast dans la GUI.
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

# Importer pygame pour utiliser Pygame
import pygame
# Importer la base des GUIs avec MLib
from mlib_objet import *
# Importer la base du Raycast avec MLib
from raycast.mlib_raycast_moteur import *

#******************
#
# La classe "Raycast_Fenetre"
#
#******************

class Raycast_Fenetre(Objet):
    """Classe représentant une fenêtre graphique de Raycast"""

    # Constructeur de Raycast_Fenetre
    def __init__(self, structure_plus: Structure_Plus, nom: str, x: int = 0, y: int = 0, largeur: int = 0, hauteur: int = 0) -> None:
        """ Constructeur de Raycast_Fenetre

        Arguments:
            structure_plus (Structure_Plus): structure plus dans le software
            nom (str): nom de l'objet
            x (int, optional): Position X de l'objet. Defaults to 0.
            y (int, optional): Position Y de l'objet. Defaults to 0.
            largeur (int, optional): Largeur de l'objet. Defaults to 0.
            hauteur (int, optional): Hauteur de l'objet. Defaults to 0.
        """
        super().__init__(structure_plus, nom, x, y, largeur, hauteur)

        # Définition des attributs
        self.__raycast_moteur = 0

    # Applique le rendu du raycast sur la texture
    def rendu(self, surface_objet: pygame.Surface) -> None:
        """Applique le rendu du raycast sur la texture

        Args:
            surface_objet (pygame.Surface): Surface de l'objet
        """
        if self.arriere_plan_texture() != "": self.set_arriere_plan_texture_par_nom("")
        super().rendu(surface_objet)

        # Applique le rendu 2D
        surface_actuelle = self.raycast_moteur().rendu_2d()
        surface_actuelle = pygame.transform.scale(surface_actuelle, (surface_objet.get_width(), surface_objet.get_height()))
        surface_objet.blit(surface_actuelle, (0, 0, surface_objet.get_width(), surface_objet.get_height()))

    # Getters et setters
    def raycast_moteur(self) -> Raycast_Moteur:
        """Retourne le moteur de raycast utilisé

        Retour:
            Raycast_Moteur: moteur de raycast utilisé
        """
        return self.__raycast_moteur
    def set_raycast_moteur(self, moteur: Raycast_Moteur) -> None:
        """Change le moteur de raycast utilisé

        Args:
            moteur (Raycast_Moteur): nouveau moteur de raycast utilisé
        """
        self.__raycast_moteur = moteur