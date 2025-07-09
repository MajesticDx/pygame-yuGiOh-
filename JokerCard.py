from Card import Card


class JokerCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "JokerCard.jpeg"
        self._currentAtt = 1000
        self._currentDef = 2000
        self._index = 3
        self._attackSound = "jokerAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):      #Angriffs veringerungs Fähigkeit
        opposingObject._defend(self, self._currentAtt)
        if not opposingObject._player():
            opposingObject._halfAttack()