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
    def __init__(self, raycast_moteur_structure: Raycast_Moteur_Structure, nom: str):
        """ Constructeur de "Raycast_Objet_Dynamique"

        Args:
            raycast_moteur_structure (Raycast_Moteur_Structure): moteur principal de l'objet dynamique
            nom (str): nom de l'objet dynamique
        """
        super().__init__(raycast_moteur_structure, nom)

        # Définition des attributs
        self.__gravite = 9.81
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
    
    # Getters et setters
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
    def vitesse(self) -> Point_3D:
        """Retourne la vitesse du rafale

        Returns:
            Point_3D: vitesse du rafale
        """
        return self.__vitesse