from Card import Card


class AngelCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "AngelCard.jpg"
        self._currentAtt = 1000
        self._currentDef = 2500
        self._index = 11
        self._attackSound = "angelAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):      #Heil fähigkeit
        opposingObject._defend(self, self._currentAtt)
        self._currentDef += int(self._currentAtt / 2)