#******************
#
# mlib_math_transformation.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient des informations mathématiques à propos de transformation.
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

# Importer des fonctions mathématiques nécessaires
from math import sin, cos

#******************
#
# La classe "Transformation_3D"
#
#******************

class Point_3D:
    """Classe représentant un simple point en 3D"""

    # Constructeur de "Point_3D"
    def __init__(self) -> None:
        """Constructeur de "Point_3D
        """

        # Définition des attributs
        self.__x = 0
        self.__y = 0
        self.__z = 0

    # Getters et setters
    def set_x(self, nouvel_x: float) -> None:
        """Modifie la valeur du X dans le point

        Args:
            float (nouvel_x): nouvelle valeur du X dans le point
        """
        self.__x = nouvel_x
    def set_y(self, nouvel_y: float) -> None:
        """Modifie la valeur du Y dans le point

        Args:
            float (nouvel_y): nouvelle valeur du Y dans le point
        """
        self.__y = nouvel_y
    def x(self) -> float:
        """Retourne la position X de la transformation

        Returns:
            float: position X de la transformation
        """
        return self.__x
    def y(self) -> float:
        """Retourne la position Y de la transformation

        Returns:
            float: position Y de la transformation
        """
        return self.__y
    def z(self) -> float:
        """Retourne la position Z de la transformation

        Returns:
            float: position Z de la transformation
        """
        return self.__z

class Transformation_3D(Point_3D):
    """Classe représentant une transformation 3D"""

    # Constructeur de "Transformation_3D"
    def __init__(self) -> None:
        """Constructeur de "Transformation_3D"
        """
        super().__init__()

        # Définition des attributs
        self.__rotation_x = 0
        self.__rotation_y = 0
        self.__rotation_z = 0

    # Avance via le vecteur avant d'une certaine valeur
    def avancer(self, avancement: float) -> None:
        """Avance via le vecteur avant d'une certaine valeur

        Args:
            avancement (float): avancement du vecteur
        """
        avant = self.devant_normalise()
        self.set_x(self.x() + avant.x() * avancement)
        self.set_y(self.y() + avant.y() * avancement)
    # Retourne le vecteur "avant" de la trnasformation
    def devant_normalise(self, angle_ajuste: float = 0) -> Point_3D:
        """Retourne le vecteur "avant" de la trnasformation

        Argument:
            angle_ajuste (float): ajustement possible de l'angle, par défaut à 0.

        Returns:
            Point_3D: vecteur "avant" de la trnasformation
        """
        avant = Point_3D()
        avant.set_x(cos(self.rotation_y() + angle_ajuste))
        avant.set_y(sin(self.rotation_y() + angle_ajuste))
        return avant

    # Getters et setters
    def rotation_y(self) -> float:
        """Retourne la rotation Y de la transformation

        Returns:
            float: rotation Y de la transformation
        """
        return self.__rotation_y
    def set_rotation_y(self, nouvelle_rotation_y: float) -> None:
        """Change la rotation Y de la transformation

        Returns:
            float: nouvelle rotation Y de la transformation
        """
        if nouvelle_rotation_y != self.__rotation_y:
            self.__rotation_y = nouvelle_rotation_y