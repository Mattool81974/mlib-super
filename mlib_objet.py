#******************
#
# mlib_objet.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient la classe "Objet", et tout le nécessaire pour l'utiliser.
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

# Importer Pygame pour utiliser le contexte OpenGL
import pygame

#******************
#
# La classe "Objet"
#
#******************

class Objet:
    """Classe représentant un objet 2D"""

    # Constructeur de "Objet"
    def __init__(self, nom: str, x: int = 0, y: int = 0, largeur: int = 0, hauteur: int = 0) -> None:
        """Constructeur d'un objet 2D

        Arguments:
            nom (str): nom de l'objet
            x (int, optional): Position X de l'objet. Defaults to 0.
            y (int, optional): Position Y de l'objet. Defaults to 0.
            largeur (int, optional): Largeur de l'objet. Defaults to 0.
            hauteur (int, optional): Hauteur de l'objet. Defaults to 0.
        """
        
        # Définition des attributs de base
        self.__couleur_arriere_plan = (255, 255, 255, 0)
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__nom = largeur
        self.__surface = 0
        self.__x = x
        self.__y = y

    def maj_rendu(self, surface_ecran: pygame.Surface) -> None:
        """Fonction exécutée pour mettre la fenêtre graphique à jour, en y appliquant le rendu de l'objet

        Args:
            surface_ecran (pygame.Surface): Fenêtre graphique, où le rendu doit être fait
        """

        # Création de la surface de l'objet
        self.__surface = pygame.Surface((self.__largeur, self.__hauteur))
        self.__surface.fill(self.__couleur_arriere_plan)
        # Applique le rendu nécessaire
        self.rendu(self.__surface)

        # Application de la surface sur l'écran pricipal
        surface_ecran.blit(self.__surface, (self.__x, self.__y))

    def rendu(self, surface_objet: pygame.Surface) -> None:
        """Applique le rendu nécessaire à la surface de l'objet

        Args:
            surface_objet (pygame.Surface): Surface de l'objet
        """
        pass

    # Getters et setters
    def set_couleur_arriere_plan(self, nouvel_couleur_arriere_plan: tuple) -> None:
        """Modifie la valeur de la couleur d'arrière plan

        Argument:
            nouvel_hauteur (int): Nouvelle couleur d'arrière plan
        """
        self.__couleur_arriere_plan = nouvel_couleur_arriere_plan
    def set_hauteur(self, nouvel_hauteur: int) -> None:
        """Modifie la valeur de hauteur

        Argument:
            nouvel_hauteur (int): Nouvelle valeur de hauteur
        """
        self.__hauteur = nouvel_hauteur
    def set_largeur(self, nouvel_largeur: int) -> None:
        """Modifie la valeur de largeur

        Argument:
            nouvel_largeur (int): Nouvelle valeur de largeur
        """
        self.__largeur = nouvel_largeur
    def set_x(self, nouvel_x: int) -> None:
        """Modifie la valeur de x

        Argument:
            nouvel_x (int): Nouvelle valeur de x
        """
        self.__x = nouvel_x
    def set_y(self, nouvel_y: int) -> None:
        """Modifie la valeur de y

        Argument:
            nouvel_y (int): Nouvelle valeur de y
        """
        self.__y = nouvel_y

#******************
#
# La classe "Objet"
#
#******************

class Texte(Objet) :
    """Classe représentant un texte 2D"""

    def __init__(self, nom: str, x: int = 0, y: int = 0, largeur: int = 0, hauteur: int = 0) -> None:
        """Constructeur d'un objet 2D

        Arguments:
            nom (str): nom de l'objet
            x (int, optional): Position X de l'objet. Defaults to 0.
            y (int, optional): Position Y de l'objet. Defaults to 0.
            largeur (int, optional): Largeur de l'objet. Defaults to 0.
            hauteur (int, optional): Hauteur de l'objet. Defaults to 0.
        """
        super().__init__(nom, x, y, largeur, hauteur)

        # Définition des attributes
        self.__police = 0
        self.__police_taille = 20
        self.__texte = ""
        self.__texte_alignement_horizontal = 1
        self.__texte_alignement_vertical = 1
        self.__texte_couleur = (0, 0, 0)

    def __maj_police(self) -> None:
        """Met la police du texte à jour"""
        self.__police = pygame.font.SysFont(pygame.font.get_default_font(), self.__police_taille)
    
    def rendu(self, surface_objet: pygame.Surface) -> None:
        """Applique le rendu nécessaire à la surface de l'objet

        Args:
            surface_objet (pygame.Surface): Surface de l'objet
        """
        
        # Création du texte nécessaire
        surface_texte = self.__police.render(self.__texte, True, self.__texte_couleur)

        # Calcul des coordonnées du texte
        texte_x = 0
        if self.__texte_alignement_horizontal == 1 : texte_x = surface_objet.get_width() / 2.0 - surface_texte.get_width() / 2.0
        elif self.__texte_alignement_horizontal == 2 : texte_x = surface_objet.get_width() - surface_texte.get_width()
        texte_y = 0
        if self.__texte_alignement_vertical == 1 : texte_y = surface_objet.get_height() / 2.0 - surface_texte.get_height() / 2.0
        elif self.__texte_alignement_vertical == 2 : texte_y = surface_objet.get_height() - surface_texte.get_height()

        # Copie de la surface du texte
        surface_objet.blit(surface_texte, (texte_x, texte_y))

    # Getters et setters
    def set_police_taille(self, nouvelle_police_taille: int) -> None:
        """Change la taille de la police du texte

        Args:
            nouvelle_police_taille (int): Nouvelle taille de la police du texte
        """
        if self.__police_taille != nouvelle_police_taille:
            self.__police_taille = nouvelle_police_taille
            self.__maj_police()
    def set_texte(self, nouveau_texte: str) -> None:
        """Change le texte de l'objet

        Args:
            nouveau_texte (str): Nouveau texte de l'objet
        """
        if self.__texte != nouveau_texte:
            self.__texte = nouveau_texte
    def set_texte_alignement_horizontal(self, nouveau_texte_alignement_horizontal: int) -> None:
        """Change l'alignement horizontal texte de l'objet

        Args:
            nouveau_texte_alignement_horizontal (str): Nouveau alignement horizontal du texte de l'objet
        """
        if self.__texte_alignement_horizontal != nouveau_texte_alignement_horizontal:
            self.__texte_alignement_horizontal = nouveau_texte_alignement_horizontal
    def set_texte_alignement_vertical(self, nouveau_texte_alignement_vertical: int) -> None:
        """Change l'alignement vertical texte de l'objet

        Args:
            nouveau_texte_alignement_vertical (str): Nouveau alignement vertical du texte de l'objet
        """
        if self.__texte_alignement_vertical != nouveau_texte_alignement_vertical:
            self.__texte_alignement_vertical = nouveau_texte_alignement_vertical