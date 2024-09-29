#******************
#
# mlib_window.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient la classe "Fenetre", et tout le nécessaire pour l'utiliser.
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

# Importer MLib_Objet pour utiliser les objets MLib
from mlib_objet import *
# Importer MLib_Raycast pour utiliser le raycast MLib
from mlib_raycast import *
# Importer MLib_Structure_Plus pour utiliser la structure avancée de la fenêtre
from mlib_structure_plus import *
# Importer time_ns pour le calcul du delta time
from time import time_ns

#******************
#
# La classe "Fenetre"
#
#******************

class Fenetre(Structure_Plus) :
    """Classe représentant une fenêtre MLib"""
    
    def __init__(self, largeur: int, hauteur: int) -> None:
        """Constructeur de "Fenetre"

        Arguments:
            largeur (int): Largeur de la fenêtre
            hauteur (int): Hauteur de la fenêtre
        """
        super().__init__()

        # Définition des attributs de base
        self.__continue = True
        self.__couleur_arriere_plan = (255, 255, 255)
        self.__dernier_fps = 0
        self.__hauteur = hauteur
        self.__ecran = 0
        self.__enfants = []
        self.__evenements = 0
        self.__frame_depuis_dernier_fps = 0
        self.__largeur = largeur
        self.__temps_depuis_dernier_fps = 0

        # Mise en place de Pygame
        pygame.init()
        self.__ecran = pygame.display.set_mode((largeur, hauteur))

    def __del__(self) -> None:
        """Destructeur de "Fenetre"""
        self.__enfants.clear()

    # Gérer les touches pendant un évènement
    def __maj_evenements_touche(self, touche: str, type: int) -> None:
        """Gérer les touches pendant un évènement
        
        Argument:
            touche (str): touche à gérer
            type (int): type d'évènement
        """
        if type == pygame.KEYDOWN:
            self.touches_etats()[touche] = 1
        else:
            self.touches_etats().pop(touche)
    # Gérer les évènements
    def maj_evenements(self) -> None :
        """Fonction exécutée avant chaque mise à jour de la fenêtre, pour gérer les évènements"""

        # Gérer le delta time et les FPS
        if self.dernier_delta_time() != 0: self.set_delta_time((time_ns() - self.dernier_delta_time()) / pow(10, 9))
        self.set_dernier_delta_time(time_ns())
        self.__temps_depuis_dernier_fps += self.delta_time()
        if self.__temps_depuis_dernier_fps > 1:
            self.__dernier_fps = self.__frame_depuis_dernier_fps
            self.__frame_depuis_dernier_fps = 0
            self.__temps_depuis_dernier_fps -= 1
            print("FPS :", self.__dernier_fps)
        self.__frame_depuis_dernier_fps += 1
        super().maj_evenements()

        # On navigue dans chaques évènements
        self.__evenements = pygame.event.get()
        for evenement in self.__evenements:
            if evenement.type == pygame.KEYDOWN or evenement.type == pygame.KEYUP:
                # Une touche du clavier est pressée ou relachée
                if evenement.key == pygame.K_a: self.__maj_evenements_touche("a", evenement.type)
                elif evenement.key == pygame.K_b: self.__maj_evenements_touche("b", evenement.type)
                elif evenement.key == pygame.K_c: self.__maj_evenements_touche("c", evenement.type)
                elif evenement.key == pygame.K_d: self.__maj_evenements_touche("d", evenement.type)
                elif evenement.key == pygame.K_e: self.__maj_evenements_touche("e", evenement.type)
                elif evenement.key == pygame.K_f: self.__maj_evenements_touche("f", evenement.type)
                elif evenement.key == pygame.K_g: self.__maj_evenements_touche("g", evenement.type)
                elif evenement.key == pygame.K_h: self.__maj_evenements_touche("h", evenement.type)
                elif evenement.key == pygame.K_i: self.__maj_evenements_touche("i", evenement.type)
                elif evenement.key == pygame.K_j: self.__maj_evenements_touche("j", evenement.type)
                elif evenement.key == pygame.K_k: self.__maj_evenements_touche("k", evenement.type)
                elif evenement.key == pygame.K_l: self.__maj_evenements_touche("l", evenement.type)
                elif evenement.key == pygame.K_m: self.__maj_evenements_touche("m", evenement.type)
                elif evenement.key == pygame.K_n: self.__maj_evenements_touche("n", evenement.type)
                elif evenement.key == pygame.K_o: self.__maj_evenements_touche("o", evenement.type)
                elif evenement.key == pygame.K_p: self.__maj_evenements_touche("p", evenement.type)
                elif evenement.key == pygame.K_q: self.__maj_evenements_touche("q", evenement.type)
                elif evenement.key == pygame.K_r: self.__maj_evenements_touche("r", evenement.type)
                elif evenement.key == pygame.K_s: self.__maj_evenements_touche("s", evenement.type)
                elif evenement.key == pygame.K_t: self.__maj_evenements_touche("t", evenement.type)
                elif evenement.key == pygame.K_u: self.__maj_evenements_touche("u", evenement.type)
                elif evenement.key == pygame.K_v: self.__maj_evenements_touche("v", evenement.type)
                elif evenement.key == pygame.K_w: self.__maj_evenements_touche("w", evenement.type)
                elif evenement.key == pygame.K_x: self.__maj_evenements_touche("x", evenement.type)
                elif evenement.key == pygame.K_y: self.__maj_evenements_touche("y", evenement.type)
                elif evenement.key == pygame.K_z: self.__maj_evenements_touche("z", evenement.type)
                elif evenement.key == pygame.K_LEFT: self.__maj_evenements_touche("fg", evenement.type)
                elif evenement.key == pygame.K_RIGHT: self.__maj_evenements_touche("fd", evenement.type)
                elif evenement.key == pygame.K_UP: self.__maj_evenements_touche("fh", evenement.type)
                elif evenement.key == pygame.K_DOWN: self.__maj_evenements_touche("fb", evenement.type)
                elif evenement.key == pygame.K_SPACE: self.__maj_evenements_touche("espace", evenement.type)
                elif evenement.key == pygame.K_LSHIFT: self.__maj_evenements_touche("shift", evenement.type)
            elif evenement.type == pygame.QUIT:
                # On repère l'évènement pour quitter le programme
                self.__continue = False

        # Appliquer les évènements graphiques de base
        self.__ecran.fill(self.__couleur_arriere_plan)

    # Gérer le rendu
    def maj_rendu(self) -> None:
        """Fonction exécutée pour mettre la fenêtre graphique à jour"""

        # Ajoute chaque enfants sur la surface
        for enfant in self.__enfants:
            enfant.maj_rendu(self.__ecran)

        # On affiche l'écran
        pygame.display.flip()

    def nouvel_enfant_createur(self, nom: str, type: str) -> Objet:
        """Crée l'enfant, avec le type nécessaire selon "type

        Args:
            nom (str): Nom de l'enfant
            type (str): Type de l'enfant

        Returns:
            Objet: Enfant crée
        """

        # Création d'un texte
        if type == "text" or type == "texte": return Texte(self, nom)
        # Création d'une fenêtre Raycast
        elif type == "raycast": return Raycast_Fenetre(self, nom)

        # Création avec le type de base
        return Objet(self, nom)

    def nouvel_enfant(self, nom: str, type: str, x: int, y: int, largeur: int, hauteur: int) -> Objet:
        """Crée et retourne un nouvel enfant dans la fenêtre

        Arguments:
            nom (str): Nom du nouvel enfant
            x (int): Position X du nouvel enfant
            y (int): Position Y du nouvel enfant
            largeur (int): Largeur du nouvel enfant
            hauteur (int): Hauteur du nouvel enfant

        Retour:
            Objet: Objet crée
        """

        # Création de l'enfant
        nouvel_objet = self.nouvel_enfant_createur(nom, type)
        nouvel_objet.set_hauteur(hauteur)
        nouvel_objet.set_largeur(largeur)
        nouvel_objet.set_x(x)
        nouvel_objet.set_y(y)
        self.__enfants.append(nouvel_objet)

        return nouvel_objet
    # Crée et retourne un moteur raycast pour la fenêtre
    def nouveau_raycast(self) -> Raycast_Moteur:
        """Crée et retourne un moteur raycast pour la fenêtre

        Returns:
            Raycast_Moteur: moteur raycast crée
        """
        return Raycast_Moteur(self)

    # Getters et setters
    def continuer(self) -> bool:
        """Retourne si la classe continue de marcher"""
        return self.__continue