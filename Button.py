import pygame
from pygame import mixer

class Button():                                     #Button Klasse die individuell anklickbare Buttons erstellt
    def __init__(self, x, y, imagepath1, imagepath2, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image1 = pygame.image.load(f"pictures/{imagepath1}")
        self.image1 = pygame.transform.scale(self.image1, (width, height))
        self.image2 = pygame.image.load(f"pictures/{imagepath2}")
        self.image2 = pygame.transform.scale(self.image2, (width, height))
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
        self.overtake = False

    def draw(self, window):                         #Malt den Knopf
        window.blit(self.image, (self.rect.x, self.rect.y))

    def check(self):                                #Checkt ob der Knopf gedrückt wird
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.image = self.image2
            if self.overtake:
               self.hoverSound() 
               self.overtake = False
        else:
            self.image = self.image1
            self.overtake = True
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True
            self.clickSound()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
    
    def hoverSound(self):      #Funktion um hover Sound zu machen
        mixer.Channel(5).set_volume(0.1)
        mixer.Channel(5).play(mixer.Sound("music/hoverSound.mp3"))
    def clickSound(self):      #Funktion um click Sound zu machen
        mixer.Channel(5).set_volume(0.2)
        mixer.Channel(5).play(mixer.Sound("music/clickSound.mp3"))
    
class HoverButton():                                     #HoverButton Klasse die bei "hover" über das Bild reagiert
    def __init__(self, x, y, imagepath1, imagepath2, width, height, width2, height2):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image1 = pygame.image.load(f"pictures/{imagepath1}")
        self.image1 = pygame.transform.scale(self.image1, (width, height))
        self.image2 = pygame.image.load(f"pictures/{imagepath2}")
        self.image2 = pygame.transform.scale(self.image2, (width2, height2))
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.rectOriginal = self.rect
        self.rectOriginal.center = (x,y)
        self.clicked = False
        self.overtake = False
    
    def draw(self, window):                         #Malt den Knopf
        window.blit(self.image, (self.rect.x, self.rect.y))

    def check(self):                                #Checkt ob über das Bild "gehovert" wird
        action = False
        pos = pygame.mouse.get_pos()
        if self.rectOriginal.collidepoint(pos):
            self.image = self.image2
            self.rect = self.image2.get_rect()
            self.rect.center = (217, 500)
            if self.overtake:
               self.hoverSound()
               self.overtake = False
        else:
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.center = (self.x,self.y)
            self.overtake = True
    
    def hoverSound(self):      #Funktion um hover Sound zu machen
        mixer.Channel(5).set_volume(0.1)
        mixer.Channel(5).play(mixer.Sound("music/hoverSound.mp3"))