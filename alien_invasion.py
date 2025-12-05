import sys #usado para salir del juego
import pygame
from settings import Settings
from goku import Goku



class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento
    del juego"""
    def __init__(self):
        """Inicializa el juego y crea los recursos"""
        pygame.init() #configuracion de fondo para que pygame inicie
        self.clock = pygame.time.Clock() #para controlar el fps
        pygame.display.set_caption("Alien invasion")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_ancho,
                                               self.settings.screen_alto))
        # lo anterior crea ventana:
        #si no se especifica la tupla, es la pantalla completa
        self.goku = Goku(self) #este self, aparece como "juego" en goku.py


    def run_game(self):
        """Inicializa el bucle principal para el juego"""
        while True:
            self._check_events() #se invoca el metodo auxiliar
            self.goku.update()
            self._update_screen()#se invoca el metodo auxiliar
            self.clock.tick(60)#el argumento es la tasa de frames del juego,
            #con esto, pygame se asegura que el bucle se ejecute 60 veces
            #por segundo


    def _check_events(self): #metodo auxiliar, trabaja dentro de una clase,pero
        #no se ha creado para ser utilizado por el código externo a 
        #dicha clase #siempre con un guion bajo
        
        #Busca eventos de teclado y ratón:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #elif para que quit siempre tenga prioridad
            elif event.type == pygame.KEYDOWN: #detectar teclado
                if event.key == pygame.K_ESCAPE:
                   sys.exit()
                if event.key == pygame.K_RIGHT:
                    #Mueve la nave hacia la derecha:
                    self.goku.moving_right = True #cambiamos el flag 
                elif event.key == pygame.K_LEFT: # o bien derecha o izquierda
                    self.goku.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: #detecta cuando suelta la tecla
                                            #que tenia presionada
                    self.goku.moving_right = False 
                elif event.key == pygame.K_LEFT:
                    self.goku.moving_left = False                

    def _update_screen(self):
         #redibuja la pantalla en cada paso por el bucle:
        self.screen.fill(self.settings.bg_color) #se rellena con fill
        self.goku.blitme() #se llama al metodo blitme() para dibujar en
                                #pantalla
        
        pygame.display.flip()#Hace visible la última pantalla dibujada
    

if __name__ == '__main__': #se ejecuta si se llama al archivo directamente
    #dice lo que se tiene que ejecutar al momento de abrir el archivo
    #hace una instancia del juego y lo ejecuta:
    a_i = AlienInvasion()
    a_i.run_game()