from Card import Card


class ItachiCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "ItachiCard.jpg"
        self._currentAtt = 750
        self._currentDef = 3500
        self._index = 13
        self._attackSound = "itachiAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):      #brenn Fähigkeit
        opposingObject._defend(self, self._currentAtt)
        opposingObject._burn()