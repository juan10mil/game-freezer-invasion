import pygame
from pygame.sprite import Sprite

class Freezer(Sprite):
    """Clase que representa un solo freezer"""

    def __init__(self, juego):
        """Inicializa a freezer"""
        super().__init__()
        #Cara la imagen de freezer y configura su rect
        self.screen = juego.screen
        self.image = pygame.image.load('images/freezer_2.bmp')
        self.rect = self.image.get_rect()
        self.settings = juego.settings
        #inicializa un nuevo freezer en la parte superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = 0

        #Guarda la posicion exacta del alien:
        self.x = float(self.rect.x)
    def update(self):
        """Mueve a freezer"""       
        self.x += (self.settings.freezer_velocidad * 
                   self.settings.flota_direccion)
        self.rect.x = self.x
    

    def check_edges(self):
        """Devuelve True si esta en el borde"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

