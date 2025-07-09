from Card import Card


class PicaCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "PicaCard.jpeg"
        self._currentAtt = 500
        self._currentDef = 7000
        self._index = 7
        self._attackSound = "picaAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)


    
