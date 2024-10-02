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
from math import acos, asin, sin, cos, sqrt, pow, pi

#******************
#
# La classe "Point_3D"
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

    # Ajoute un vecteur à ce point
    def ajouter(self, vecteur):
        """Ajouter un vecteur à ce point

        Args:
            vecteur (Point_3D): valeur à ajouter
        """
        self.set_x(self.x() + vecteur.x())
        self.set_y(self.y() + vecteur.y())
        self.set_z(self.z() + vecteur.z())
    # Copie et retourne ce point
    def copie(self):
        """Copie et retourne ce point

        Returns:
            Point_3D: copie de ce point
        """
        nouveau_point = Point_3D()
        nouveau_point.set_x(self.x())
        nouveau_point.set_y(self.y())
        nouveau_point.set_z(self.z())
        return nouveau_point
    # Enlève un vecteur à ce point
    def enlever(self, vecteur):
        """Enlève un vecteur à ce point

        Args:
            vecteur (Point_3D): valeur à ajouter
        """
        self.set_x(self.x() - vecteur.x())
        self.set_y(self.y() - vecteur.y())
        self.set_z(self.z() - vecteur.z())
    # Multiplie une valeur à ce point
    def multiplier_valeur(self, valeur: float):
        """Ajouter un vecteur à ce point

        Args:
            valeur (float): valeur à multiplier
        """
        self.set_x(self.x() * valeur)
        self.set_y(self.y() * valeur)
        self.set_z(self.z() * valeur)
    # Retourne la taille des points
    def valeur(self) -> float:
        """Retourne la taille des points

        Returns:
            float: taille des points
        """
        return sqrt(self.z() * self.z() + self.x() * self.x() + self.y() * self.y())

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
    def set_z(self, nouvel_z: float) -> None:
        """Modifie la valeur du Z dans le point

        Args:
            float (nouvel_z): nouvelle valeur du Z dans le point
        """
        self.__z = nouvel_z
    def set_xyz(self, xyz) -> None:
        """Change la valeur des trois axes 3D

        Args:
            xyz (Point_3D): nouvelle valeur des trois axes 3D
        """
        self.set_x(xyz.x())
        self.set_y(xyz.y())
        self.set_z(xyz.z())
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
    
    # Surchage des opérateurs
    def __add__(self, autre):
        """Retourne l'addition de ce point avec un autre

        Args:
            autre (Point_3D): point à additionner

        Returns:
            Point_3D: addition de ce point avec un autre
        """
        nouveau_point = Point_3D()
        nouveau_point.set_x(self.x() + autre.x())
        nouveau_point.set_y(self.y() + autre.y())
        nouveau_point.set_z(self.z() + autre.z())
        return nouveau_point
    def __iadd__(self, autre):
        """Effectue l'addition de ce point avec un autre

        Args:
            autre (Point_3D): point à additionner
        """
        self.set_x(self.x() + autre.x())
        self.set_y(self.y() + autre.y())
        self.set_z(self.z() + autre.z())
        return self
    def __imul__(self, autre):
        """Effectue la multiplication de ce point avec un autre

        Args:
            autre: valeur à multiplier
        """
        if type(autre) == float or type(autre) == int:
            self.set_x(self.x() * autre)
            self.set_y(self.y() * autre)
            self.set_z(self.z() * autre)
        return self
    def __isub__(self, autre):
        """Effectue la soustraction de ce point avec un autre

        Args:
            autre (Point_3D): point à soustraire
        """
        self.set_x(self.x() - autre.x())
        self.set_y(self.y() - autre.y())
        self.set_z(self.z() - autre.z())
        return self
    def __mul__(self, autre):
        """Effectue la multiplication de ce point avec un autre

        Args:
            autre: valeur à multiplier
        """
        point_final = self.copie()
        point_final *= autre
        return point_final
    def __sub__(self, autre):
        """Retourne la soustraction de ce point avec un autre

        Args:
            autre (Point_3D): point à soustraire

        Returns:
            Point_3D: soustraction de ce point avec un autre
        """
        nouveau_point = Point_3D()
        nouveau_point.set_x(self.x() - autre.x())
        nouveau_point.set_y(self.y() - autre.y())
        nouveau_point.set_z(self.z() - autre.z())
        return nouveau_point

def angle(premier_point: Point_3D, deuxieme_point: Point_3D, troisieme_point: Point_3D) -> float:
    """Retourne l'angle entre 3 points

    Args:
        premier_point (Point_3D): premier point
        deuxieme_point (Point_3D): deuxième_point
        troisieme_point (Point_3D): troisième_point

    Returns:
        float: angle entre ces 3 points
    """

    # Calculer le premier angle
    premier_hypothenus = sqrt(pow(premier_point.x() - deuxieme_point.x(), 2) + pow(premier_point.y() - deuxieme_point.y(), 2))
    premier_angle_x = asin(abs(deuxieme_point.y() - premier_point.y()) / premier_hypothenus)
    premier_angle_y = acos(abs(deuxieme_point.y() - premier_point.y()) / premier_hypothenus)

    # Calculer le deuxième angle
    deuxieme_hypothenus = sqrt(pow(troisieme_point.x() - deuxieme_point.x(), 2) + pow(troisieme_point.y() - deuxieme_point.y(), 2))
    deuxieme_angle_x = asin(abs(troisieme_point.y() - deuxieme_point.y()) / deuxieme_hypothenus)
    deuxieme_angle_y = acos(abs(troisieme_point.y() - deuxieme_point.y()) / deuxieme_hypothenus)

    # Renvoyer le bon résultat
    if premier_point.x() > deuxieme_point.x() and deuxieme_point.x() > troisieme_point.x():
        # Deuxième point au milieu des 2 points et 1er point après 3ème point
        if premier_point.y() > deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return pi - (premier_angle_x + deuxieme_angle_x)
        elif premier_point.y() > deuxieme_point.y() and troisieme_point.y() < deuxieme_point.y(): return pi + (pi / 2.0 - premier_angle_x) + deuxieme_angle_x
        elif premier_point.y() < deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return pi + (pi / 2.0 - deuxieme_angle_x) + premier_angle_x
        else: return -(pi - (premier_angle_x + deuxieme_angle_x))
    elif premier_point.x() < deuxieme_point.x() and deuxieme_point.x() < troisieme_point.x():
        # Deuxième point au milieu des 2 points 1er point avant 3ème point
        if premier_point.y() > deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return -(pi - (premier_angle_x + deuxieme_angle_x))
        elif premier_point.y() > deuxieme_point.y() and troisieme_point.y() < deuxieme_point.y(): return pi + (pi / 2.0 - deuxieme_angle_x) + premier_angle_x
        elif premier_point.y() < deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return pi + (pi / 2.0 - premier_angle_x) + deuxieme_angle_x
        else: return pi - (premier_angle_x + deuxieme_angle_x)
    elif premier_point.x() > deuxieme_point.x() and troisieme_point.x() > deuxieme_point.x():
        # Deuxième point à gauche (+ x) des 2 points
        if premier_point.y() == deuxieme_point.y(): return deuxieme_angle_x
        elif troisieme_point.y() == deuxieme_point.y(): return -premier_angle_x
        elif premier_point.y() > deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return (deuxieme_angle_x - premier_angle_x)
        elif premier_point.y() > deuxieme_point.y() and troisieme_point.y() < deuxieme_point.y(): return pi + (deuxieme_angle_x + premier_angle_x)
        elif premier_point.y() < deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return (deuxieme_angle_x + premier_angle_x)
        else: return (premier_angle_x - deuxieme_angle_x)
    else:
        # Deuxième point à droite (- x) des 2 points
        if premier_point.y() == deuxieme_point.y(): return -deuxieme_angle_x
        elif troisieme_point.y() == deuxieme_point.y(): return premier_angle_x
        elif premier_point.y() > deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return (premier_angle_x - deuxieme_angle_x)
        elif premier_point.y() > deuxieme_point.y() and troisieme_point.y() < deuxieme_point.y(): return (premier_angle_x + deuxieme_angle_x)
        elif premier_point.y() < deuxieme_point.y() and troisieme_point.y() > deuxieme_point.y(): return -(premier_angle_x + deuxieme_angle_x)
        else: return deuxieme_angle_x - premier_angle_x

    return (deuxieme_angle_y - premier_angle_y)

def distance(premier_point: Point_3D, deuxieme_point: Point_3D) -> float:
    """Retourne la distance entre deux points

    Args:
        premier_point (Point_3D): premier point
        deuxieme_point (Point_3D): premier point

    Returns:
        float: distance entre deux points
    """
    return sqrt(pow(premier_point.x() - deuxieme_point.x(), 2) + pow(premier_point.y() - deuxieme_point.y(), 2))

def tourner(point: Point_3D, rotation: float) -> None:
    """Tourne un point autour du centre (0, 0)

    Args:
        point (Point_3D): point à tourner
        rotation (float): rotation à appliquer au point
    """

    # Calcul du nécessaire à la rotation
    taille = sqrt(pow(point.x(), 2) + pow(point.y(), 2))
    angle_x = acos(point.x() / taille)
    if point.y() < 0: angle_x = 3.1415 * 2 - angle_x

    # Calcul de la nouvelle rotation
    angle_x += rotation
    point.set_x(cos(angle_x) * taille)
    point.set_y(sin(angle_x) * taille)

#******************
#
# La classe "Transformation_3D"
#
#******************

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
        avant.set_z(sin(self.rotation_x()))
        return avant

    # Getters et setters
    def rotation_x(self) -> float:
        """Retourne la rotation X de la transformation

        Returns:
            float: rotation X de la transformation
        """
        return self.__rotation_x
    def rotation_y(self) -> float:
        """Retourne la rotation Y de la transformation

        Returns:
            float: rotation Y de la transformation
        """
        return self.__rotation_y
    def rotation_z(self) -> float:
        """Retourne la rotation Z de la transformation

        Returns:
            float: rotation Z de la transformation
        """
        return self.__rotation_z
    def set_rotation_x(self, nouvelle_rotation_x: float) -> None:
        """Change la rotation X de la transformation

        Returns:
            float: nouvelle rotation X de la transformation
        """
        if nouvelle_rotation_x != self.__rotation_x:
            self.__rotation_x = nouvelle_rotation_x
    def set_rotation_y(self, nouvelle_rotation_y: float) -> None:
        """Change la rotation Y de la transformation

        Returns:
            float: nouvelle rotation Y de la transformation
        """
        if nouvelle_rotation_y != self.__rotation_y:
            self.__rotation_y = nouvelle_rotation_y
    def set_rotation_z(self, nouvelle_rotation_z: float) -> None:
        """Change la rotation Z de la transformation

        Returns:
            float: nouvelle rotation Z de la transformation
        """
        if nouvelle_rotation_z != self.__rotation_z:
            self.__rotation_z = nouvelle_rotation_z