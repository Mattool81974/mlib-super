#******************
#
# mlib_structure_plus.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du projet "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient la classe "Structure_Plus", et tout le nécessaire pour l'utiliser.
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

# Importer des données sur les chemin d'accés
import os.path
# Importer pygame pour utiliser Pygame
import pygame

#******************
#
# La classe "Texture"
#
#******************

class Texture:
    """Classe représentant une texture pour MLib"""

    # Constructeur de "Texture"
    def __init__(self, nom: str, texture_chemin_acces: str = "") -> None:
        """Constructeur d'une texture MLib

        Arguments:;
            nom (str): nom de la texture
            texture_chemin_acces (str): chemin d'accés de l'image de la texture
        """

        # Définition des attributs de base
        self.__chemin_acces = texture_chemin_acces
        self.__nom = nom
        self.__surface = 0

        # Charger la texture (si elle utilise un chemin d'accés)
        if(texture_chemin_acces != ""):
            if os.path.exists(texture_chemin_acces):
                self.__surface = pygame.image.load(texture_chemin_acces)
            else:
                print("MLib Texture : le chemin d'accés \"" + texture_chemin_acces + "\" pour la texture \"" + nom + "\" n'existe pas.")

    def nom(self) -> str:
        """Retourne le nom de la texture

        Returns:
            str: nom de la texture
        """
        return self.__nom
    def surface(self) -> pygame.Surface:
        """Retourne la surface de la texture

        Returns:
            pygame.Surface: surface de la texture
        """
        return self.__surface

#******************
#
# La classe "Structure_Plus"
#
#******************

class Structure_Plus :
    """Classe représentant la structure de base de la fenêtre"""

    # Constructeur de "Structure_Plus :"
    def __init__(self) -> None:
        """Constructeur d'une structure plus de fenêtre
        """

        # Définition des attributes de bases
        self.__delta_time = 0
        self.__dernier_delta_time = 0
        self.__touches_etats = {}
        self.__textures = []

    # Charge une texture selon un chemin d'accés et la retourne
    def charger_texture_chemin_acces(self, texture_nom: str, texture_chemin_acces: str) -> Texture:
        """Charge une texture selon un chemin d'accés et la retourne

        Args:
            texture_nom (str): nom de la texture
            texture_chemin_acces (str): chemin d'accés de la texture

        Returns:
            Texture: texture chargée
        """
        if self.texture_nom(texture_nom) == 0:
            if os.path.exists(texture_chemin_acces):
                nouvelle_texture = Texture(texture_nom, texture_chemin_acces)
                self.textures().append(nouvelle_texture)
                return nouvelle_texture
            else:
                print("MLib Structure Plus de la Fenêtre : la texture \"" + texture_nom + "\" que vous essayez de charger utilise le chemin d'accés \"" + texture_chemin_acces + "\", qui n'existe pas.")
        else:
            print("MLib Structure Plus de la Fenêtre : la texture \"" + texture_nom + "\" que vous essayez de charger existe déjà.")
    # Retourne une texture
    def texture_nom(self, texture_nom: str) -> Texture:
        """Retourne une texture slon son nom

        Args:
            texture_nom (str): nom de la texture

        Returns:
            Texture: texture avec ce nom (ou 0 si aucune texture de ce nom existe)
        """

        # Parcourir les texture
        for t in self.__textures:
            if t.nom() == texture_nom:
                return t
        return 0

    # Getters et setters
    def delta_time(self) -> int:
        """Retourne le delta time entre deux exécution du software

        Returns:
            int: delta time entre deux exécution du software
        """
        return self.__delta_time
    def dernier_delta_time(self) -> int:
        """Retourne le dernier delta time entre deux exécution du software

        Returns:
            int: dernier delta time entre deux exécution du software
        """
        return self.__dernier_delta_time
    def set_delta_time(self, nouveau_delta_time: int) -> None:
        """Modifie la valeur du delta time entre deux exécution du software

        Args:
            delta_time (int): nouvelle valeur du delta time entre deux exécution du software
        """
        self.__delta_time = nouveau_delta_time
    def set_dernier_delta_time(self, nouveau_dernier_delta_time: int) -> None:
        """Modifie la valeur du dernier delta time entre deux exécution du software

        Args:
            delta_time (int): nouvelle valeur du dernier delta time entre deux exécution du software
        """
        self.__dernier_delta_time = nouveau_dernier_delta_time
    def textures(self) -> list:
        """Retourne les textures chargées dans la structure

        Returns:
            dict: textures chargées dans la structure
        """
        return self.__textures
    def touche_pressee(self, touche: str) -> bool:
        """Retourne si une touche est actuellement pressée

        Args:
            touche (str): touche à tester

        Returns:
            bool: si la touche est pressé ou pas
        """
        return list(self.touches_pressees()).count(touche) > 0
    def touches_etats(self) -> dict:
        """Retourne le dictionnaire des états des touches pressées

        Returns:
            list: dictionnaire des états des touches pressées
        """
        return self.__touches_etats
    def touches_pressees(self) -> list:
        """Retourne la liste des touches pressées

        Returns:
            list: liste des touches pressées
        """
        return self.__touches_etats.keys()