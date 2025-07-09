import pygame
from pygame import mixer
from Control import Control

pygame.init()
mixer.init()
mixer.set_num_channels(6)

                                                                                                              
class Main:
    def __init__(self):
        self.__myControl = Control(self)        #die Control Initsialisieren
        self.__FPS = 60                            #Frames per second auf 60 setzen

    def __mainTheme(self, song, check):     #Funktion um main-themes abzuspielen
        if check:
            mixer.music.load(f"music/{song}")
            mixer.music.set_volume(0.1)
            mixer.music.play(loops=5)

    def _summonSound(self):                         #Funktion um den Sound des beschwörens von Karten abzuspielen
        mixer.Channel(0).set_volume(0.7)
        mixer.Channel(0).play(mixer.Sound("music/summon.mp3"))
    
    def _dieSound(self):                            #Funktion um den Sound des sterbens von Karten abzuspielen
        mixer.Channel(0).set_volume(0.2)
        mixer.Channel(0).play(mixer.Sound("music/die.mp3"))
    
    def _channelSound(self, sound, num, loop):      #Funktion um in verschiedenen Channel verschiedene Sounds abzuspielen
        mixer.Channel(num).set_volume(0.2)
        mixer.Channel(num).play(mixer.Sound("music/"+ sound +""), loops=loop)


    def main(self):
        HOMESCREEN = True       #Variablen um den Zustand des Spiels zu bestimmen
        CARDHALL = False
        P1ROUND = False
        P2ROUND = False
        FINISH = False

        homemusic = True        #Sorgen für das einmalige abspielen von den main-themes
        gamemusic = False
        
        clock = pygame.time.Clock()     #initialisieren der clock
        run = True
        while run:                          #game-loop
            clock.tick(self.__FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if HOMESCREEN:              #Homescreen Zustand
                if homemusic:
                    self.__mainTheme("HomeMusic.mp3", homemusic)
                    homemusic = False
                self.__myControl._homescreen()      #Steuerung des homescreens
                if self.__myControl._checkButton(self.__myControl._startGameButton):    #check starte Spiel Knopf
                    self._channelSound("timeToDuel.mp3", 2, 0)
                    HOMESCREEN = False
                    P1ROUND = True
                    gamemusic = True
                    homemusic = True
                    self.__myControl._myP1._deactivateAttackButton() 
                if self.__myControl._checkButton(self.__myControl._cardHallButton):     #check cardHall Knopf
                    HOMESCREEN = False
                    CARDHALL = True
            elif CARDHALL:              #Cardhall Zustand
                self.__myControl._cardHall()      #Steuerung der Cardhall
                if self.__myControl._checkButton(self.__myControl._cardHallHomeButton):     #check cardHall Knopf
                    HOMESCREEN = True
                    CARDHALL = False           
            elif P1ROUND:              #Runde Spieler 1 Zustand
                if gamemusic:           #einmaliges ausführen der Spiel Musik
                    self.__mainTheme("GameMusic.mp3", gamemusic)
                    gamemusic = False
                self.__myControl._p1Turn()      #Steuerung der Spieler 1 Runde
                if self.__myControl._checkButton(self.__myControl._myP1._endturnButton):        #check endturn Knopf
                    self._channelSound("endTurn1.mp3", 3, 0)
                    P1ROUND = False
                    P2ROUND = True
                    self.__myControl._myP2._resetButtons()
                    self.__myControl._myP1._tick()
                if self.__myControl._checkDead():        #check ob ein Spieler tot ist
                    P1ROUND = False
                    FINISH = True
                    self.__myControl._myP2._kill()
                    self.__myControl._setPlayer1Winner(True)
            elif P2ROUND:              #Runde Spieler 2 Zustand
                self.__myControl._p2Turn()
                if self.__myControl._checkButton(self.__myControl._myP2._endturnButton):        #check endturn Knopf
                    self._channelSound("endTurn2.mp3", 3, 0)
                    P2ROUND = False
                    P1ROUND = True
                    self.__myControl._countRound()
                    self.__myControl._myP1._resetButtons()
                    self.__myControl._myP2._tick()
                if self.__myControl._checkDead():       #check ob ein Spieler tot ist
                    P2ROUND = False
                    FINISH = True
                    self.__myControl._myP1._kill()
                    self.__myControl._setPlayer1Winner(False)
            elif FINISH:              #Spiel Ende Zustand
                if homemusic:
                    self.__mainTheme("HomeMusic.mp3", homemusic)
                    self._channelSound("losingSound.mp3", 2, 0)
                    self.__myControl._p1Turn()
                    homemusic = False
                self.__myControl._finish()          #Steuerung des finish screens
                if self.__myControl._checkButton(self.__myControl._finishHomeButton):       #check HomeButton Knopf
                    HOMESCREEN = True
                    FINISH = False
                    self.__myControl = Control(self)        #neu erstellung der Control-Klasse

        pygame.quit()
if __name__ == "__main__":
    main = Main()
    main.main()

#python -m pip install -U pygame==2.5.2
#python -m pip install -U multipledispatch