from Card import Card


class LawCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "LawCard.jpg"
        self._currentAtt = 1000
        self._currentDef = 4000
        self._index = 12
        self._attackSound = "lawAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)