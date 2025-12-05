import pygame
class Goku:
    """Clase para gestionar al jugador"""
    def __init__(self,juego):
        """Inicializa a goku"""
        self.screen = juego.screen #es de la pantalla
        self.settings = juego.settings
        self.screen_rect = juego.screen.get_rect() # los trata como rectangulos
        #Carga la imagen y obtiene su rect:
        self.image = pygame.image.load('images/goku_4.bmp')# para png o jpg
                                                #se necesitan otras librerias
                                                #bmp es por defecto de pygame
        self.rect = self.image.get_rect() #ubicacion de goku

        #coloca inicialmente en el centro de la parte inferior:
        self.rect.midbottom = self.screen_rect.midbottom 
        #rect de goku (midbottom) = rect de pantalla (medio de parte inferior)

        self.x = float(self.rect.x) #el rect es entero, se castea para precision

        #Flag de movimiento;empieza con unnna bandera que no se mueve:
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Actualiza la posiciono de la nave en funcion de flag"""
        if self.moving_right and self.screen_rect.right > self.rect.right:
            self.x += self.settings.goku_velocidad #mueve un casillero a la 
                                                #derecha #en el eje x
        if self.moving_left and 0 < self.rect.left: #comienza 0 de la izquierda
            self.x -= self.settings.goku_velocidad
        self.rect.x = self.x #solo toma la porcion entera

    def centrar(self):
        """Centra a goku en la pantalla"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)                          

    def blitme(self):
        """Dibuja la nave en la ubicacion actual"""
        self.screen.blit(self.image, self.rect) #dibuja la imagen en la pantalla
       