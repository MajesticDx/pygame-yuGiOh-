from Card import Card


class YetiCoolBrothersCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "YetiCoolBrothersCard.jpeg"
        self._currentAtt = 500
        self._currentDef = 5000
        self._index = 8
        self._attackSound = "yetiAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):      #Doppel angriff Fähigkeit
        opposingObject._defend(self, self._currentAtt)
        opposingObject._defend(self, self._currentAtt)
    
    def _selfAttack(self):
        self._defend(self, self._currentAtt)
        self._defend(self, self._currentAtt)