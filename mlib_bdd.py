#******************
#
# mlib_bdd.py
#
#******************
# Presentation :
#
# MLib Super est la dernière version du problej "MLib".
# Elle est réalisé pour le projet "Trophées NSI", pour faciliter la création de Software.
#
# Ce fichier contient des outils de simplification pour l'utilisation de bases de données.
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

# Importer sqlite3 pour utiliser les bases de données .db
import sqlite3

#******************
#
# La classe "Base_De_Donnees"
#
#******************

class Base_De_Donnees:
    """Classe représentant une base de données"""

    def __init__(self, chemin_acces: str) -> None:
        """Constructeur de "Base_De_Donnees"

        Arguments:
            chemin_acces (str): chemin d'accès de la base de données
        """

        # Définition des attributs
        self.__connection = sqlite3.connect(chemin_acces)
    def __del__(self) -> None:
        """Destructeur de "Base_De_Donnees"""
        self.__connection.close()

    def creer_table(self, nom_table: str, attributs_table: tuple) -> None:
        """Créer une table dans le .db

        Args:
            nom_table (str): nom de la table à créer
            attributs_table (tuple): attributs de la table à créer
        """

        # Créer la requête nécessaire
        #if(self.contient_table(nom_table)): return
        commande = "CREATE TABLE IF NOT EXISTS " + nom_table + "(\n"
        types = {"float": "FLOAT", "int": "INT", "str": "VARCHAR(100)"}
        for attribut in attributs_table:
            commande += attribut[0] + " " + types[attribut[1]] + ",\n"
        commande = commande[:len(commande) - 2] + "\n)\n"
        # Effectueur la commande nécessaire
        self.connection().execute(commande)
        self.connection().commit()

    # Getters et setters
    def connection(self) -> sqlite3.Connection:
        """Retourne la connection de cette base de données

        Returns:
            sqlite3.Connection: connection de cette base de données
        """
        return self.__connection