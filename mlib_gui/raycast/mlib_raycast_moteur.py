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
# Importer des outils de multi thread
import threading

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
        self.__hauteur = 1
        self.__numero_frame_dernier_rendu = 0
        self.__sous_map = []
        self.__x = x
        self.__y = y

    # Faire un rendu de la case
    def rendu(self, numero_frame__rendu: int) -> None:
        """Avertir la case qu'un rendu va être effectué"""
        self.__numero_frame_dernier_rendu = numero_frame__rendu

    # Getters et setters
    def contenu(self) -> Raycast_Materiel:
        """Retourne le contenu de la case

        Returns:
            int: contenu de la case
        """
        return self.__contenu
    def hauteur(self) -> float:
        """Retourne la hauteur du contenu d'une case

        Returns:
            float: hauteur du contenu d'une case
        """
        return self.__hauteur
    def numero_frame_dernier_rendu(self) -> int:
        """Returne le numéro de la frame du dernier rendu

        Returns:
            int: numéro de la frame du dernier rendu
        """
        return self.__numero_frame_dernier_rendu
    def x(self) -> int:
        """Retourne la coordonnées X de la case

        Returns:
            int: coordonnées X de la case
        """
        return self.__x
    def y(self) -> int:
        """Retourne la coordonnées Y de la case

        Returns:
            int: coordonnées Y de la case
        """
        return self.__y

#******************
#
# La classe "Raycast_Camera"
#
#******************

class Raycast_Camera(Transformation_3D):
    """Classe représentant la caméra du moteur Raycast"""

    # Constructeur de "Raycast_Camera"
    def __init__(self, raycast_moteur_structure: Raycast_Moteur_Structure, largeur_ecran: int) -> None:
        """Constructeur de "Raycast_Camera"

        Args:
            raycast_moteur_structure (Raycast_Moteur_Structure): structure du moteur raycast
        """
        super().__init__()

        # Définition des attributs
        self.__fov = 1
        self.__largeur_ecran = largeur_ecran
        self.__raycast_moteur_structure = raycast_moteur_structure
    
    # Getters et setters
    def fov(self) -> float:
        """Retourne le FOV de la caméra

        Returns:
            float: FOV de la caméra
        """
        return self.__fov
    def largeur_ecran(self) -> int:
        """Retourne la largeur de l'écran en pixel

        Returns:
            int: largeur de l'écran en pixel
        """
        return self.__largeur_ecran
    def set_fov(self, nouveau_fov: float) -> None:
        """Change le FOV de la caméra

        Args:
            nouveau_fov (float): nouveau FOV de la caméra
        """
        self.__fov = nouveau_fov

#******************
#
# La classe "Raycast_Moteur" et ses nécessités
#
#******************

class Raycast_Collision:
    """Classe représentant une collision dans un raycast"""

    # Constructeur de "Raycast_Collision"
    def __init__(self) -> None:
        """Constructeur de "Raycast_Collision"

        Returns:
            _type_: _description_
        """

        # Définition des attributs
        self.__case_entree = Point_3D()
        self.__case_entree_distance = -1
        self.__case_sortie = Point_3D()
        self.__case_sortie_distance = -1
        self.__case_touchee = 0
        self.__offset_x = 0
        self.__point_depart = 0

    # Getters et setters
    def case_entree(self) -> Point_3D:
        """Retourne l'entrée de la case du raycast

        Returns:
            Point_3D: entrée de la case du raycast
        """
        return self.__case_entree
    def case_entree_distance(self) -> float:
        """Retourne la distance de l'entrée de la case du raycast

        Returns:
            float: distance de l'entrée de la case du raycast
        """
        return self.__case_entree_distance
    def case_sortie(self) -> Point_3D:
        """Retourne la sortie de la case du raycast

        Returns:
            Point_3D: sortie de la case du raycast
        """
        return self.__case_sortie
    def case_sortie_distance(self) -> float:
        """Retourne la distance de la sortie de la case du raycast

        Returns:
            float: distance de la sortie de la case du raycast
        """
        return self.__case_sortie_distance
    def case_touchee(self) -> Raycast_Case:
        """Retourne la case touchée

        Returns:
            Raycast_Case: case touchée
        """
        return self.__case_touchee
    def offset_x(self) -> int:
        """Retourne l'offset X de la collision

        Returns:
            int: offset X de la collision
        """
        return self.__offset_x
    def point_depart(self) -> Point_3D:
        """Retourne le point de départ du raycast

        Returns:
            Point_3D: point de départ du raycast
        """
        return self.__point_depart
    def set_case_entree(self, nouveau_point: Point_3D, distance: float) -> None:
        """Change l'entrée de la case du raycast

        Argument:
            nouveau_point (Point_3D): nouvelle entrée de la case du raycast
            distance (float): distance au point final du raycast
        """
        self.__case_entree = nouveau_point
        self.__case_entree_distance = distance
    def set_case_sortie(self, nouveau_point: Point_3D, distance: float) -> None:
        """Change la sortie de la case du raycast

        Argument:
            nouveau_point (Point_3D): nouvelle sortie de la case du raycast
            distance (float): distance au point du raycast
        """
        self.__case_sortie = nouveau_point
        self.__case_sortie_distance = distance
    def set_case_touchee(self, nouvelle_case_touchee: Raycast_Case) -> None:
        """Change la valeur de la case touché

        Args:
            nouvelle_case_touchee (Raycast_Case): nouvelle valeur de la case touché
        """
        self.__case_touchee = nouvelle_case_touchee
    def set_offset_x(self, nouveau_offset_x: int) -> None:
        """Change la valeur d'offset de X

        Args:
            nouveau_offset_x (int): nouvelle valeur d'offset de X
        """
        self.__offset_x = nouveau_offset_x
    def set_point_depart(self, nouveau_point_depart: Point_3D) -> None:
        """Change le point de départ du raycast

        Arguments:
            nouveau_point_depart (Point_3D): nouveau point de départ du raycast
        """
        self.__point_depart = nouveau_point_depart

class Raycast:
    """Classe représentant un Raycast dans le moteur"""

    # Constructeur de "Raycast"
    def __init__(self, camera: Raycast_Camera) -> None:
        """Constructeur de "Raycast"
        """

        # Définition des attributs
        self.__angles_camera = []
        self.__camera = camera
        self.__collisions = []

    # Retourne les données d'avancement pour le raycast
    def avancement_donnees(self, indice: int = 0) -> tuple:
        """Retourne les données d'avancement pour le raycast

        Returns:
            tuple: données d'avancement pour le raycast
        """
        ajout_horizontal = 1
        ajout_vertical = 1
        ratio_horizontal = 1
        ratio_vertical = 1
        # Préparation des données du raycast horziontal
        avant = self.avant(indice)
        if avant.x() != 0:
            # Calcul des différences nécessaires
            ajout_horizontal = 1
            ratio_horizontal = abs(avant.y() / avant.x())
            if avant.x() < 0 and avant.y() < 0:
                ajout_horizontal = -ajout_horizontal
                ratio_horizontal = -ratio_horizontal
            elif avant.y() < 0: ratio_horizontal = -ratio_horizontal
            elif avant.x() < 0: ajout_horizontal = -ajout_horizontal
        # Préapartion des données du raycast vertical
        if avant.y() != 0:
            # Calcul des différences nécessaires
            ajout_vertical = 1
            ratio_vertical = abs(avant.x() / avant.y())
            if avant.x() < 0 and avant.y() < 0:
                ajout_vertical = -ajout_vertical
                ratio_vertical = -ratio_vertical
            elif avant.x() < 0: ratio_vertical = -ratio_vertical
            elif avant.y() < 0: ajout_vertical = -ajout_vertical
        return (ajout_horizontal, ajout_vertical, ratio_horizontal, ratio_vertical)
    # Élimine les raycasts duplicants
    def ranger_collisions(self) -> None:
        """Élimine les raycasts duplicants"""

        # Tri les collisions
        self.__collisions = sorted(self.__collisions, key=lambda collision: collision.case_entree_distance())

    # Getters et setter
    def angle_camera(self, indice: int) -> float:
        """Retourne un angle de caméra utilisé dans le raycast

        Args:
            indice (int): indice de l'angle nécessaire

        Returns:
            float: _desangle de caméra utilisé dans le raycastcription_
        """
        return self.angles_camera()[indice]
    def angles_camera(self) -> list:
        """Retourne les angles de caméra utilisé dans le raycast

        Returns:
            float: les angles de caméra utilisé dans le raycast
        """
        return self.__angles_camera
    def avant(self, indince: int = 0) -> Point_3D:
        """Retourne le vecteur avant dans le raycast

        Returns:
            Point_3D: vecteur avant dans le raycast
        """
        return self.camera().devant_normalise(self.angle_camera(indince))
    def camera(self) -> Raycast_Camera:
        """Retourne la caméra utilisé par le raycast

        Returns:
            Raycast_Camera: caméra utilisé par le raycast
        """
        return self.__camera
    def collisions(self) -> list:
        """Retourne la liste des collisions dans le raycast

        Returns:
            list: liste des collisions dans le raycast
        """
        return self.__collisions
    def point_depart(self) -> Point_3D:
        """Retourne le point de départ du raycast

        Returns:
            Point_3D: point de départ du raycast
        """
        return self.__camera
    def set_avant(self, nouveau_avant: Point_3D) -> None:
        """Change le vecteur avant dans le raycast

        Argument:
            nouveau_avant (Point_3D): nouveau vecteur avant dans le raycast
        """
        self.__avant = nouveau_avant
    def set_point_depart(self, nouveau_point_depart: Point_3D) -> None:
        """Change le point de départ du raycast

        Arguments:
            nouveau_point_depart (Point_3D): nouveau point de départ du raycast
        """
        self.__point_depart = nouveau_point_depart

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
    def nombre_rayons(self) -> int:
        """Retourne le nombre de rayons dans le raycast

        Returns:
            int: nombre de rayons dans le raycast
        """
        return len(self.rayons())
    def point_depart(self) -> Point_3D:
        """Retourne le point de départ des raycasts

        Returns:
            Point_3D: point de départ des raycasts
        """
        return self.__point_depart
    def rayons(self) -> list:
        """Retourne la liste de rayons générés

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
        """Constructeur de "Raycast_Moteur"""
        super().__init__(structure_plus)

        # Définition des attributs
        self.__camera = Raycast_Camera(self, 400)
        self.__couleur_arriere_plan = (0, 128, 255)
        self.__hauteur_map = 0
        self.__largeur_map = 0
        self.__map = []
        self.__objets_dynamiques = []

    # Retourne une case selon deux coordonnées
    def case(self, x_case: int, y_case: int) -> Raycast_Case:
        """Retourne une case selon deux coordonnées

        Args:
            x_case (int): X de la case à retourner
            y_case (int): y de la case à retourner

        Returns:
            Raycast_Case: case à retourner
        """
        x_case = floor(x_case)
        y_case = floor(y_case)
        if self.dans_map(x_case, y_case):
            return self.__map[y_case][x_case]
        return 0
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

    # Crée et retourne un nouvel objet dynamique avec son bon type
    def nouvel_objet_dynamique_createur(self, nom: str, type: str) -> Raycast_Objet_Dynamique:
        """Crée et retourne un nouvel objet dynamique avec son bon type

        Args:
            nom (str): nom de l'objet à créer
            type (str): type de l'objet à créer

        Returns:
            Raycast_Objet_Dynamique: objet crée
        """
        return Raycast_Objet_Dynamique(self, nom)
    # Crée et retourne un nouvel objet dynamique
    def nouvel_objet_dynamique(self, nom: str, type: str) -> Raycast_Objet_Dynamique:
        """Crée et retourne un nouvel objet dynamique

        Args:
            nom (str): nom de l'objet dynamique
            type (str): type de l'objet dynamique

        Returns:
            Raycast_Objet_Dynamique: objet dynamique crée (ou 0 si création impossible)
        """

        if self.objet_dynamique_par_nom(nom) == 0:
            # Création de l'objet dynamique
            nouvel_objet = self.nouvel_objet_dynamique_createur(nom, type)
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

    # Ajoute une collision au raycast
    def __raycast_appliquer_difference_horizontale(self, point: Point_3D, ajout_horizontal: float, ratio_horizontal: float) -> None:
        """Applique une différence nécessaire dans la map pour le raycast

        Args:
            point (Point_3D): point auquel appliquer la différence
        """
        # Nouvelle position
        x_actuel = ceil(point.x())
        if ajout_horizontal < 0: x_actuel = floor(point.x())
        difference_x = abs(x_actuel - point.x())
        y_actuel = point.y() + difference_x * ratio_horizontal
        # Appliquer les modifications
        point.set_x(x_actuel)
        point.set_y(y_actuel)
    def __raycast_appliquer_difference_verticale(self, point: Point_3D, ajout_vertical: float, ratio_vertical: float) -> None:
        """Applique une différence nécessaire dans la map pour le raycast

        Args:
            point (Point_3D): point auquel appliquer la différence
        """
        # Nouvelle position
        y_actuel = ceil(point.y())
        if ajout_vertical < 0: y_actuel = floor(point.y())
        difference_y = abs(y_actuel - point.y())
        x_actuel = point.x() + difference_y * ratio_vertical
        # Appliquer les modifications
        point.set_x(x_actuel)
        point.set_y(y_actuel)
    def __raycast_avancement_donnees(self, point_depart: Point_3D, point_arrive: Point_3D) -> tuple:
        """Retourne quelques données sur la façon dont le rayon doit avancer

        Returns:
            tuple: quelques données sur la façon dont le rayon doit avancer
        """
        ajout_horizontal = 1
        ajout_vertical = 1
        ratio_horizontal = 1
        ratio_vertical = 1
        # Préparation des données du raycast horziontal
        avant = point_arrive.copie()
        avant -= point_depart
        if avant.x() != 0:
            # Calcul des différences nécessaires
            ajout_horizontal = 1
            ratio_horizontal = abs(avant.y() / avant.x())
            if avant.x() < 0 and avant.y() < 0:
                ajout_horizontal = -ajout_horizontal
                ratio_horizontal = -ratio_horizontal
            elif avant.y() < 0: ratio_horizontal = -ratio_horizontal
            elif avant.x() < 0: ajout_horizontal = -ajout_horizontal
        # Préapartion des données du raycast vertical
        if avant.y() != 0:
            # Calcul des différences nécessaires
            ajout_vertical = 1
            ratio_vertical = abs(avant.x() / avant.y())
            if avant.x() < 0 and avant.y() < 0:
                ajout_vertical = -ajout_vertical
                ratio_vertical = -ratio_vertical
            elif avant.x() < 0: ratio_vertical = -ratio_vertical
            elif avant.y() < 0: ajout_vertical = -ajout_vertical
        return (ajout_horizontal, ajout_vertical, ratio_horizontal, ratio_vertical)
    def __raycast_nouvelle_collision(self, raycast_entier: Raycast_Entier, raycast: Raycast, offset_x: int, case_touchee: Raycast_Case, point_touche: Point_3D, point_touche_distance: float, sens_arrive: int, donnees_raycast: tuple) -> None:
        """Ajoute une collision au raycast

        Arguments:
            raycast (Raycast): raycast auquel ajouté une collision
            case_touchee (Raycast_Case): case touchée par la collision
            point_touche (Raycast_Case): point touché par la collision
            point_touche_distance (float): distance entre le point de la collision et l'envoyeur du rayon 
            sens_arrive (int): sens d'arrivé de la collision (0 = horizontal, 1 = vertical)
            donnees_raycast (tuple): autres données secondaires sur le raycast
        """

        # Préparer la création de la collision
        ajout_horizontal = donnees_raycast[0]
        ajout_vertical = donnees_raycast[1]
        point_actuel = point_touche.copie()
        ratio_horizontal = donnees_raycast[2]
        ratio_vertical = donnees_raycast[3]

        # Créer la collision
        raycast_actuel = Raycast_Collision()
        raycast_actuel.set_case_touchee(case_touchee)
        raycast_actuel.set_case_entree(point_actuel.copie(), point_touche_distance)
        raycast_actuel.set_offset_x(offset_x)
        raycast_actuel.set_point_depart(raycast_entier.point_depart())

        # Préparer la recherche de la sortie
        distance_horizontale_sortie = -1
        distance_verticale_sortie = -1
        point_de_depart = raycast_actuel.point_depart()
        point_horizontal_sortie = point_touche.copie()
        point_vertical_sortie = point_touche.copie()
        if case_touchee != 0:
            # Modifier les coordonnées comme nécessaire
            if sens_arrive == 0:
                # Tester l'axe horizontal
                point_horizontal_sortie.set_x(point_horizontal_sortie.x() + ajout_horizontal)
                point_horizontal_sortie.set_y(point_horizontal_sortie.y() + ratio_horizontal)
                distance_horizontale_sortie = distance(point_de_depart, point_horizontal_sortie)

                # Tester l'axe vertical
                self.__raycast_appliquer_difference_verticale(point_vertical_sortie, ajout_vertical, ratio_vertical)
                case_verticale = self.case(point_horizontal_sortie.x(), point_horizontal_sortie.y())
                if case_verticale != 0 and case_verticale != case_touchee: distance_verticale_sortie = distance(point_de_depart, point_vertical_sortie)
            else:
                # Tester l'axe vertical
                point_vertical_sortie.set_x(point_vertical_sortie.x() + ratio_vertical)
                point_vertical_sortie.set_y(point_vertical_sortie.y() + ajout_vertical)
                distance_verticale_sortie = distance(point_de_depart, point_vertical_sortie)

                # Tester l'axe horizontal
                self.__raycast_appliquer_difference_horizontale(point_horizontal_sortie, ajout_horizontal, ratio_horizontal)
                case_horizontale = self.case(point_horizontal_sortie.x(), point_horizontal_sortie.y())
                if case_horizontale != 0 and case_horizontale != case_touchee: distance_horizontale_sortie = distance(point_de_depart, point_horizontal_sortie)
                    
        # Préparer le point de sortie
        if distance_horizontale_sortie <= -1:
            raycast_actuel.set_case_sortie(point_vertical_sortie, distance_verticale_sortie)
        elif distance_verticale_sortie <= -1:
            raycast_actuel.set_case_sortie(point_horizontal_sortie, distance_horizontale_sortie)
        elif distance_verticale_sortie <= distance_horizontale_sortie:
            raycast_actuel.set_case_sortie(point_vertical_sortie, distance_verticale_sortie)
        else:
            raycast_actuel.set_case_sortie(point_horizontal_sortie, distance_horizontale_sortie)

        # Ajoute la collision
        raycast.collisions().append(raycast_actuel)
    def __raycast_case(self, raycast_entier: Raycast_Entier, case: Raycast_Case) -> None:
        """Réalise un raycast pour une case entière"""

        # Vérifier si le rendu doit être fait
        if case.numero_frame_dernier_rendu() == self.structure_plus().numero_frame(): return
        case.rendu(self.structure_plus().numero_frame())

        # Calculer les valeurs nécessaires pour la case
        point_case = Point_3D()
        point_case_fin = Point_3D()
        point_case_milieu = Point_3D()
        if case.x() > self.camera().x():
            point_case.set_x(case.x())
            point_case_fin.set_x(case.x() + 1)
            point_case_milieu.set_x(case.x())
            if case.y() > self.camera().y():
                point_case.set_y(case.y() + 1)
                point_case_fin.set_y(case.y())
                point_case_milieu.set_y(case.y())

        # Calcul l'angle pour la case
        angle_case = -angle(self.camera() + self.camera().devant_normalise(), self.camera(), point_case)
        angle_case_fin = -angle(self.camera() + self.camera().devant_normalise(), self.camera(), point_case_fin)
        angle_case_milieu = -angle(self.camera() + self.camera().devant_normalise(), self.camera(), point_case_milieu)
        angle_total_face_1 = abs(angle_case_milieu - angle_case)
        angle_total_face_2 = abs(angle_case_fin - angle_case_milieu)
        angle_pixel = self.camera().fov() / self.camera().largeur_ecran()
        angle_start = round(((angle_case + self.camera().fov() / 2.0) / self.camera().fov()) / angle_pixel)
        number_pixels_face_1 = round(angle_total_face_1 / angle_pixel)
        number_pixels_face_2 = round(angle_total_face_2 / angle_pixel)
        nombre_pixels_total = number_pixels_face_1 + number_pixels_face_2
        rayon_par_pixel = floor(self.camera().largeur_ecran() / raycast_entier.nombre_rayons())

        if number_pixels_face_1 >= 1:
            # Calcul des collisions nécessaires pour la première face
            point_actuel = point_case.copie()
            distance_actuelle = 0
            for i in range(angle_start, angle_start + number_pixels_face_1 + 1):
                if i < 0:
                    # Modifier le point actuel
                    point_actuel.set_y(point_actuel.y() - 1.0/number_pixels_face_1)
                    continue
                if i >= self.camera().largeur_ecran(): break
                # Appliquer la collision
                donnees_raycast = self.__raycast_avancement_donnees(self.camera(), point_actuel)
                distance_actuelle = distance(self.camera(), point_actuel)
                offset_actuel = i % rayon_par_pixel
                rayon_actuel = floor(i / rayon_par_pixel)
                raycast_actuel = raycast_entier.rayons()[rayon_actuel]
                self.__raycast_nouvelle_collision(raycast_entier, raycast_actuel, offset_actuel, case, point_actuel, distance_actuelle, 0, donnees_raycast)

                # Modifier le point actuel
                point_actuel.set_y(point_actuel.y() - 1.0/number_pixels_face_1)

        if number_pixels_face_2 >= 1:
            # Calcul des collisions nécessaires pour la deuxième face
            point_actuel = point_case_milieu.copie()
            for i in range(angle_start + number_pixels_face_1 - 1, angle_start + nombre_pixels_total):
                if i < 0:
                    # Modifier le point actuel
                    point_actuel.set_x(point_actuel.x() + 1.0/number_pixels_face_2)
                    continue
                if i >= self.camera().largeur_ecran(): break
                # Appliquer la collision
                donnees_raycast = self.__raycast_avancement_donnees(self.camera(), point_actuel)
                distance_actuelle = distance(self.camera(), point_actuel)
                offset_actuel = i % rayon_par_pixel
                rayon_actuel = floor(i / rayon_par_pixel)
                raycast_actuel = raycast_entier.rayons()[rayon_actuel]
                self.__raycast_nouvelle_collision(raycast_entier, raycast_actuel, offset_actuel, case, point_actuel, distance_actuelle, 1, donnees_raycast)

                # Modifier le point actuel
                point_actuel.set_x(point_actuel.x() + 1.0/number_pixels_face_2)
    def __raycast_position_pleine(self, raycast_entier: Raycast_Entier, x_a_tester: float, y_a_tester: float) -> bool:
        """Gère si une certaine position dans un raycast contient une case afficahble ou non

        Args:
            point (Point_3D): position à tester
        """
        if self.dans_map(x_a_tester, y_a_tester):
            if self.__map[y_a_tester][x_a_tester] != 0 and self.__map[y_a_tester][x_a_tester].contenu() != 0:
                self.__raycast_case(raycast_entier, self.__map[y_a_tester][x_a_tester])
    def raycast(self, raycast_entier: Raycast_Entier, final: Raycast, point_de_depart: Transformation_3D, angle_ajuste: float = 0) -> None:
        """Réalise et retourne un résultat de raycast

        Argument:
            point_de_depart (Transformation_3D): point de départ du rayon

        Returns:
            Raycast: résultat de raycast
        """

        # Préparation des raycast
        avant = point_de_depart.devant_normalise(angle_ajuste)
        final.set_avant(avant)

        # Préaparation des données pour le raycast
        ajout_horizontal, ajout_vertical, ratio_horizontal, ratio_vertical = final.avancement_donnees()

        # Réalisation du raycast vertical
        point_vertical = point_de_depart.copie()
        if avant.y() != 0:
            # Départ vers le début réel du raycast
            self.__raycast_appliquer_difference_verticale(point_vertical, ajout_vertical, ratio_vertical)
            
            # Premier test de la map
            x_a_tester = floor(point_vertical.x())
            y_a_tester = floor(point_vertical.y())
            if ajout_vertical > 0: y_a_tester = floor(point_vertical.y()) + 1
            self.__raycast_position_pleine(raycast_entier, x_a_tester, y_a_tester)
            # Envoie du rayon
            while self.dans_map_point(point_vertical):
                # Nouvelle position
                x_actuel = point_vertical.x() + ratio_vertical
                y_actuel = point_vertical.y() + ajout_vertical
                point_vertical.set_x(x_actuel)
                point_vertical.set_y(y_actuel)

                # Gérer la map
                x_a_tester = floor(x_actuel)
                y_a_tester = floor(y_actuel)
                if ajout_vertical > 0: y_a_tester = floor(y_actuel) + 1
                self.__raycast_position_pleine(raycast_entier, x_a_tester, y_a_tester)

        # Réalisation du raycast horizontal
        point_horizontal = point_de_depart.copie()
        if avant.x() != 0:
            # Départ vers le début réel du raycast
            self.__raycast_appliquer_difference_horizontale(point_horizontal, ajout_horizontal, ratio_horizontal)
            
            # Premier test de la map
            x_a_tester = floor(point_horizontal.x()) - 1
            if ajout_horizontal > 0: x_a_tester = floor(point_horizontal.x())
            y_a_tester = ceil(point_horizontal.y())
            self.__raycast_position_pleine(raycast_entier, x_a_tester, y_a_tester)
            # Envoie du rayon
            while self.dans_map_point(point_horizontal):
                # Nouvelle position
                x_actuel = point_horizontal.x() + ajout_horizontal
                y_actuel = point_horizontal.y() + ratio_horizontal
                point_horizontal.set_x(x_actuel)
                point_horizontal.set_y(y_actuel)

                # Gérer la map
                x_a_tester = floor(x_actuel) - 1
                if ajout_horizontal > 0: x_a_tester = floor(x_actuel)
                y_a_tester = ceil(y_actuel)
                self.__raycast_position_pleine(raycast_entier, x_a_tester, y_a_tester)
    # Effectue l'entiéreté des raycasts nécessaires à un rendu
    def __raycast_entier_un(self, raycast_entier: Raycast_Entier, i_start: int, fov: float, nombre_rayons: int, nombre_raycast: int = 20, largeur_ecran: int = 100):
        """Effectue un raycast pour le raycast en multithread"""
        for i in range(nombre_raycast):
            self.raycast(raycast_entier, raycast_entier.rayons()[i], self.camera(), fov / 2.0 - (i + i_start) * ((fov)/nombre_rayons))
    def raycast_entier(self, nombre_rayons: int = 100, nombre_thread: int= 0, largeur_ecran: int = 100) -> Raycast_Entier:
        """Retourne les données sur l'entiéreté des raycasts nécessaires à un rendu

        Argument:
            nombre_rayons(int): nombre de rayons produits par le raycast

        Returns:
            Raycast_Entier: données sur l'entiéreté des raycasts nécessaires à un rendu
        """

        # Configurer le Raycast_Entier
        angle_actuel = -self.camera().fov() / 2.0
        pixels_par_rayon = int(largeur_ecran / nombre_rayons)
        raycasts = Raycast_Entier()
        raycasts.set_point_depart(self.camera())
        for i in range(nombre_rayons):
            # Créer le raycast
            raycast_actuel = Raycast(self.camera())
            raycasts.rayons().append(raycast_actuel)
            for j in range(pixels_par_rayon):
                raycast_actuel.angles_camera().append(angle_actuel)
                angle_actuel += self.camera().fov() / largeur_ecran

        if nombre_thread > 0:
            # Création des threads nécessaires
            rayons_par_thread = int(nombre_rayons / nombre_thread)
            tous_les_threads = []
            for i in range(nombre_thread):
                tous_les_raycasts = []
                thread = threading.Thread(target=self.__raycast_entier_un, args=(raycasts, tous_les_raycasts, i * rayons_par_thread, self.camera().fov(), nombre_rayons))
                thread.start()
                tous_les_threads.append(thread)
                tous_les_threads.append(tous_les_raycasts)
            
            # Ajoute l'entiéreté des rayons
            nb_raycast = 0
            for thread in tous_les_threads:
                if type(thread) == threading.Thread:
                    thread.join()
                else:
                    for raycast in thread:
                        raycasts.rayons()[nb_raycast] = raycast
                        nb_raycast += 1
        else: self.__raycast_entier_un(raycasts, 0, self.camera().fov(), nombre_rayons, nombre_rayons, largeur_ecran)

        # Terminer la recherche de collisions
        for rayon in raycasts.rayons():
            rayon.ranger_collisions()
        
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
            pygame.draw.circle(surface, (0, 255, 0), (x_objet, y_objet), 4)
            
            # Dessiner les rayons de raycast
            raycasts = self.raycast_entier()
            for rayon in raycasts.rayons():
                if len(rayon.collisions()) > 0:
                    x_objet, y_objet = raycasts.point_depart().x() * largeur_case, surface.get_height() - raycasts.point_depart().y() * largeur_case
                    x_devant, y_devant = rayon.collisions()[0].case_entree().x() * largeur_case, surface.get_height() - rayon.collisions()[0].case_entree().y() * largeur_case
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
        largeur_ecran = self.camera().largeur_ecran()
        raycasts = self.raycast_entier(50, 0, largeur_ecran)
        surface = pygame.Surface((largeur_ecran, largeur_ecran))
        surface.fill(self.couleur_arriere_plan())

        # Calcul de l'horizon
        horizon_y = (surface.get_height() / 2.0) * (3.1415 / self.camera().rotation_x())
        if(floor(horizon_y) < surface.get_height()):
            surface.blit(self.texture_bas_rendu_3D(surface.get_width(), surface.get_height() - floor(horizon_y)), (0, floor(horizon_y)))

        # Dessiner chaque rayon
        largeur_rayon = int(surface.get_width() / len(raycasts.rayons()))
        rayon_actuel = 0
        for rayon in raycasts.rayons():
            if len(rayon.collisions()) > 0:
                # Calculer les valeur nécessaire à l'objet selon un rayon
                for collision_actuelle in rayon.collisions()[::-1]:
                    objet_hauteur = (1/collision_actuelle.case_entree_distance()) * (surface.get_height())
                    objet_y = ceil(horizon_y - (objet_hauteur / 2.0) * (1 - self.camera().z()))
                    if objet_y < 0 : continue
                    # Dessiner le toit si nécessaire
                    if objet_y > horizon_y and collision_actuelle.case_sortie_distance() != -1:
                        autre_cote_hauteur = (1/collision_actuelle.case_sortie_distance()) * (surface.get_height())
                        autre_cote_y = floor(horizon_y - (autre_cote_hauteur / 2.0) * (1 - self.camera().z()))
                        pygame.draw.rect(surface, (255, 0, 0), (rayon_actuel * largeur_rayon + collision_actuelle.offset_x(), autre_cote_y, 1, objet_y - autre_cote_y))
                    # Optimiser le traçage
                    if objet_y + objet_hauteur > surface.get_height():
                        objet_hauteur += surface.get_height() - objet_y
                    pygame.draw.rect(surface, (180, 0, 0), (rayon_actuel * largeur_rayon + collision_actuelle.offset_x(), objet_y, 1, objet_hauteur))
            rayon_actuel += 1

        return surface
    
    # Retourne la texture en bas d'un rendu 3D
    def texture_bas_rendu_3D(self, longueur_jeu: int, hauteur_horizon: int) -> pygame.Surface:
        """Retourne la texture en bas d'un rendu 3D

        Argument:
            longueur_jeu (int): longueur de l'écran de jeu en pixel
            hauteur_horizon (int): hauteur de l'horizon de jeu en pixel

        Returns:
            pygame.Surface: texture en bas d'un rendu 3D
        """

        # Créer la texture
        longueur_jeu = longueur_jeu
        texture = pygame.Surface((longueur_jeu, hauteur_horizon))
        texture.fill((0, 0, 255))

        return texture

    # Getters et setters
    def camera(self) -> Raycast_Camera:
        """Retourne la caméra utilisée dans le moteur Raycast

        Returns:
            Raycast_Camera: caméra utilisée dans le moteur Raycast
        """
        return self.__camera
    def couleur_arriere_plan(self) -> tuple:
        """Retourne la couleur d'arrière plan d'un rendu 3D

        Returns:
            tuple: couleur d'arrière plan d'un rendu 3D
        """
        return self.__couleur_arriere_plan
    def hauteur_map(self) -> int:
        """Retourne la hauteur de la map

        Returns:
            int: hauteur de la map
        """
        return self.__hauteur_map