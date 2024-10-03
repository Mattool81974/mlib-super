#******************
#
# rafale_fenetre.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient la fenêtre du projet NSI test de MLib Super : "Rafale".
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
from mlib_gui.raycast.mlib_raycast_objet import Structure_Plus
from rafale_objet import *
from random import randint

#******************
#
# La classe "Rafale_Raycast"
#
#******************

class Rafale_Raycast(Raycast_Moteur):
    """Classe représentant la fenêtre du projet NSI test de MLib Super : "Rafale"."""

    # Constructeur de "Rafale_Raycast"
    def __init__(self, structure_plus: Structure_Plus) -> None:
        """Constructeur de "Rafale_Raycast"

        Args:
            structure_plus (Structure_Plus): Structure_Plus du software
        """
        super().__init__(structure_plus)

        # Définition des attributs
        self.__cibles = []

    # Ajoute une cible à stocker
    def ajouter_cible(self, cible: Raycast_Objet_Dynamique) -> None:
        """Ajoute une cible à stocker

        Args:
            cible (Raycast_Objet_Dynamique): nouvelle cible à stocker
        """
        self.__cibles.append(cible)

    # Crée et retourne un nouvel objet dynamique avec son bon type
    def nouvel_objet_dynamique_createur(self, nom: str, type: str = "") -> Raycast_Objet_Dynamique:
        """Crée et retourne un nouvel objet dynamique avec son bon type

        Args:
            nom (str): nom de l'objet à créer
            type (str): type de l'objet à créer

        Returns:
            Raycast_Objet_Dynamique: objet crée
        """

        # Création d'un rafale
        if type == "rafale": return Rafale(self, nom)
        elif type == "balle": return Balle(self, nom)

        return super().nouvel_objet_dynamique_createur(self, nom)
    
    # Supprime un objet dynamique
    def supprimer_objet_dynamique(self, objet_dynamique: Raycast_Objet_Dynamique) -> None:
        """Supprime un objet dynamique"""

        # Supprime l'objet dynamique
        if objet_dynamique.contient_tag("cible"): self.cibles().remove(objet_dynamique)
        super().supprimer_objet_dynamique(objet_dynamique)

    # Getters et setters
    def cibles(self) -> list:
        """Retourne les cibles dans le moteur Raycast

        Returns:
            list: cibles dans le moteur Raycast
        """
        return self.__cibles

#******************
#
# La classe "Rafale_Fenetre"
#
#******************

class Rafale_Fenetre(Fenetre):
    """Classe représentant la fenêtre du projet NSI test de MLib Super : "Rafale"."""

    # Constructeur de "Rafale_Fenetre"
    def __init__(self, largeur: int, hauteur: int) -> None:
        """Constructeur de "Fenetre"

        Arguments:
            largeur (int): Largeur de la fenêtre
            hauteur (int): Hauteur de la fenêtre
        """
        super().__init__(largeur, hauteur)

        # Définition des attributs
        self.__cibles_crees = 0
        self.__moteur_raycast = self.nouveau_raycast()
        self.__raycast = self.nouvel_enfant("raycast", "raycast", 0, 0, largeur, hauteur)
        self.__rafale = self.moteur_raycast().nouvel_objet_dynamique("rafale", "rafale")
        self.__rafale_texture = self.nouvel_enfant("rafale", "objet", 0, hauteur / 3, largeur, hauteur / 2)

        # Données à propos du Rafale
        self.__altitude_rafale = self.nouvel_enfant("__altitude_rafale", "texte", largeur - 250, hauteur - 80, 250, 40)
        self.__vitesse_rafale = self.nouvel_enfant("vitesse_rafale", "texte", largeur - 250, hauteur - 40, 250, 40)

        # Chargement des textures
        self.charger_texture_chemin_acces("balle", "assets/ball.png")
        self.charger_texture_chemin_acces("rafale", "assets/rafale.png")
        self.charger_texture_chemin_acces("viseur", "assets/viseur.png")

        mur = self.moteur_raycast().nouveau_materiel(1)
        mur.set_couleur_2d((255, 0, 0))

        self.moteur_raycast().generer_map_depuis_texte_chemin_acces("assets/map.txt")

        self.__raycast.set_couleur_arriere_plan((0, 0, 255))
        self.__raycast.set_raycast_moteur(self.moteur_raycast())

        self.__rafale.set_visible(False)

        self.__rafale_texture.set_couleur_arriere_plan((0, 0, 0, 0))
        self.__rafale_texture.set_arriere_plan_texture_par_nom("rafale")

        self.__altitude_rafale.set_couleur_arriere_plan((255, 0, 0))
        self.__altitude_rafale.set_police_taille(30)
        self.__altitude_rafale.set_texte("5000 m")

        viseur = self.nouvel_enfant("viseur", "", 390, 390, 20, 20)
        viseur.set_arriere_plan_texture_par_nom("viseur")

        self.__vitesse_rafale.set_couleur_arriere_plan((255, 0, 0))
        self.__vitesse_rafale.set_police_taille(30)
        self.__vitesse_rafale.set_texte("0 km/h")

        self.rafale().set_rotation_x(3.1415)
        self.rafale().set_z(5)

        self.ajouter_cible()

    # Ajoute une cible dans le jeu
    def ajouter_cible(self) -> None:
        """Ajoute une cible dans le jeu"""

        # Créer la cible
        balle = self.moteur_raycast().nouvel_objet_dynamique("cible_" + str(self.__cibles_crees))
        balle.ajouter_tag("cible")
        balle.set_texture_par_nom("balle")
        balle.set_x(randint(0, self.moteur_raycast().largeur_map()))
        balle.set_y(randint(0, self.moteur_raycast().hauteur_map()))
        balle.set_z(2)
        self.moteur_raycast().ajouter_cible(balle)
        self.__cibles_crees += 1

    def nouvel_enfant_createur(self, nom: str, type: str) -> Objet:
        """Crée l'enfant, avec le type nécessaire selon "type

        Args:
            nom (str): Nom de l'enfant
            type (str): Type de l'enfant

        Returns:
            Objet: Enfant crée
        """

        # Création avec le type de base
        return super().nouvel_enfant_createur(nom, type)
    # Crée et retourne un moteur raycast pour la fenêtre
    def nouveau_raycast(self) -> Raycast_Moteur:
        """Crée et retourne un moteur raycast pour la fenêtre

        Returns:
            Raycast_Moteur: moteur raycast crée
        """
        return Rafale_Raycast(self)

    # Met à jour le rafale
    def maj_rafale(self) -> None:
        """Met à jour le rafale
        """

        if len(self.cibles()) <= 0:
            self.ajouter_cible()

        self.moteur_raycast().maj()
        altitude = self.rafale().z() * 100
        vitesse = self.rafale().vitesse().valeur()

        rotation_speed = (3.1415)/5.0
        if self.touche_pressee("fh") or self.touche_pressee("z"): self.rafale().set_rotation_x(self.rafale().rotation_x() - rotation_speed * self.delta_time())
        if self.touche_pressee("fb") or self.touche_pressee("s"): self.rafale().set_rotation_x(self.rafale().rotation_x() + rotation_speed * self.delta_time())
        self.__rafale_texture.set_texture_rotation(self.rafale().rotation_z() * (180.0/pi))

        self.moteur_raycast().camera().set_xyz(self.rafale())
        self.moteur_raycast().camera().set_rotation_x(self.rafale().rotation_x())
        self.moteur_raycast().camera().set_rotation_y(self.rafale().rotation_y())

        self.__altitude_rafale.set_texte(str(altitude).split(".")[0] + " m")
        self.__vitesse_rafale.set_texte(str(vitesse * 3.6).split(".")[0] + " km/h")
    
    # Getters et setters
    def cibles(self) -> list:
        """Retourne les listes dans le jeu

        Returns:
            list: listes dans le jeu
        """
        return self.moteur_raycast().cibles()
    def moteur_raycast(self) -> Rafale_Raycast:
        """Retourne le moteur raycast pour le rafale

        Returns:
            Raycast_Moteur: moteur raycast pour le rafale
        """
        return self.__moteur_raycast
    def rafale(self) -> Rafale:
        """Retourne le Rafale dans la fenêtre

        Returns:
            Rafale: Rafale dans la fenêtre
        """
        return self.__rafale