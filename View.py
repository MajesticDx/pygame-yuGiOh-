import pygame
from Picture import Picture


class View:
    def __init__(self,  width, height, myP1, myP2):
        self.__WIDTH, self.__HEIGHT = width, height
        self.__WIN = pygame.display.set_mode((self.__WIDTH,self.__HEIGHT))
        pygame.display.set_caption("Yu-gi OH?")

        self.__backgroundimageGame = Picture("BackgroundGame.png", self.__WIDTH, self.__HEIGHT, 0,0)
        self.__backgroundimageHome = Picture("BackgroundHome.png", self.__WIDTH, self.__HEIGHT, 0,0)
        self.__backgroundimageFinish = Picture("BackgroundFinish.png", self.__WIDTH, self.__HEIGHT, 0,0)
        self.__backgroundimageCardHall = Picture("BackgroundCardHall.png", self.__WIDTH, self.__HEIGHT, 0,0)

        self.__cardHallOutline = Picture("cardOutline.png", 402.6, 578.3, 217, 500)

        self.__font = pygame.font.Font("font/yugioh.ttf", 100)
        self.__fontColorP2 = (255,0,0)
        self.__fontColorP1 =  (0,128,255)
        self.__p1Font = self.__font.render("Player 1 Wins!", False, self.__fontColorP1)
        self.__p2Font = self.__font.render("Player 2 Wins!", False, self.__fontColorP2)

        self.__myP1 = myP1
        self.__myP2 = myP2

        self.__font = pygame.font.Font("font/yugioh.ttf", 50)
        self.__fontColorRound = (240,212,120)

    def _drawHome(self):        #zeichnet homescreen
        self.__WIN.blit(self.__backgroundimageHome.image,(0,0))
    
    def _drawCardHall(self):    #zeichnet Kartenhalle
        self.__WIN.blit(self.__backgroundimageCardHall.image,(0,0))
        self.__WIN.blit(self.__cardHallOutline.image, (self.__cardHallOutline.rect.x, self.__cardHallOutline.rect.y))
        for i in self.__myP1._cardHallList:
            self.__WIN.blit(i._cardHallOutline.image, (i._cardHallOutline.rect.x, i._cardHallOutline.rect.y))
            i._cardHallButton.draw(self.__WIN)
        
            

    
    def _drawFinish(self, first, player1):  #zeichnet finish screen
        if first:
            self.__WIN.blit(self.__backgroundimageFinish.image,(0,0))
        if player1:
            self.__player1Wins()
        else:
            self.__player2Wins()

    def __player1Wins(self):    #Spieler 1 gewinnt Schriftzug
        self.__WIN.blit(self.__p1Font, (410, 300))
    def __player2Wins(self):    #Spieler 2 gewinnt Schriftzug
        self.__WIN.blit(self.__p2Font, (410, 300))

    def _drawStandardLayout(self):      #zeichnet standard game Layout
        self.__WIN.blit(self.__backgroundimageGame.image,(0,0))

        for i in self.__myP1._outlines:
            self.__WIN.blit(i.image, (i.rect.x, i.rect.y))
        for i in self.__myP2._outlines:
            self.__WIN.blit(i.image, (i.rect.x, i.rect.y))

        for i in self.__myP1._cards:
           if i != None:
            i._cardButton.draw(self.__WIN)
        for i in self.__myP2._cards:
           if i != None:
            i._cardButton.draw(self.__WIN)

        if self.__myP1._summonedCard != None:
            self.__myP1._summonedCard._statDraw(self.__WIN)
        if self.__myP2._summonedCard != None:
            self.__myP2._summonedCard._statDraw(self.__WIN)
        
        self.__myP1._drawHP(self.__WIN)
        self.__myP2._drawHP(self.__WIN)

        if self.__myP1._burning > 0:
            self.__myP1._drawBurn(self.__WIN)
        if self.__myP2._burning > 0:
            self.__myP2._drawBurn(self.__WIN)

    def _drawButton(self, button):      #zeichnet Knöpfe
        button.draw(self.__WIN)
    
    def _drawRounds(self, round, refillCounter):        #zeichnet Runden und refill anzeige
        roundFont = self.__font.render("Round : " + str(round), False, self.__fontColorRound)
        refillCounterFont = self.__font.render("Refill in : " + str(refillCounter), False, self.__fontColorRound)
        self.__WIN.blit(roundFont, (50, self.__HEIGHT - 100))
        self.__WIN.blit(refillCounterFont, (self.__WIDTH - 260, self.__HEIGHT - 100))
