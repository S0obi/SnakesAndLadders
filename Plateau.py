from Case import Case
from Pouvoir import Pouvoir
from BonusType import BonusType
from random import randrange

class Plateau():
    def __init__(self, nbBonus):
        self.content = [None] * 100
        self.content[0] = Case(0, None)

        for i in range(1,len(self.content) + 1):
            self.content.insert(i, Case(i, None))

        self.content[4].setPouvoir(Pouvoir.ECHELLE,  14)
        self.content[9].setPouvoir(Pouvoir.ECHELLE,  31)
        self.content[19].setPouvoir(Pouvoir.ECHELLE, 38)
        self.content[21].setPouvoir(Pouvoir.ECHELLE, 42)
        self.content[28].setPouvoir(Pouvoir.ECHELLE, 84)
        self.content[51].setPouvoir(Pouvoir.ECHELLE, 67)
        self.content[71].setPouvoir(Pouvoir.ECHELLE, 91)
        self.content[80].setPouvoir(Pouvoir.ECHELLE, 94)

        self.content[17].setPouvoir(Pouvoir.SERPENT, 7)
        self.content[54].setPouvoir(Pouvoir.SERPENT, 34)
        self.content[62].setPouvoir(Pouvoir.SERPENT, 20)
        self.content[64].setPouvoir(Pouvoir.SERPENT, 60)
        self.content[87].setPouvoir(Pouvoir.SERPENT, 24)
        self.content[93].setPouvoir(Pouvoir.SERPENT, 73)
        self.content[95].setPouvoir(Pouvoir.SERPENT, 75)
        self.content[98].setPouvoir(Pouvoir.SERPENT, 79)

        listBonusType = [b for b in BonusType]
        for i in range (0, nbBonus):
            self.content[randrange(1,100)].setBonus(listBonusType[i % len(listBonusType)])