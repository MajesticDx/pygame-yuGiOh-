from Card import Card

class UrougeCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "UrougeCard.jpeg"
        self._currentAtt = 1000
        self._currentDef = 2500
        self._index = 2
        self._attackSound = "urougeAttack.mp3"
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    #@dispatch(object, int)
    def _defend(self, opposingCard, attack):    #Heilungs Fähigkeit
        self._currentDef -= attack 
        self.__ability()

    #@dispatch(object, float)
    #def defend(self, opposingCard, attack):
        #self._currentDef -= int(self._currentDef * attack)
        #self.ability()
    
    def __ability(self):
        self._currentAtt += 500
        self._currentDef += 500

