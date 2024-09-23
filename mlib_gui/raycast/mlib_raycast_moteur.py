#******************
#
# mlib_raycast_moteur.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient le nécessaire à l'utilisation du Raycast.
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
# Importer les données basique sur le raycast
from mlib_raycast_objet import *

#******************
#
# La classe "Raycast_Case"
#
#******************

class Raycast_Case:
    """Classe représentant une case de la map d'un moteur raycast"""

    # Constructeur de "Raycast_Case"
    def __init__(self, contenu: Raycast_Materiel, x: int, y: int) -> None:
        """Constructeur de "Raycast_Case"
        """

        # Définition des attributs
        self.__contenu = contenu
        self.__sous_map = []
        self.__x = x
        self.__y = y

    # Getters et setters
    def contenu(self) -> Raycast_Materiel:
        """Retourne le contenu de la case

        Returns:
            int: contenu de la case
        """
        return self.__contenu

#******************
#
# La classe "Raycast_Camera"
#
#******************

class Raycast_Camera:
    """Classe représentant la caméra du moteur Raycast"""

    # Constructeur de "Raycast_Camera"
    def __init__(self, raycast_moteur_structure: Raycast_Moteur_Structure) -> None:
        """Constructeur de "Raycast_Camera"

        Args:
            raycast_moteur_structure (Raycast_Moteur_Structure): structure du moteur raycast
        """

        # Définition des attributs
        self.__raycast_moteur_structure = raycast_moteur_structure

#******************
#
# La classe "Raycast_Moteur"
#
#******************

class Raycast_Moteur(Raycast_Moteur_Structure):
    """Classe représentant un moteur de raycast"""

    # Constructeur de "Raycast_Moteur"
    def __init__(self, structure_plus: Structure_Plus) -> None:
        """Constructeur de "Raycast_Moteur"
        """
        super().__init__(structure_plus)

        # Définition des attributs
        self.__hauteur_map = 0
        self.__largeur_map = 0
        self.__map = []
        self.__objets_dynamiques = []

    # Génère la map depuis un texte
    def generer_map_depuis_texte(self, texte: str):
        """Génère la map depuis un texte

        Args:
            texte (str): texte d'où générer la map
        """

        # Préparer la génération
        self.__map = []
        texte = texte.replace(chr(10), "").replace(chr(13), "") # Suppression des caractères inutiles
        while texte.count(" ") > 0 : texte = texte.replace(" ", "")

        # Effectuer la génération
        decoupe = texte.split(";")
        self.__largeur_map, self.__hauteur_map, x_map, y_map = int(decoupe[0]), int(decoupe[1]), int(decoupe[2]), int(decoupe[3])
        x_map_actuel, y_map_actuel = x_map, y_map
        decoupe = decoupe[4].split("-")
        for partie in decoupe:
            # Parcourir ligne par ligne
            decoupe_temporaire = partie.split("_")
            ligne_actuelle = []
            for bloc in decoupe_temporaire:
                # Parcourir bloc par bloc
                materiel = int(bloc)
                if materiel != 0:
                    materiel = self.materiel_par_id(materiel)
                    if materiel == 0:
                        print("MLib Raycast moteur : le matériel \"" + bloc + "\" que vous essayez de charger n'existe pas.")
                case_actuelle = Raycast_Case(materiel, x_map_actuel, y_map_actuel)
                ligne_actuelle.append(case_actuelle)
                x_map_actuel += 1
            self.__map.append(ligne_actuelle)
            x_map_actuel = x_map
            y_map_actuel += 1
    # Génère la map depuis un texte dans un chemin d'accés
    def generer_map_depuis_texte_chemin_acces(self, chemin_acces: str) -> None:
        """Génère la map depuis un texte dans un chemin d'accés

        Args:
            chemin_acces (str): chemin d'accés où se trouve la map à générer
        """
        if os.path.exists(chemin_acces):
            fichier = open(chemin_acces)
            self.generer_map_depuis_texte(fichier.read())
            fichier.close()
        else:
            print("MLib Raycast moteur : le chemin d'accés \"" + chemin_acces + "\" que vous essayez de charger en tant que map n'existe pas.")

    # Crée et retourne un nouvel objet dynamique
    def nouvel_objet_dynamique(self, nom: str) -> Raycast_Objet_Dynamique:
        """Crée et retourne un nouvel objet dynamique

        Args:
            nom (str): nom de l'objet dynamique

        Returns:
            Raycast_Objet_Dynamique: objet dynamique crée (ou 0 si création impossible)
        """

        if self.objet_dynamique_par_nom(nom) == 0:
            # Création de l'objet dynamique
            nouvel_objet = Raycast_Objet_Dynamique(self, nom)
            self.__objets_dynamiques.append(nouvel_objet)
            return nouvel_objet
        else:
            print("MLib Raycast moteur : l'objet \"" + nom + "\" que vous essayez de créer existe déjà.")
        return 0
    # Retourne un objet dynamique par son nom
    def objet_dynamique_par_nom(self, nom: str) -> Raycast_Objet_Dynamique:
        """Retourne un objet dynamique par son nom

        Args:
            nom (str): nom de l'objet dynamique

        Returns:
            Raycast_Objet_Dynamique: objet dynamique (ou 0 si non trouvé)
        """
        for objet in self.__objets_dynamiques:
            if objet.nom() == nom:
                return objet
        return 0

    # Retourne le rendu 2D du raycast
    def rendu_2d(self) -> pygame.Surface:
        """Retourne le rendu 2D du raycast

        Returns:
            pygame.Surface: rendu 2D du raycast
        """

        # Création de la surface nécessaire
        largeur_case = 20
        surface = pygame.Surface((self.__largeur_map * largeur_case, self.__hauteur_map * largeur_case))

        # Dessiner les cases une par une dessus
        x_actuel, y_actuel = 0, 0
        for ligne in self.__map:
            for case in ligne:
                # On dessine les cases 1 par 1
                if case.contenu() != 0:
                    pygame.draw.rect(surface, case.contenu().couleur_2d(), (x_actuel * largeur_case, y_actuel * largeur_case, largeur_case, largeur_case))
                x_actuel += 1
            x_actuel = 0
            y_actuel += 1
        
        # Dessiner les objets dynamiques
        for objet in self.__objets_dynamiques:
            if objet.materiel() != 0:
                # Obtenir les coordonnées de l'objet
                x_objet = objet.x() * largeur_case
                y_objet = objet.y() * largeur_case
                pygame.draw.circle(surface, objet.materiel().couleur_2d(), (x_objet, y_objet), 4)

        return surface