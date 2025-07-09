from Card import Card



class PredigerCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "PredigerCard.jpeg"
        self._currentAtt = 0
        self._currentDef = 250
        self._index = 4
        self._attackSound = "predigerAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _attack(self, opposingObject):  #one shot Fähigkeit
        opposingObject._kill()
    
    def _selfAttack(self):
        self._kill()