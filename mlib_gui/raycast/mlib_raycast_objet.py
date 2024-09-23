#******************
#
# mlib_raycast_objet.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient la base pour l'utilisation du Raycast.
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
# Importer des données sur les chemin d'accés
import os.path
# Importer des données sur les objets de base de MLib
from mlib_structure_plus import *

#******************
#
# La classe "Raycast_Materiel"
#
#******************

class Raycast_Materiel:
    """Classe représentant un matériel pour le raycast"""

    # Constructeur de "Raycast_Materiel"
    def __init__(self, id: int) -> None:
        """Constructeur de "Raycast_Materiel"

        Arguments:
            id (int): id du matériel
        """

        # Définition des attributs
        self.__couleur_2d = (0, 0, 0)
        self.__id = id
    
    # Getters et setters
    def couleur_2d(self) -> tuple:
        """Retourne la couleur du matériel en 2D

        Returns:
            tuple: couleur du matériel en 2D
        """
        return self.__couleur_2d
    def id(self) -> int:
        """Retourne l'id du matériel

        Returns:
            int: id du matériel
        """
        return self.__id
    def set_couleur_2d(self, couleur_2d: tuple) -> None:
        """Change la valeur de la couleur 2D

        Args:
            couleur_2d (tuple): nouvelle valeur de la couleur 2D
        """
        self.__couleur_2d = couleur_2d

#******************
#
# La classe "Raycast_Moteur_Structure"
#
#******************

class Raycast_Moteur_Structure:
    """Structure de base d'un Raycast_Moteur"""

    # Constructeur de "Raycast_Moteur_Structure"
    def __init__(self, structure_plus: Structure_Plus) -> None:
        """Constructeur de "Raycast_Moteur_Structure"

        Returns:
            _type_: _description_
        """

        # Définition des attributs
        self.__materiaux = []
        self.__structure_plus = structure_plus
    
    # Retourne un matériel dans le moteur par l'id
    def materiel_par_id(self, id: int) -> Raycast_Materiel:
        """Retourne un matériel dans le moteur par l'id

        Args:
            id (int): id du matériel recherché

        Returns:
            Raycast_Materiel: matériel recherché (ou 0 si il n'existe pas)
        """

        # Naviguer parmi les matériaux
        for materiel in self.__materiaux:
            if materiel.id() == id:
                return materiel
        return 0
    # Crée et retourne un nouveau matériel
    def nouveau_materiel(self, id: int) -> Raycast_Materiel:
        """Crée et retourne un nouveau matériel

        Args:
            id (int): id du matériel

        Returns:
            Raycast_Materiel: matériel crée
        """

        if self.materiel_par_id(id) == 0:
            # Créer le matériel
            nouveau_materiel = Raycast_Materiel(id)
            self.__materiaux.append(nouveau_materiel)
            return nouveau_materiel
        else :
            print("MLib Raycast moteur : le matériel d'id \"" + str(id) + "\" que vous essayez de créer existe déjà.")
        return 0

    # Getters et setters
    def structure_plus(self) -> Structure_Plus:
        """Retourne la Structure_Plus du software

        Returns:
            Structure_Plus: Structure_Plus du software
        """
        return self.__structure_plus

#******************
#
# La classe "Raycast_Objet_Dynamique"
#
#******************

class Raycast_Objet_Dynamique:
    """Classe représentant un objet dynamique pour le raycast"""

    # Constructeur de "Raycast_Objet_Dynamique"
    def __init__(self, raycast_moteur_structure: Raycast_Moteur_Structure, nom: str):
        """ Constructeur de "Raycast_Objet_Dynamique"

        Args:
            nom (str): nom de l'objet dynamique
        """

        # Définition des attributs
        self.__materiel = 0
        self.__nom = nom
        self.__raycast_moteur_structure = raycast_moteur_structure
        self.__x = 0
        self.__y = 0
    
    # Getters et setters
    def materiel(self) -> Raycast_Materiel:
        """Retourne le matériel de raycast de l'objet

        Returns:
            Raycast_Materiel: matériel de raycast de l'objet
        """
        return self.__materiel
    def nom(self) -> str:
        """Retourne le nom de l'objet dynamique

        Returns:
            str: nom de l'objet dynamique
        """
        return self.__nom
    def raycast_moteur_structure(self) -> Raycast_Moteur_Structure:
        """Retourne la structure du moteur de raycast

        Returns:
            Raycast_Moteur_Structure: structure du moteur de raycast
        """
        return self.__raycast_moteur_structure
    def set_materiel(self, nouveau_materiel: Raycast_Materiel) -> None:
        """Change le matériel de raycast de l'objet

        Args:
            nouveau_materiel (Raycast_Materiel): nouveau le matériel de raycast de l'objet
        """
        self.__materiel = nouveau_materiel
    def set_materiel_par_id(self, nouveau_materiel: int) -> None:
        """Change le matériel de raycast de l'objet par son id

        Args:
            nouveau_materiel (Raycast_Materiel): id du nouveau matériel
        """
        self.set_materiel(self.raycast_moteur_structure().materiel_par_id(nouveau_materiel))
    def set_x(self, nouvel_x: float) -> None:
        """Change la valeur de x

        Args:
            nouvel_x (float): nouvelle valeur de x
        """
        self.__x = nouvel_x
    def set_y(self, nouvel_y: float) -> None:
        """Change la valeur de y

        Args:
            nouvel_y (float): nouvelle valeur de y
        """
        self.__y = nouvel_y
    def x(self) -> float:
        """Retourne la valeur de x

        Returns:
            float: valeur de x
        """
        return self.__x
    def y(self) -> float:
        """Retourne la valeur de y

        Returns:
            float: valeur de y
        """
        return self.__y