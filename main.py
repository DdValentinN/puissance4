
import random
from enum import Enum

# Couleurs des pions
class CouleurPion(Enum):
    JAUNE = 1
    ROUGE = 2

# Objet Pion
class Pion :
    # Construction d'un nouveau Pion
    def __init__(self,couleur_pion : CouleurPion):
        self.couleur_pion = couleur_pion

# Cet objet représente un joueur
class Joueur:
    # Création d'un attribut pour un joueur d'un TABLEAU de Pion : [Pion]
    # Par défaut le tableau est : vide
    pions_du_joueur: [Pion] = []

    # Construction d'un nouveau joueur
    def __init__(self, nom, couleur : CouleurPion):
        self.nom = nom
        self.couleur = couleur

    # Ajoute un pion au joueur
    def donner_pion (self, pion :Pion):
        self.pions_du_joueur.append(pion)

    # Prendre un pion dans la pile des pions du joueur
    def prendre_pion(self):
        return self.pions_du_joueur.pop()

class Case:
    pion_qui_est_contenu_dans_la_case : Pion = None
    def __init__(self, pion : Pion = None):
        self.pion_qui_est_contenu_dans_la_case = pion

    # On place un pion dans la case
    def placer_pion(self, pion : Pion):
        self.pion_qui_est_contenu_dans_la_case = pion
    # On récupère le pion qui est contenu dans la case
    def get_pion(self):
        if self.pion_qui_est_contenu_dans_la_case == None :
            return None
        else :
            return self.pion_qui_est_contenu_dans_la_case

class Game:
    joueurs: [Joueur]

    plateau_de_jeu = [
        [Case(), Case(), Case(), Case(), Case(), Case(), Case()],
        [Case(), Case(), Case(), Case(), Case(), Case(), Case()],
        [Case(), Case(), Case(), Case(), Case(), Case(), Case()],
        [Case(), Case(), Case(), Case(), Case(), Case(), Case()],
        [Case(), Case(), Case(), Case(), Case(), Case(), Case()],
        [Case(), Case(), Case(), Case(), Case(), Case(), Case()],
    ]

    # création d'un nouveau jeu
    def __init__(self, joueurs : [Joueur]):
        # On ajoute les joueurs au jeu en cours
        self.joueurs = joueurs

        # On place 21 pions dans la pioche des joueurs
        for joueur in self.joueurs:
            for i in range(21):
                joueur.donner_pion(Pion(joueur.couleur))

    # Permet de placer un pion dans une colonne
    def placer_pion_dans_colonne(self, pion : Pion, numero_colonne : int):
        # On va scanner de bas en haut le plateau de jeu
        # On prend ligne par ligne, et on :
        # - place le pion si la case est vide
        # - on remonte d'une ligne si la case est pleine
        for i in [5,4,3,2,1,0]:
            ligne = self.plateau_de_jeu[i]
            case = ligne[numero_colonne]
            if(case.pion_qui_est_contenu_dans_la_case == None):
                case.placer_pion(pion)
                return
        # Si on est ici, c'est que la colonne est full
        raise ValueError("La colonne est pleine mon coco")

    # Routine de jeu
    def jouer(self):
        i=0
        while self.qui_gagne== None:
            Joueur[i+1].placer_pion_dans_colonne()





        # tant qu'il n'y a pas de gagnant:
        while self.qui_gagne == None:
            print("Joueur 1 : A toi de jouer")


    # Fonction qui donne soit :
    # None si aucun joueur ne gagne
    # OU un Joueur qui est désigné gagnant
    def qui_gagne(self):
        for i in [5,4,3,2,1,0]:
            ligne = self.plateau_de_jeu[i]
            compteur_de_de_cases_de_la_couleur_rouge= 0
            compteur_de_de_cases_de_la_couleur_jaune = 0
            for case in ligne:
                if case.pion_qui_est_contenu_dans_la_case != None and case.pion_qui_est_contenu_dans_la_case.couleur_pion == CouleurPion.ROUGE:
                    compteur_de_de_cases_de_la_couleur_rouge += 1
                    compteur_de_de_cases_de_la_couleur_jaune = 0
                    if compteur_de_de_cases_de_la_couleur_rouge == 4:
                        return CouleurPion.ROUGE
                elif case.pion_qui_est_contenu_dans_la_case != None and case.pion_qui_est_contenu_dans_la_case.couleur_pion == CouleurPion.JAUNE:
                    compteur_de_de_cases_de_la_couleur_jaune += 1
                    compteur_de_de_cases_de_la_couleur_rouge = 0
                    if compteur_de_de_cases_de_la_couleur_jaune == 4:
                        return CouleurPion.JAUNE
        return None

# Création des joueurs
valentin = Joueur('Valentin', CouleurPion.JAUNE)
kevin = Joueur('Kévin', CouleurPion.ROUGE)

# Création d'un jeu Puissance 4
game = Game([valentin, kevin])

# On lance la routine de jeu
game.jouer()
