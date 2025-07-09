from Card import Card

class ShinjiCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "ShinjiCard.jpeg"
        self._currentAtt = 0
        self._currentDef = 4000
        self._index = 9
        self._attackSound = "shinjiAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):      #sselbstangriffs Fähigkeit
        if not opposingObject._player():
            opposingObject._selfAttack()