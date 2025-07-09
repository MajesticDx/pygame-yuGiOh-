from Card import Card

class MahoragaCard(Card):
    def __init__(self, cardInfo, num):
        self.__image = "MahoragaCard.jpg"
        self._currentAtt = 1000
        self._currentDef = 3500
        self._index = 10
        self._attackSound = "mahoragaAttack.mp3"
        self.__adaptCard = None
        self.__adaptDegree = 1
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)

    def _defend(self, opposingCard, attack):    #Adaption Fähigkeit
        if opposingCard == self.__adaptCard:
            self.__adaptDegree *= 0.5
        else:
            self.__adaptDegree = 1
        self._currentDef -= int(attack * self.__adaptDegree)
        self.__adaptCard = opposingCard
