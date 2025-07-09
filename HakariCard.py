import pygame
from Card import Card
import random

from Picture import Picture


class HakariCard(Card):
    def __init__(self, cardInfo, num):
        self.__cardInfo = cardInfo
        self.__image = "HakariCard.jpeg"
        self._currentAtt = 4000
        self._currentDef = 1000
        self._index = 6
        self.__random = 0
        self._attackSound = "hakariAttack.mp3"

        self.__hit = False
        self.__hitImage = Picture("hit.png", 30, 30, self.__cardInfo[4].x - 370 if self.__cardInfo[6] else self.__cardInfo[4].x + 370, self.__cardInfo[4].y + 50 if self.__cardInfo[6] else self.__cardInfo[4].y - 30)
        self.__missImage = Picture("miss.png", 30, 30, self.__cardInfo[4].x - 370 if self.__cardInfo[6] else self.__cardInfo[4].x + 370, self.__cardInfo[4].y + 50 if self.__cardInfo[6] else self.__cardInfo[4].y - 30)
        
        self.__font = pygame.font.Font("font/yugioh.ttf", 50)
        self.__fontColorAtt = (255,0,0)
        self.__fontColorDef =  (0,128,255)
        super().__init__(cardInfo, num, self.__image, self._currentAtt, self._currentDef, self._index, self._attackSound)
    
    def _statDraw(self, window):    #extra anzeige ob er trifft
        if self._summoned():
            attFont = self.__font.render(str(self._currentAtt), False, self.__fontColorAtt)
            defFont = self.__font.render(str(self._currentDef), False, self.__fontColorDef)
            window.blit(attFont, (self.__cardInfo[4].x - 330 if self.__cardInfo[6] else self.__cardInfo[4].x + 230, self.__cardInfo[4].y - 25))
            window.blit(defFont, (self.__cardInfo[5].x - 330 if self.__cardInfo[6] else self.__cardInfo[5].x + 230, self.__cardInfo[5].y - 25))

            if self.__hit:
                window.blit(self.__hitImage.image, (self.__hitImage.rect.x, self.__hitImage.rect.y))
            elif not self.__hit:
                window.blit(self.__missImage.image, (self.__missImage.rect.x, self.__missImage.rect.y))
                
            if self._burning > 0:
                window.blit(self._burnImage.image, (self._burnImage.rect.x, self._burnImage.rect.y))

    def _attack(self, opposingObject): #50/50 Fähigkeit
        self.__randomNumber()
        if self.__random == 1:
            opposingObject._defend(self, self._currentAtt)
            self.__hit = True
        else:
            self.__hit = False
    
    #@dispatch(object , int)
    def _defend(self, opposingCard, attack):
        self.__randomNumber()
        if self.__random == 1:
            self._currentDef -= attack
            self.__hit = True
        else:
            self.__hit = False 

    #@dispatch(object, float)
    #def defend(self, opposingCard, attack):
        #self.randomNumber()
        #if self.random == 1:
            #self._currentDef -= int(self._currentDef * attack)
    
    def _halfAttack(self):
        if self.__random == 1:
            self._currentAtt = int(0.5 * self._currentAtt)
    
    def __randomNumber(self):
        self.__random = random.randint(0,1)