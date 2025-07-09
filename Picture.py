import pygame

class Picture():        #Klasse für Bildererstellung
    def __init__(self, image, width, height, x, y):
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            self.image = pygame.image.load(f"pictures/{image}")
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)