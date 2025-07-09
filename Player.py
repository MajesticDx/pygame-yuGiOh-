import pygame

import copy
import random
from Button import Button
from pygame import mixer

from AngelCard import AngelCard
from HakariCard import HakariCard
from HigurumaCard import HigurumaCard
from ItachiCard import ItachiCard
from JokerCard import JokerCard
from LawCard import LawCard
from MahoragaCard import MahoragaCard
from PicaCard import PicaCard
from Picture import Picture
from PredigerCard import PredigerCard
from ShinjiCard import ShinjiCard
from UrougeCard import UrougeCard
from YutaCard import YutaCard
from YetiCoolBrothersCard import YetiCoolBrothersCard


class Player:
    def __init__(self, height, width, player1):

        self.__player1 = player1        #Spieler 1 -> True / Spieler 2 -> False

        self.__HP = 10000

        self.__font = pygame.font.Font("font/yugioh.ttf", 90)
        self.__fontColorHP = (0,115,213) if player1 else (213,0,0)

        self.__cardOutline1 = Picture("cardOutline1.png" if player1 else "cardOutline2.png", 101.5, 146, width//2, abs(height - 150.5))
        self.__cardOutline2 = Picture("cardOutline1.png" if player1 else "cardOutline2.png", 101.5, 146, width//2 - 150, abs(height - 175.5))
        self.__cardOutline3 = Picture("cardOutline1.png" if player1 else "cardOutline2.png", 101.5, 146, width//2 + 150, abs(height - 175.5))
        self.__summonOutline = Picture("cardOutline1.png" if player1 else "cardOutline2.png", 145, 208.5, width//2, abs(height - 370))
        self._outlines = [self.__cardOutline1, self.__cardOutline2, self.__cardOutline3, self.__summonOutline]

        self._attackButton = Button(width//2 + 130 if player1 else width//2 - 130, abs(height - 410), "attackButton.png", "attackButtonReact.png", 62.5, 25)
        self._endturnButton = Button(width//2 + 130 if player1 else width//2 - 130, abs(height - 340), "endturnButton.png", "endturnButtonReact.png", 62.5, 30)
        self._rerollButton = Button(width//2 + 235 if player1 else width//2 - 235, abs(height - 175.5), "refreshButton.png", "refreshButtonReact.png", 25, 25)

        self.__setButton1 = Button(width//2, abs(height - 50), "setButton.png", "setButtonReact.png", 50, 25)
        self.__setButton2 = Button(width//2 - 150, abs(height - 75), "setButton.png", "setButtonReact.png", 50, 25)
        self.__setButton3 = Button(width//2 + 150, abs(height - 75), "setButton.png", "setButtonReact.png", 50, 25)
        self._setButtons = [self.__setButton1, self.__setButton2, self.__setButton3]
        self._attackButtonBool = True
        self._rerollButtonBool = True
        self._setButtonsBool = True

        self._burning = 0
        self._burnImage = Picture("burning.png", 35, 35, self.__summonOutline.rect.x + 420, self.__summonOutline.rect.y if self.__player1 else self.__summonOutline.rect.y)

        self.__cardInfo =   [self.__cardOutline1,
                            self.__cardOutline2,
                            self.__cardOutline3,
                            self.__summonOutline,
                            self._attackButton,
                            self._endturnButton,
                            self.__player1]

        self._cardHallList =    [YutaCard(self.__cardInfo, 0),
                                UrougeCard(self.__cardInfo, 0),
                                JokerCard(self.__cardInfo, 0),
                                PredigerCard(self.__cardInfo, 0),
                                HigurumaCard(self.__cardInfo, 0),
                                HakariCard(self.__cardInfo, 0),
                                PicaCard(self.__cardInfo, 0),
                                YetiCoolBrothersCard(self.__cardInfo, 0),
                                ShinjiCard(self.__cardInfo, 0),
                                MahoragaCard(self.__cardInfo, 0),
                                AngelCard(self.__cardInfo, 0),
                                LawCard(self.__cardInfo, 0),
                                ItachiCard(self.__cardInfo, 0)]

        self.__allCardsList = []
        self._card1 = None
        self._card2 = None
        self._card3 = None
        self._summonedCard = None
        self._fill1Spot()
        self._fill1Spot()
        self._fill1Spot()
        self._cards = [self._card1, self._card2, self._card3, self._summonedCard]
    
    def __generateAllCardsList(self, num):                      #generiert die Karten Liste
        self.__allCardsList = [YutaCard(self.__cardInfo, num), 
                               UrougeCard(self.__cardInfo, num), 
                               JokerCard(self.__cardInfo, num), 
                               PredigerCard(self.__cardInfo, num), 
                               HigurumaCard(self.__cardInfo, num), 
                               HakariCard(self.__cardInfo, num), 
                               PicaCard(self.__cardInfo, num), 
                               YetiCoolBrothersCard(self.__cardInfo, num), 
                               ShinjiCard(self.__cardInfo, num), 
                               MahoragaCard(self.__cardInfo, num), 
                               AngelCard(self.__cardInfo, num),
                               LawCard(self.__cardInfo, num),
                               ItachiCard(self.__cardInfo, num)]
    
    def _summonCard(self, card):        #beschwört eine Karte für den Spieler
        """match card._index:
            case 1:
                self._summonedCard = YutaCard(self.__cardInfo, 0)
            case 2:
                self._summonedCard = UrougeCard(self.__cardInfo, 0)
            case 3:
                self._summonedCard = JokerCard(self.__cardInfo, 0)
            case 4:
                self._summonedCard = PredigerCard(self.__cardInfo, 0)
            case 5:
                self._summonedCard = HigurumaCard(self.__cardInfo, 0)
            case 6:
                self._summonedCard = HakariCard(self.__cardInfo, 0)
            case 7:
                self._summonedCard = PicaCard(self.__cardInfo, 0)
            case 8:
                self._summonedCard = YetiCoolBrothersCard(self.__cardInfo, 0)
            case 9:
                self._summonedCard = ShinjiCard(self.__cardInfo, 0)
            case 10:
                self._summonedCard = MahoragaCard(self.__cardInfo, 0)
            case 11:
                self._summonedCard = AngelCard(self.__cardInfo, 0)
            case 12:
                self._summonedCard = LawCard(self.__cardInfo, 0)   
            case 13:
                self._summonedCard = ItachiCard(self.__cardInfo, 0)"""
        self._summonedCard = card      
        self._summonedCard._summon()

    def _refreshCards(self):        #refreshed das Karten array
        self._cards = [self._card1, self._card2, self._card3, self._summonedCard]
        
    def _randomize(self):           #Randomized die vorhandenen Karten des Spielerss
        if self._card1 != None:
            self.__generateAllCardsList(1)
            self._card1 = random.choice(self.__allCardsList)
        if self._card2 != None:
            self.__generateAllCardsList(2)
            self._card2 = random.choice(self.__allCardsList)
        if self._card3 != None:
            self.__generateAllCardsList(3)
            self._card3 = random.choice(self.__allCardsList)
    
    def _fill1Spot(self):           #Fügt 1 Karte hinzu falls die Karten Slots nicht alle voll sind
        if self._card1 == None:
            self.__generateAllCardsList(1)
            self._card1 = random.choice(self.__allCardsList)
        elif self._card2 == None:
            self.__generateAllCardsList(2)
            self._card2 = random.choice(self.__allCardsList)
        elif self._card3 == None:
            self.__generateAllCardsList(3)
            self._card3 = random.choice(self.__allCardsList)

    def _resetButtons(self):            #selbsterklärend
        self._setButtonsBool = True
        self._attackButtonBool = True
        self._rerollButtonBool = True
    def _deactivateAttackButton(self):
        self._attackButtonBool = False
    def _deactivateRerollButton(self):
        self._rerollButtonBool = False
    def _deactivateSetButtons(self):
        self._setButtonsBool = False

    def _reduceHP(self, amount):        #verringert die HP
        self.__HP -= amount
    #def addHP(self, amount):
        #self.__HP += amount
    
    #@dispatch(object , int)
    def _defend(self, opposingPlayer, attack):      #verteidigung des Spielers
        self.__HP -= attack 

    #@dispatch(object, float)
    #def defend(self, opposingPlayer, attack):
        #self.__HP -= int(self.__HP * attack)
    
    def _kill(self):        #tötet den Spieler
        self.__HP = 0
    
    def _drawHP(self, window):      #zeichnet seine HP
        hpFont = self.__font.render(str(self.__HP), False, self.__fontColorHP)
        window.blit(hpFont, (self.__summonOutline.rect.x + 400, self.__summonOutline.rect.y if self.__player1 else self.__summonOutline.rect.y))
    
    def _player(self):      #gibt True da es sich um einen Spieler handelt
        return True

    def _dead(self):        #checkt ob der Spieler tot ist
        if self.__HP <= 0:
            return True
        else:
            return False
    
    def _tick(self):             #einmal pro Runde wird der tick ausgeführt
        if self._summonedCard != None:
            self._summonedCard._tick()
        if self._burning > 0:
            self._playBurnSound()
            self._burning -= 1
            self.__HP -= 500
    
    def _burn(self):        #setzt Spieler in Flammen (ItachiKarte)
        self._burning = 2
    
    def _playBurnSound(self):
        mixer.Channel(4).set_volume(0.7)
        mixer.Channel(4).play(mixer.Sound("music/burnSound.mp3"))
    
    def _drawBurn(self, window):
        window.blit(self._burnImage.image, (self._burnImage.rect.x, self._burnImage.rect.y))

