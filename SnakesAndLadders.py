from Joueur import Joueur
from Plateau import Plateau
from BonusType import BonusType
from random import randrange

nbBonus = int(input("Nombre de bonus : "))
nbJoueur = int(input("Saisissez le nombre de joueur : "))
listJoueur = []

for i in range(0,nbJoueur):
    listJoueur.append(Joueur(input("Nom du joueur " + str(i+1) + " : ")))

print("\n")

partieGagne = False
gagnant = None
Plateau = Plateau(nbBonus)
replay = False
tour = 0

while not partieGagne:
    j = listJoueur[tour % nbJoueur]

    print("*** Tour de " + j.name + " ***")
    print("Lancer les dés ... : ", end="")
    input()

    lancerDe = randrange(1,6)
    print(str(lancerDe))

    tmpPos = j.pos + lancerDe

    if tmpPos > 100:
        print("Il faut faire " + str(100 - j.pos) + " pour gagner !\n")
        tour += 1
        continue

    case = Plateau.content[tmpPos]

    if case.hasBonus() and tmpPos != 100:
        print("!!! BONUS : " + case.bonus.type.name + " !!!\n")

        if case.bonus.type == BonusType.REJOUER:
            replay = True
        elif case.bonus.type == BonusType.DOUBLE:
            tmpPos += lancerDe
        elif case.bonus.type == BonusType.AVANCER_5_CASES:
            tmpPos += 5

    if tmpPos == 100:
        partieGagne = True
        gagnant = j
        continue

    elif tmpPos <= 100:
        j.pos = tmpPos
        if replay:
            replay = False
            continue

    case = Plateau.content[tmpPos] # update Case for pouvoir

    if case.hasPouvoir():
        print("Attention ! C'est une case " + case.pouvoir.name + " direction la case : " + str(case.targetCase))
        j.pos = case.targetCase

    print ("Case : " + str(j.pos) + "\n")
    tour += 1

print("Bravo ! Le gagnant est : " + gagnant.name)

