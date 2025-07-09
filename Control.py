import pygame
from Button import Button
from Card import Card
from LawCard import LawCard
from View import View
from Player import Player


class Control:
    def __init__(self, main):
        self.__main = main              #Für die Sound Wiedergabe
        self.__WIDTH, self.__HEIGHT = 1400, 1000        #die Werte der screen größe

        self.__round = 1
        self.__baseRefillNumber = 4
        self.__refillCounter = self.__baseRefillNumber

        self.__firstFinish = True
        self._player1Winner = True
        self._finishHomeButton = Button(self.__WIDTH//2, self.__HEIGHT // 2, "home.png", "homeReact.png", 100, 100)

        self._cardHallHomeButton = Button(940, abs(self.__HEIGHT // 2) + 300, "cardhomeButton.png", "cardhomeButtonReact.png", 200, 50)
        self._startGameButton = Button(self.__WIDTH//2, abs(self.__HEIGHT // 2) + 100, "startGameButton.png", "startGameButtonReact.png", 200, 50)
        self._cardHallButton = Button(self.__WIDTH//2, abs(self.__HEIGHT // 2) + 200, "cardHallButton.png", "cardHallButtonReact.png", 200, 50)

        self._myP1 = Player(self.__HEIGHT, self.__WIDTH, True)      #initsialisierung des Spieler 1
        self._myP2 = Player(0, self.__WIDTH, False)      #initsialisierung des Spieler 2

        self.__myView = View(self.__WIDTH,self.__HEIGHT, self._myP1, self._myP2)      #initsialisierung der View

    def _homescreen(self):  #sorgt für die Funktionen des homescreens
        self.__myView._drawHome()
        self.__myView._drawButton(self._startGameButton)
        self.__myView._drawButton(self._cardHallButton)
        self.__firstFinish = True
        pygame.display.update()
    
    def _cardHall(self):  #sorgt für die Funktionen der cardHall
        self.__myView._drawCardHall()
        self.__myView._drawButton(self._cardHallHomeButton)
        for i in self._myP1._cardHallList:
            if i != None:
                i._cardHallButton.check()
        pygame.display.update()

    def _finish(self):  #sorgt für die Funktionen des finish screens
        self.__myView._drawFinish(self.__firstFinish, self._player1Winner)
        self.__firstFinish = False
        self.__myView._drawButton(self._finishHomeButton)
        pygame.display.update()
    
    def _setPlayer1Winner(self, player1):  #setzt einen Spieler als gewinner
        if player1:
            self._player1Winner = True
        else:
            self._player1Winner = False

    def _checkDead(self):  #schaut ob eine Spieler tot ist
        if self._myP1._dead():
            return True
        elif self._myP2._dead():
            return True
        else:
            return False

    def _checkButton(self, button):  #guckt ob mit einem Knopf interagiert wird
        if button.check():
            return True
        else:
            return False

    def __cardCheck(self):  #schaut für den Karten-hover Effekt und ob Karten tot sind
        for i in self._myP1._cards:
            if i != None:
                i._cardButton.check()
        for i in self._myP2._cards:
            if i != None:
                i._cardButton.check()
        if self._myP1._summonedCard != None:
            if self._myP1._summonedCard._dead():
                self.__main._dieSound()
                self._myP1._summonedCard = None
        if self._myP2._summonedCard != None:
            if self._myP2._summonedCard._dead():
                self.__main._dieSound()
                self._myP2._summonedCard = None
    
    def __setButtonCheck(self, button, card, player, num):   #checkt den set Knopf und summoned eine Karte
        if card != None:
            self.__myView._drawButton(button)
            if button.check():
                self.__main._summonSound()
                player._summonCard(card)
                self.__killSetCard(player, num)
                player._deactivateSetButtons()
    
    def __killSetCard(self, player, num):  #tötet die gesetzte Karte
        if num == 1:
            player._card1 = None
        elif num == 2:
            player._card2 = None
        elif num == 3:
            player._card3 = None

    def __attackButtonCheck(self, player, opposingPlayer):  #checkt den attackButton Knopf und sorgt für die Angriffs-Funktion
        if player._summonedCard != None:
            self.__myView._drawButton(player._attackButton)
            if player._attackButton.check():
                self.__main._channelSound(player._summonedCard._attackSound, 1, 0)
                if opposingPlayer._summonedCard != None and not isinstance(player._summonedCard, LawCard):
                    player._summonedCard._attack(opposingPlayer._summonedCard)
                    if opposingPlayer._summonedCard._dead():
                        opposingPlayer._reduceHP(abs(opposingPlayer._summonedCard._currentDef))
                else:
                    player._summonedCard._attack(opposingPlayer)
                player._deactivateAttackButton()
    
    def __rerollButtonCheck(self, player):  #checkt den reroll Knopf und sorgt für den reroll der Karten
        self.__myView._drawButton(player._rerollButton)
        if player._rerollButton.check():
            self.__main._channelSound("rerollSound.mp3", 4, 2)
            player._randomize()
            player._deactivateRerollButton()
    
    def _countRound(self):  #zählt die Runden
        self.__round += 1
        self.__refillCounter -= 1
        if self.__refillCounter <= 0:
            self.__refillCounter = self.__baseRefillNumber
            self._myP1._fill1Spot()
            self._myP2._fill1Spot()

    def __turn(self, player, otherPlayer):  #alle Funktionen die nötig sind für eine Runde (ob 1 oder 2)
        self.__cardCheck()
        self.__myView._drawStandardLayout()
        self.__myView._drawRounds(self.__round, self.__refillCounter)

        if player._setButtonsBool:
            self.__setButtonCheck(player._setButtons[0], player._card1, player, 1)
            self.__setButtonCheck(player._setButtons[1], player._card2, player, 2)
            self.__setButtonCheck(player._setButtons[2], player._card3, player, 3)
        
        if player._attackButtonBool:
            self.__attackButtonCheck(player, otherPlayer)
        
        if player._rerollButtonBool:
            self.__rerollButtonCheck(player)

        self.__myView._drawButton(player._endturnButton)

        player._refreshCards()
        otherPlayer._refreshCards()
        pygame.display.update()

    def _p1Turn(self):  #Parameter für Runde 1
        self.__turn(self._myP1, self._myP2)

    def _p2Turn(self):  #Parameter für Runde 2
        self.__turn(self._myP2, self._myP1)
