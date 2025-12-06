import pygame.font
from pygame.sprite import Group
from goku import Goku


class ScoreTabla:
    """Una clase para dar informacion de la puntuacion"""


    def __init__(self,juego):
        """Inicializa los atributos de la puntuacion"""
        self.juego = juego
        self.screen = juego.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = juego.settings
        self.stats = juego.stats
        #Configuracion de la fuente para la informacion de la puntuacion:
        self.text_color = (237, 49, 12)
        self.font = pygame.font.SysFont(None, 48)#fuente y tamaño

        #Prepara la imagen de la puntuacion inicial:
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_gokus()


    def prep_score(self):
        """Convierte la puntuacion en una imagen renderizada"""
        redondear_score = round(self.stats.score, -1)#redondea hasta un numero
        #de posiciones decimales que se pasa comos segundo argumento, en caso
        #de negativos, se redondea el valor al 10,100,1000 etc mas cercano
        #es decir, redondea a la decena mas cercana
        #score_str = str(redondear_score)#de valor numericoo a string
        score_str = f"{redondear_score:,}"# cuando se le agrega :, ; indica a 
        #python que inserte comas en los lugares adecuados del valor numerico
        #como resultado se tiene 1,000,000
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.bg_color)#render 
                                            #crea la imagen

        #muestra la puntuacion en la parte superior derecha de la pantalla
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #a 20 pixeles del 
        #borde derecho de la pantalla 
        self.score_rect.top = 20#borde superior 20 pixeles por debajo del 
        #borde superior de la pantalla

    
    def show_score(self):
        """Dibuja la puntuacion en la pantalla"""
        self.screen.blit(self.score_image, self.score_rect)#se dibuja en la 
        #pantalla
        self.screen.blit (self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.gokus.draw(self.screen)


    def prep_high_score(self):
        """Convierte la puntuacion mas alta en una imagen renderizada"""
        high_score = round(self.stats.high_score, -1 )
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, 
                                                 self.text_color, 
                                                 self.settings.bg_color)
        #centra la puntuacion más alta en la parte superior de la pantalla:
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        #coincide con el centro del eje x del screen
        self.high_score_rect.top = self.score_rect.top #coincide con el top
        #del score

    def prep_level(self):
        """Convierte el nivel en una imagen renderizada"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, 
                                            self.settings.bg_color)

        #coloca el nivel debajo de la puntuacion
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_gokus(self):
        """Muestra cuantos gokus quedan"""
        self.gokus = Group()
        for goku_numero in range(self.stats.vidas_restantes):
            goku = Goku(self)
            goku.rect.x = 10 + goku_numero * goku.rect.width
            goku.rect.y = 10
            self.gokus.add(goku)

    def check_high_score(self):
        """Comprueba si hay una nueva puntuación más alta"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()