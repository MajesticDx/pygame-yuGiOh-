import pygame
from pygame import mixer
from Button import HoverButton
from abc import ABC

from Picture import Picture

class Card(ABC):        #abstrakte Klasse zum erstellen individueller Klassen
    def __init__(self, cardInfo, num, image, currentAtt, currentDef, index, attackSound):
        self.__cardOutline = cardInfo[0] if num == 1 else cardInfo[1] if num == 2 else cardInfo[2] 
        self.__summonOutline = cardInfo[3]
        self.__attackButton = cardInfo[4]
        self.__endturnButton = cardInfo[5]
        self.__player1 = cardInfo[6]    #wenn die Karte Spieler 1 gehört dann True
        self.__image = image
        self.__font = pygame.font.Font("font/yugioh.ttf", 50)
        self.__fontColorAtt = (255,0,0)
        self.__fontColorDef =  (0,128,255)
        self.__summoned = False
        self._currentAtt = currentAtt
        self._currentDef = currentDef
        self._cardButton = HoverButton(self.__cardOutline.x, self.__cardOutline.y , self.__image, self.__image, 91.5, 135.5, 366, 542)

        self._burning = 0
        self._burnImage = Picture("burning.png", 30, 30, cardInfo[4].x - 395 if cardInfo[6] else cardInfo[4].x + 395, cardInfo[4].y + 80 if cardInfo[6] else cardInfo[4].y - 60)

        if self._index < 6:     #sorgt dafür das die Koordianten in der Cardhall mit Bezug des Indexes ein 5x3 Rechteck ausfüllt
            self.__cardHallX = self._index 
        elif self._index < 11:
            self.__cardHallX = self._index - 5
        else:
            self.__cardHallX = self._index - 10
        
        if self._index < 6:
            self.__cardHallY = 1
        elif self._index < 11:
            self.__cardHallY = 2
        else:
            self.__cardHallY = 3
    
        self._cardHallButton = HoverButton((400 + (self.__cardHallX * 180)), ((self.__cardHallY * 230) - 100), self.__image, self.__image, 128, 189, 366, 542)
        self._cardHallOutline = Picture("cardOutline.png", 140.8, 201.63, (400 + (self.__cardHallX * 180)),((self.__cardHallY * 230) - 100))

        self._index = index
        self._attackSound = attackSound

    def _summoned(self):    #guckt ob die Karte beschwört
        if self.__summoned == True:
            return True
        else:
            return False

    def _summon(self):    #beschwört eine Karte
        self._cardButton = HoverButton(self.__summonOutline.x, self.__summonOutline.y, self.__image, self.__image, 135, 200, 366, 542)
        self.__summoned = True

    def _statDraw(self, window):    #zeichnet die Statistiken
        if self._summoned():
            attFont = self.__font.render(str(self._currentAtt), False, self.__fontColorAtt)
            defFont = self.__font.render(str(self._currentDef), False, self.__fontColorDef)
            window.blit(attFont, (self.__attackButton.x - 330 if self.__player1 else self.__attackButton.x + 230, self.__attackButton.y - 25))
            window.blit(defFont, (self.__endturnButton.x - 330 if self.__player1 else self.__endturnButton.x + 230, self.__endturnButton.y - 25))
            if self._burning > 0:
                window.blit(self._burnImage.image, (self._burnImage.rect.x, self._burnImage.rect.y))

    
    def _dead(self):    #guckt ob die Karte tot ist und gibt bool zurück
        if self._currentDef <= 0:
            return True
        else:
            return False

    def _attack(self, opposingObject):    #standard angriff einer Karte
        opposingObject._defend(self, self._currentAtt)
    
    #@dispatch(object , int)
    def _defend(self, opposingCard, attack):    #standard verteidigung einer karte
        self._currentDef -= attack 

    #@dispatch(object, float)
    #def defend(self, opposingCard, attack):
        #self._currentDef -= int(self._currentDef * attack)
    
    def _halfAttack(self):    #halbiert currentAttack (JokerKarte)
        self._currentAtt = int(0.5 * self._currentAtt)
    
    def _kill(self):    #tötet die Karte
        self._currentDef = 0
    
    def _justice(self):    #sorgt für einen gegenangriff    (TakabaKarte)
        self._currentDef -= int(self._currentAtt / 2)
    
    def _player(self):    #abfrage ob es sich um einen Spieler handelt
        return False
    
    def _selfAttack(self):    #greift sich selber an (ShinjiKarte)
        self._defend(self, self._currentAtt)

    def _tick(self):        #Funktion für den tick-damage (über Runden hinaus Brennschaden)
        if self._burning > 0:
            self._playBurnSound()
            self._burning -= 1
            self._currentDef -= 500
    
    def _burn(self):        #setzt eine Karte in Flammen (ItachiKarte)
        self._burning = 2
    
    def _playBurnSound(self):
        mixer.Channel(4).set_volume(0.7)
        mixer.Channel(4).play(mixer.Sound("music/burnSound.mp3"))