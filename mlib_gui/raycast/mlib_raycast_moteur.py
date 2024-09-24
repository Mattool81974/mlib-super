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

# Importer des fonctions mathématiques nécessaires
from math import ceil, floor, pow, sqrt
# Importer pygame pour utiliser Pygame
import pygame
# Importer des données sur les chemin d'accés
import os.path
# Importer les données mathématiques nécessaire pour le raycast
from mlib_math.mlib_math_transformation import *
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

class Raycast_Camera(Transformation_3D):
    """Classe représentant la caméra du moteur Raycast"""

    # Constructeur de "Raycast_Camera"
    def __init__(self, raycast_moteur_structure: Raycast_Moteur_Structure) -> None:
        """Constructeur de "Raycast_Camera"

        Args:
            raycast_moteur_structure (Raycast_Moteur_Structure): structure du moteur raycast
        """
        super().__init__()

        # Définition des attributs
        self.__raycast_moteur_structure = raycast_moteur_structure

#******************
#
# La classe "Raycast_Moteur"
#
#******************

class Raycast:
    """Classe représentant un Raycast dans le moteur"""

    # Constructeur de "Raycast"
    def __init__(self) -> None:
        """Constructeur de "Raycast"
        """

        # Définition des attributs
        self.__point_final = Point_3D()
        self.__point_final_distance = -1

    # Getters et setter
    def point_final(self) -> Point_3D:
        """Retourne le point final du raycast

        Returns:
            Point_3D: point final du raycast
        """
        return self.__point_final
    def point_final_distance(self) -> float:
        """Retourne la distance au point final du raycast

        Returns:
            float: distance au point final du raycast
        """
        return self.__point_final_distance
    def set_point_final(self, nouveau_point: Point_3D, distance: float) -> None:
        """Change le point final du raycast

        Argument:
            nouveau_point (Point_3D): nouveau point final du raycast
            distance (float): distance au point final du raycast
        """
        self.__point_final = nouveau_point
        self.__point_final_distance = distance

class Raycast_Entier:
    """Classe représentant l'entiéreté des raycasts nécessaire à un rendu"""

    # Constructeur de "Raycast_Entier"
    def __init__(self) -> None:
        """Constructeur de "Raycast_Entier"
        """

        # Définition des attributs
        self.__point_depart = 0
        self.__raycasts = []

    # Getters et setters
    def point_depart(self) -> Point_3D:
        """Retourne le point de départ des raycasts

        Returns:
            Point_3D: point de départ des raycasts
        """
        return self.__point_depart
    def rayons(self) -> list:
        """Retourne la liste de raons générés

        Returns:
            List: la liste de rayons générés
        """
        return self.__raycasts
    def set_point_depart(self, point_depart: Point_3D) -> None:
        """Change la valeur du point de départ des raycasts

        Args:
            point_depart (Point_3D): nouveau point de départ des raycasts
        """
        self.__point_depart = point_depart

class Raycast_Moteur(Raycast_Moteur_Structure):
    """Classe représentant un moteur de raycast"""

    # Constructeur de "Raycast_Moteur"
    def __init__(self, structure_plus: Structure_Plus) -> None:
        """Constructeur de "Raycast_Moteur"
        """
        super().__init__(structure_plus)

        # Définition des attributs
        self.__camera = Raycast_Camera(self)
        self.__hauteur_map = 0
        self.__largeur_map = 0
        self.__map = []
        self.__objets_dynamiques = []

    # Retourne si une coordonnée est dans la map
    def dans_map(self, x_a_tester: int, y_a_tester: int) -> bool:
        """Retourne si une coordonnée est dans la map

        Args:
            coordonnee (Point_3D): coordonnée à tester

        Returns:
            bool: si la coordonnée est dans la map
        """
        x_a_tester = int(x_a_tester)
        y_a_tester = int(y_a_tester)
        return x_a_tester >= 0 and y_a_tester >= 0 and len(self.__map) > y_a_tester and len(self.__map[y_a_tester]) > x_a_tester
    def dans_map_point(self, point: Point_3D) -> bool:
        """Retourne si un point est dans la map

        Args:
            point (Point_3D): point à tester

        Returns:
            bool: si le point est dans la map
        """
        return self.dans_map(point.x(), point.y())
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

    # Effectue un raycast dans la map
    def raycast(self, point_de_depart: Transformation_3D, angle_ajuste: float = 0) -> Raycast:
        """Réalise et retourne un résultat de raycast

        Argument:
            point_de_depart (Transformation_3D): point de départ du rayon

        Returns:
            Raycast: résultat de raycast
        """

        # Préparation des raycast
        avant = point_de_depart.devant_normalise(angle_ajuste)

        # Réalisation du raycast vertical
        distance_verticale = -1
        point_vertical = Point_3D()
        point_vertical.set_x(point_de_depart.x() + avant.x())
        point_vertical.set_y(point_de_depart.y() + avant.y())
        if avant.y() != 0:
            # Calcul des différences nécessaires
            ajout_vertical = 1
            ratio_vertical = abs(avant.x() / avant.y())
            if avant.x() < 0 and avant.y() < 0:
                ajout_vertical = -ajout_vertical
                ratio_vertical = -ratio_vertical
            elif avant.x() < 0: ratio_vertical = -ratio_vertical
            elif avant.y() < 0: ajout_vertical = -ajout_vertical
            # Départ vers le début réel du raycast
            premiere_difference_vertical = ceil(point_de_depart.y()) - point_de_depart.y()
            if ajout_vertical < 0: premiere_difference_vertical = point_de_depart.y() - floor(point_de_depart.y())
            point_vertical = Point_3D()
            point_vertical.set_x(point_de_depart.x() + premiere_difference_vertical * ratio_vertical)
            point_vertical.set_y(ceil(point_de_depart.y()))
            if ajout_vertical < 0: point_vertical.set_y(floor(point_de_depart.y()))
            distance_verticale = sqrt(pow(point_vertical.x() - point_de_depart.x(), 2) + pow(point_vertical.y() - point_de_depart.y(), 2))
            # Premier test de la map
            x_a_tester = floor(point_vertical.x())
            y_a_tester = floor(point_vertical.y())
            if ajout_vertical > 0: y_a_tester = floor(point_vertical.y()) + 1
            if not(self.dans_map(x_a_tester, y_a_tester) and self.__map[y_a_tester][x_a_tester] != 0 and self.__map[y_a_tester][x_a_tester].contenu() != 0):
                # Envoie du rayon
                while self.dans_map_point(point_vertical):
                    # Nouvelle position
                    x_actuel = point_vertical.x() + ratio_vertical
                    y_actuel = point_vertical.y() + ajout_vertical
                    point_vertical.set_x(x_actuel)
                    point_vertical.set_y(y_actuel)
                    distance_verticale = sqrt(pow(x_actuel - point_de_depart.x(), 2) + pow(y_actuel - point_de_depart.y(), 2))

                    # Gérer la map
                    x_a_tester = floor(x_actuel)
                    y_a_tester = floor(y_actuel)
                    if ajout_vertical > 0: y_a_tester = floor(y_actuel) + 1
                    if self.dans_map(x_a_tester, y_a_tester):
                        if self.__map[y_a_tester][x_a_tester] != 0 and self.__map[y_a_tester][x_a_tester].contenu() != 0:
                            break

        # Réalisation du raycast horizontal
        distance_horizontale = -1
        point_horizontal = Point_3D()
        point_horizontal.set_x(point_de_depart.x() + avant.x())
        point_horizontal.set_y(point_de_depart.y() + avant.y())
        if avant.x() != 0:
            # Calcul des différences nécessaires
            ajout_horizontal = 1
            ratio_horizontal = abs(avant.y() / avant.x())
            if avant.x() < 0 and avant.y() < 0:
                ajout_horizontal = -ajout_horizontal
                ratio_horizontal = -ratio_horizontal
            elif avant.y() < 0: ratio_horizontal = -ratio_horizontal
            elif avant.x() < 0: ajout_horizontal = -ajout_horizontal
            # Départ vers le début réel du raycast
            premiere_difference_horizontale = ceil(point_de_depart.x()) - point_de_depart.x()
            if ajout_horizontal < 0: premiere_difference_horizontale = point_de_depart.x() - floor(point_de_depart.x())
            point_horizontal = Point_3D()
            point_horizontal.set_x(ceil(point_de_depart.x()))
            if ajout_horizontal < 0: point_horizontal.set_x(floor(point_de_depart.x()))
            point_horizontal.set_y(point_de_depart.y() + premiere_difference_horizontale * ratio_horizontal)
            distance_horizontale = sqrt(pow(point_horizontal.x() - point_de_depart.x(), 2) + pow(point_horizontal.y() - point_de_depart.y(), 2))
            # Premier test de la map
            x_a_tester = floor(point_horizontal.x()) - 1
            if ajout_horizontal > 0: x_a_tester = floor(point_horizontal.x())
            y_a_tester = ceil(point_horizontal.y())
            if not(self.dans_map(x_a_tester, y_a_tester) and self.__map[y_a_tester][x_a_tester] != 0 and self.__map[y_a_tester][x_a_tester].contenu() != 0):
                # Envoie du rayon
                while self.dans_map_point(point_horizontal):
                    # Nouvelle position
                    x_actuel = point_horizontal.x() + ajout_horizontal
                    y_actuel = point_horizontal.y() + ratio_horizontal
                    point_horizontal.set_x(x_actuel)
                    point_horizontal.set_y(y_actuel)
                    distance_horizontale = sqrt(pow(x_actuel - point_de_depart.x(), 2) + pow(y_actuel - point_de_depart.y(), 2))

                    # Gérer la map
                    x_a_tester = floor(x_actuel) - 1
                    if ajout_horizontal > 0: x_a_tester = floor(x_actuel)
                    y_a_tester = ceil(y_actuel)
                    if self.dans_map(x_a_tester, y_a_tester):
                        if self.__map[y_a_tester][x_a_tester] != 0 and self.__map[y_a_tester][x_a_tester].contenu() != 0:
                            break
        
        # Préparer les données finales
        final = Raycast()
        if distance_horizontale <= -1:
            final.set_point_final(point_vertical, distance_verticale)
        elif distance_verticale <= -1:
            final.set_point_final(point_horizontal, distance_horizontale)
        elif distance_verticale <= distance_horizontale:
            final.set_point_final(point_vertical, distance_verticale)
        else:
            final.set_point_final(point_horizontal, distance_horizontale)
        return final
    # Effectue l'entiéreté des raycasts nécessaires à un rendu
    def raycast_entier(self) -> Raycast_Entier:
        """Retourne les données sur l'entiéreté des raycasts nécessaires à un rendu

        Returns:
            Raycast_Entier: données sur l'entiéreté des raycasts nécessaires à un rendu
        """

        # Congifurer le Raycast_Entier
        fov = 0.5
        nombre_rayons = 100
        raycasts = Raycast_Entier()
        raycasts.set_point_depart(self.camera())

        # Réalise l'entiéreté des rayons
        for i in range(nombre_rayons):
            raycast = self.raycast(self.camera(), fov / 2.0 - i * ((fov)/nombre_rayons))
            raycasts.rayons().append(raycast)
        
        return raycasts

    # Retourne le rendu 2D du raycast
    def rendu_2d(self) -> pygame.Surface:
        """Retourne le rendu 2D du raycast

        Returns:
            pygame.Surface: rendu 2D du raycast
        """

        # Création de la surface nécessaire
        largeur_case = 20
        surface = pygame.Surface((self.__largeur_map * largeur_case, self.__hauteur_map * largeur_case))

        # Dessiner la caméra
        if self.camera() != 0:
            # Obtenir les coordonnées de la caméra
            x_objet = self.camera().x() * largeur_case
            y_objet = surface.get_height() - self.camera().y() * largeur_case
            
            # Dessiner les rayons de raycast
            raycasts = self.raycast_entier()
            for rayon in raycasts.rayons():
                x_objet, y_objet = raycasts.point_depart().x() * largeur_case, surface.get_height() - raycasts.point_depart().y() * largeur_case
                x_devant, y_devant = rayon.point_final().x() * largeur_case, surface.get_height() - rayon.point_final().y() * largeur_case
                pygame.draw.circle(surface, (0, 255, 0), (x_objet, y_objet), 4)
                pygame.draw.line(surface, (0, 255, 0), (x_objet, y_objet), (x_devant, y_devant), 2)

        # Dessiner les cases une par une dessus
        x_actuel, y_actuel = 0, 0
        for ligne in self.__map:
            for case in ligne:
                # On dessine les cases 1 par 1
                if case.contenu() != 0:
                    pygame.draw.rect(surface, case.contenu().couleur_2d(), (x_actuel * largeur_case, surface.get_height() - y_actuel * largeur_case, largeur_case, largeur_case))
                x_actuel += 1
            x_actuel = 0
            y_actuel += 1
        
        # Dessiner les objets dynamiques
        for objet in self.__objets_dynamiques:
            if objet.materiel() != 0:
                # Obtenir les coordonnées de l'objet
                x_objet = objet.x() * largeur_case
                y_objet = surface.get_height() - objet.y() * largeur_case
                pygame.draw.circle(surface, objet.materiel().couleur_2d(), (x_objet, y_objet), 4)

        return surface
    # Retourne le rendu 3D du raycast
    def rendu_3d(self) -> pygame.Surface:
        """Retourne le rendu 3D du raycast

        Returns:
            pygame.Surface: rendu 3D du raycast
        """

        # Création de la surface et des inforamtions nécessaire
        raycasts = self.raycast_entier()
        surface = pygame.Surface((500, 500))

        # Dessiner chaque rayon
        largeur_rayon = surface.get_width() / len(raycasts.rayons())
        rayon_actuel = 0
        for rayon in raycasts.rayons():
            if rayon.point_final() != 0:
                # Calculer les valeur nécessaire à l'objet
                objet_height = (1/rayon.point_final_distance()) * (surface.get_height())
                objet_y = surface.get_height() / 2.0 - objet_height / 2.0
                pygame.draw.rect(surface, (255, 0, 0), (rayon_actuel * largeur_rayon, objet_y, largeur_rayon, objet_height))
            rayon_actuel += 1

        return surface

    # Getters et setters
    def camera(self) -> Raycast_Camera:
        """Retourne la caméra utilisée dans le moteur Raycast

        Returns:
            Raycast_Camera: caméra utilisée dans le moteur Raycast
        """
        return self.__camera
    def hauteur_map(self) -> int:
        """Retourne la hauteur de la map

        Returns:
            int: hauteur de la map
        """
        return self.__hauteur_map