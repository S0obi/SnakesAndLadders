from Bonus import Bonus

class Case:
    def __init__(self, num, pouvoir):
        self.num = num
        self.pouvoir = pouvoir
        self.targetCase = None
        self.bonus = None

    def setPouvoir(self, pouvoir, targetCase):
        self.pouvoir = pouvoir
        self.targetCase = targetCase

    def hasPouvoir(self):
        return self.targetCase is not None

    def hasBonus(self):
        return self.bonus is not None

    def setBonus(self, bonusType):
        self.bonus = Bonus(bonusType)