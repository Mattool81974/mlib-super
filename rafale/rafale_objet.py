#******************
#
# rafale_objet.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient les objets pour le projet NSI test de MLib Super : "Rafale".
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

from mlib import *
from mlib_gui.mlib_structure_plus import Structure_Plus

#******************
#
# La classe "Rafale"
#
#******************

class Mitrailleuse:
    """Classe représentant une mitrailleuse équipable sur un véhicule"""

    # Constructeur de "Mitrailleuse"
    def __init__(self, moteur_raycast: Raycast_Moteur, nom: str) -> None:
        """Constructeur de "Mitrailleuse"

        Returns:
            _type_: _description_
        """

        # Définition des attributs
        self.__balles_tirees = 0
        self.__cadence = 10
        self.__moteur_raycast = moteur_raycast
        self.__nom = nom
        self.__temps_dernier_tir = 0

    # Valide un tir
    def __tirer(self, position_tir: Transformation_3D) -> None:
        """Tire une munition"""
        balle = self.moteur_raycast().nouvel_objet_dynamique(self.nom() + "-balle_" + str(self.__balles_tirees), "balle")
        position_finale = position_tir + position_tir.devant_normalise() * 4
        balle.set_x(position_finale.x())
        balle.set_y(position_finale.y())
        balle.set_z(position_finale.z())
        self.__balles_tirees += 1
    # Tire avec la mitrailleuse
    def tirer(self, position_tir: Transformation_3D) -> bool:
        """Tire avec la mitrailleuse

        Returns:
            bool: si le tire a bien eu lieu
        """

        # Vérifie si le tir peut avoir lieu
        if time_ns() - self.__temps_dernier_tir < 1.0/self.cadence(): return
        self.__temps_dernier_tir = time_ns()
        self.__tirer(position_tir)

    # Getters et setters
    def cadence(self) -> int:
        """Retourne la cadence de la mitrailleuse

        Returns:
            int: cadence de la mitrailleuse
        """
        return self.__cadence
    def moteur_raycast(self) -> Raycast_Moteur:
        """Retourne le moteur de raycast de la mitrailleuse

        Returns:
            Raycast_Moteur: moteur de raycast de la mitrailleuse
        """
        return self.__moteur_raycast
    def nom(self) -> str:
        """Retourne le nom de la mitrailleuse

        Returns:
            str: nom de la mitrailleuse
        """
        return self.__nom
    def structure_plus(self) -> Structure_Plus:
        """Retourne la Structure_Plus de la mitrailleuse

        Returns:
            Structure_Plus: Structure_Plus de la mitrailleuse
        """
        return self.moteur_raycast().structure_plus()

class Rafale_Moteur:
    """Classe représentant un moteur de Rafale (Safran M88-2)"""

    # Constructeur de "Rafale_Moteur"
    def __init__(self) -> None:
        """Constructeur d'un "Rafale_Moteur"
        """

        # Définition des attributs
        self.__poussee = 0
        self.__poussee_maximale = 50000

    # Getters et setters
    def poussee(self) -> float:
        """Retourne la poussée actuelle du moteur en Newton

        Returns:
            float: poussée actuelle du moteur en Newton
        """
        return self.__poussee
    def set_poussee(self, nouvelle_poussee: float) -> None:
        """Change la poussée actuelle du rafale en KN

        Args:
            nouvelle_poussee (float): nouvelle poussée actuelle du rafale KN=
        """
        self.__poussee = nouvelle_poussee

class Rafale(Raycast_Objet_Dynamique):
    """Classe représentant un Rafale (partie physique et graphique)"""

    # Constructeur de "Rafale"
    def __init__(self, raycast_moteur: Raycast_Moteur, nom: str):
        """ Constructeur de "Raycast_Objet_Dynamique"

        Args:
            raycast_moteur_structure (Raycast_Moteur_Structure): moteur principal de l'objet dynamique
            nom (str): nom de l'objet dynamique
        """
        super().__init__(raycast_moteur, nom)

        # Définition des attributs
        self.__gravite = 9.81
        self.__mitrailleuse = Mitrailleuse(raycast_moteur, nom + "-defa")
        self.__moteur_droit = Rafale_Moteur()
        self.__moteur_gauche = Rafale_Moteur()
        self.__poids = 3680
        self.__vitesse = Point_3D()

        self.__moteur_droit.set_poussee(75000)
        self.__moteur_gauche.set_poussee(75000)

    # Met le Rafale à jour
    def maj(self) -> None:
        """Effectue une mise à jour du rafale"""

        # Met à jour la vitesse du rafale
        # Prend en compte la poussée
        poussee_globale = self.moteur_droit().poussee() + self.moteur_gauche().poussee()
        vecteur_avant = self.devant_normalise()
        vitesse_accumulee = vecteur_avant.copie()
        vitesse_accumulee *= (poussee_globale / self.poids()) * self.structure_plus().delta_time()
        self.__vitesse += vitesse_accumulee

        # Prend en compte le changement de rétention d'énergie
        modification_rotation = 0
        modification_rotation_z = 0
        rotation_seconde = 1.0
        rotation_x_seconde = pi / 2.0
        if self.structure_plus().touche_pressee("q"):
            modification_rotation = rotation_seconde * self.structure_plus().delta_time()
            modification_rotation_z = rotation_x_seconde * self.structure_plus().delta_time()
            tourner(self.__vitesse, modification_rotation)
        if self.structure_plus().touche_pressee("d"):
            modification_rotation = -rotation_seconde * self.structure_plus().delta_time()
            modification_rotation_z = -rotation_x_seconde * self.structure_plus().delta_time()
            tourner(self.__vitesse, modification_rotation)
        if modification_rotation != 0: self.__vitesse *= (1.0 - (self.structure_plus().delta_time()/4.0))
        self.set_rotation_z(self.rotation_z() + modification_rotation_z)
        if self.rotation_z() > pi / 2.0: self.set_rotation_z(pi / 2.0)
        if self.rotation_z() < -pi / 2.0: self.set_rotation_z(-pi / 2.0)
        self.set_rotation_y(self.rotation_y() + modification_rotation)
        
        # Prend en compte les frottements
        vitesse_actuelle = self.__vitesse.copie()
        vitesse_actuelle.set_z(vitesse_actuelle.z() * 2)
        vitesse_a_enlever = vecteur_avant.copie()
        vitesse_a_enlever -= vitesse_actuelle
        vitesse_a_enlever *= 0.1 * self.structure_plus().delta_time()
        self.__vitesse += vitesse_a_enlever
        self.set_rotation_z(self.rotation_z() * (1.0 - (self.structure_plus().delta_time()) * 3.0))

        # Mettre le rafale en mouvement
        vitesse_a_ajouter = self.__vitesse.copie()
        vitesse_a_ajouter *= 0.01
        vitesse_a_ajouter *= self.structure_plus().delta_time()
        self.ajouter(vitesse_a_ajouter)

        # Attaque avec le Rafale
        if self.structure_plus().touche_pressee("e"):
            self.tirer()
    # Tirer avec le Rafale
    def tirer(self) -> None:
        """Tire avec le Rafale"""
        self.mitrailleuse().tirer(self)

    # Getters et setters
    def mitrailleuse(self) -> Mitrailleuse:
        """Retourne la mitrailleuse utilisé dans le rafale

        Returns:
            Mitrailleuse: mitrailleuse utilisé dans le rafale
        """
        return self.__mitrailleuse
    def moteur_droit(self) -> Rafale_Moteur:
        """Retourne le moteur droit du Rafale

        Returns:
            Rafale_Moteur: moteur droit du Rafale
        """
        return self.__moteur_droit
    def moteur_gauche(self) -> Rafale_Moteur:
        """Retourne le moteur gauche du Rafale

        Returns:
            Rafale_Moteur: moteur gauche du Rafale
        """
        return self.__moteur_gauche
    def poids(self) -> float:
        """Retourne le poids du rafale en Kg

        Returns:
            float: poids du rafale en Kg
        """
        return self.__poids
    def moteur_raycast(self) -> Raycast_Moteur:
        """Retourne le moteur Raycast de l'objet

        Returns:
            Raycast_Moteur: moteur Raycast de l'objet
        """
        return self.raycast_moteur_structure()
    def vitesse(self) -> Point_3D:
        """Retourne la vitesse du rafale

        Returns:
            Point_3D: vitesse du rafale
        """
        return self.__vitesse