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
# Importer les données mathématiques nécessaire pour le raycast
from mlib_math.mlib_math_transformation import *
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
    # Retourne une liste de tous les objets dynamiques contenant un certain tag
    def objets_dynamiques_par_tag(self, tag: str) -> list:
        """Retourne une liste de tous les obejts dynamiques contenant un certain tag

        Args:
            tag (str): tag à tester

        Returns:
            list: liste des objets
        """
        return []

    # Supprime un objet dynamique
    def supprimer_objet_dynamique(self, objet_dynamique) -> None:
        """Supprime un objet dynamique"""
        pass

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

class Raycast_Objet_Dynamique(Transformation_3D):
    """Classe représentant un objet dynamique pour le raycast"""

    # Constructeur de "Raycast_Objet_Dynamique"
    def __init__(self, raycast_moteur_structure: Raycast_Moteur_Structure, nom: str):
        """ Constructeur de "Raycast_Objet_Dynamique"

        Args:
            raycast_moteur_structure (Raycast_Moteur_Structure): moteur principal de l'objet dynamique
            nom (str): nom de l'objet dynamique
        """
        super().__init__()

        # Définition des attributs
        self.__hauteur = 1
        self.__largeur = 1
        self.__materiel = 0
        self.__nom = nom
        self.__raycast_moteur_structure = raycast_moteur_structure
        self.__tags = []
        self.__texture = 0
        self.__visible = True

    # Rajoute un tag à l'objet
    def ajouter_tag(self, tag: str) -> None:
        """Rajoute un tag à l'objet

        Args:
            tag(str): tag à ajouter
        """
        if not self.contient_tag(tag):
            self.tags().append(tag)
    # Retourne si l'objet contient un tag
    def contient_tag(self, tag: str) -> bool:
        """Si l'objet contient un tag

        Args:
            tag (str): tag à tester

        Returns:
            bool: si l'objet contient un tag
        """
        return self.tags().count(tag)

    # Met l'objet à jour
    def maj(self) -> None:
        """Met l'objet à jour"""
        pass
    
    # Getters et setters
    def hauteur(self) -> float:
        """Retourne la hauteur de l'objet

        Returns:
            float: hauteur de l'objet
        """
        return self.__hauteur
    def largeur(self) -> float:
        """Retourne la largeur de l'objet

        Returns:
            float: largeur de l'objet
        """
        return self.__largeur
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
    def set_hauteur(self, nouvelle_hauteur: float) -> None:
        """Change la hauteur de l'objet

        Args:
            nouvelle_hauteur (float): nouvelle hauteur de l'objet
        """
        self.__hauteur = nouvelle_hauteur
    def set_largeur(self, nouvelle_largeur: float) -> None:
        """Change la largeur de l'objet

        Args:
            nouvelle_largeur (float): nouvelle largeur de l'objet
        """
        self.__largeur = nouvelle_largeur
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
    def set_texture_par_nom(self, nom_texture: str) -> None:
        """Change la texture par une texture d'un certain nom

        Args:
            nom_texture (str): nom de la nouvelle texture
        """
        texture = self.structure_plus().texture_nom(nom_texture)
        if texture != self.__texture:
            self.__texture = texture
    def set_visible(self, nouveau_visible: bool) -> None:
        """Change si l'objet est visible ou pas

        Args:
            nouveau_visible (bool): nouveau si l'objet est visible ou pas
        """
        if self.visible() != nouveau_visible:
            self.__visible = nouveau_visible
    def structure_plus(self) -> Structure_Plus:
        """Retourne la Structure_Plus du software

        Returns:
            Structure_Plus: Structure_Plus du software
        """
        return self.raycast_moteur_structure().structure_plus()
    def tags(self) -> list:
        """Retourne les tags de l'objet

        Returns:
            list: tags de l'objet
        """
        return self.__tags
    def texture(self) -> Texture:
        """Retourne la texture de l'objet

        Returns:
            Texture: texture de l'objet
        """
        return self.__texture
    def visible(self) -> bool:
        """Retourne si l'objet est visible ou pas

        Returns:
            bool: si l'objet est visible ou pas
        """
        return self.__visible