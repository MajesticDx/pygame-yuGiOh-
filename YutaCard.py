from Card import Card

class YutaCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "YutaCard.jpg"
        self._currentAtt = 0
        self._currentDef = 3500
        self._index = 1
        self._attackSound = "yutaAttack.mp3"
        self.__firstAttack = True
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):  #Angriffs kopie Fähigkeit
        if not opposingObject._player():
            if self.__firstAttack:
                self.__firstAttack = False
                self._currentAtt = opposingObject._currentAtt
        opposingObject._defend(self, self._currentAtt)
