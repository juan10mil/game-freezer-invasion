import pygame
from pygame.sprite import Sprite#Sprite hace que se agrupen los elementos 
#relacionadso del juego para actuar sobre todos ellos al mismo tiempo

class Kame(Sprite): #hereda de Sprite
    """Gestiona los kames"""
    def __init__(self, juego):
        """Cre un objeto """
        super().__init__()
        self.screen = juego.screen
        self.settings = juego.settings
        self.color = self.settings.kame_color

        #Crea un rectangulo para el kame en (0,0) y luego lo pone en posicion

        self.rect = pygame.Rect(0, 0, self.settings.kame_ancho, 
                                self.settings.kame_alto)#crea un rectangulo
        self.rect.midtop = juego.goku.rect.midtop #midtop de kame coincidira
                #con el midtop de goku

        #Guarda la posicion de la bala como flotante
        self.y = float(self.rect.y)
    

    def update(self):
        """Mueve la bala hacia arriba de la pantalla"""
        "Actualiza la posicion exacta de la bala"
        self.y -= self.settings.kame_speed #se mueve hacia arriba
        #actualiza la posicion del rectangulo:
        self.rect.y = self.y
    

    def draw_kame(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect) #dibuja el 
        #rectangulo que se creó (pantalla definida,color,parte de la pantalla)