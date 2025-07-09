from Card import Card


class HigurumaCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "HigurumaCard.jpeg"
        self._currentAtt = 1000
        self._currentDef = 3000
        self._index = 5
        self._attackSound = "higurumaAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    #@dispatch(object , int)
    def _defend(self, opposingCard, attack):    #justice Fähigkeit
        self._currentDef -= attack
        opposingCard._justice() 

    #@dispatch(object, float)
    #def defend(self, opposingCard, attack):
        #self._currentDef -= int(self._currentDef * attack)
        #opposingCard.justice()