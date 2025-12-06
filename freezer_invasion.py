import sys #usado para salir del juego
import pygame
from time import sleep # sleep hace una pausa en el programa
from settings import Settings
from goku import Goku
from kame import Kame
from freezer import Freezer
from estadisticas_game import GameStats
from boton import Boton
from scoreboard import ScoreTabla

class FreezerInvasion:
    """Clase general para gestionar los recursos y el comportamiento
    del juego"""
    def __init__(self):
        """Inicializa el juego y crea los recursos"""
        pygame.init() #configuracion de fondo para que pygame inicie
        self.clock = pygame.time.Clock() #para controlar el fps
        pygame.display.set_caption("Alien invasion")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)#pantalla
                                                                    #completa
        self.settings.screen_ancho = self.screen.get_rect().width #ancho
        self.settings.screen_alto = self.screen.get_rect().height #alto
        # lo anterior crea ventana:
        #si no se especifica la tupla, es la pantalla completa

        self.stats = GameStats(self)
        self.score = ScoreTabla(self)

        self.goku = Goku(self) #este self, aparece como "juego" en goku.py
        self.kames = pygame.sprite.Group()#devuelve un grupo para almacenar 
        #varios elementos del juego, para eso sirve sprite
        self.freezers = pygame.sprite.Group()
        self._crear_flota()

        #inicia el juego en estado activo:
        self.game_active = False

        #Crea el boton Play:
        self.play_boton = Boton(self, 'Play')

    def _crear_freezer(self, actual_x, actual_y):
        """Crea un alienigena y lo coloca en la fila y demas filas"""
        new_freezer = Freezer(self)
        new_freezer.x = actual_x#
        new_freezer.rect.x = actual_x
        new_freezer.rect.y = actual_y
        self.freezers.add(new_freezer)

    def _goku_freezer_golpe(self):
        """Responde al impacto entre estos dos titanes"""
        if self.stats.vidas_restantes > 1 :
            #disminuye vidas:
            self.stats.vidas_restantes -= 1

            self.score.prep_gokus()

            #se deshace de freezers y los kames:
            self.freezers.empty()
            self.kames.empty()

            #crea una nueva flota y centra a goku:
            self._crear_flota()
            self.goku.centrar()

            #pausa
            sleep(0.5) #pausa el programa por medio segundo
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)#hace visible el raton

    def _crear_flota(self):
        """Crea la flota de freezers"""
        #hace un freezer y toda la flota
        freezer = Freezer(self)
        #ancho_freezer = freezer.rect.width, tambien:
        ancho_freezer, alto_freezer = freezer.rect.size #devuelve ancho y alto
        actual_x, actual_y = ancho_freezer, 0
         #siguiente posicion horizontal de freezer y vertical

        while actual_y < (self.settings.screen_alto - 5 * alto_freezer):

            while actual_x <= (self.settings.screen_ancho - ancho_freezer):
                self._crear_freezer(actual_x, actual_y)
                actual_x += ancho_freezer
            #una vez que termino la fila, resetea x y aumenta y:
            actual_x = ancho_freezer
            actual_y += 1 * alto_freezer

    def run_game(self):
        """Inicializa el bucle principal para el juego"""
        while True:
            self._check_events() #se invoca el metodo auxiliar
            if self.game_active: #solo si quedan vidas:
                self.goku.update()
                self._update_kames()
                self._update_freezers()
            self._update_screen()#se invoca el metodo auxiliar
            self.clock.tick(60)#el argumento es la tasa de frames del juego,
            #con esto, pygame se asegura que el bucle se ejecute 60 veces
            #por segundo

    def _update_freezers(self):
        """Actualiza las posiciones de freezers"""
        self._check_flota_bordes()
        self.freezers.update()
        
        #busca closiones goku-freezer:
        if pygame.sprite.spritecollideany(self.goku, self.freezers):#esta 
            #funcion toma dos argumentos, un sprite y un grupo, busca cualquier
            #miembro del grupo sprite haya chocado con el sprite, en este caso
            #goku, devuelve ese freezer que choco, si nadie choca, devuelve None

            print("Shit hit!!!")
            self._goku_freezer_golpe()

        #busca si freezers llegaron al fondo:
        self._check_freezers_abajo()


    def _check_flota_bordes(self):
        """Responde si alguien ha llefado al borde"""
        for freezer in self.freezers.sprites():
            if freezer.check_edges():
                self._cambiar_direccion_flota()
                break

    def _cambiar_direccion_flota(self):
        """Baja toda la flota y cambia su direccion"""
        for freezer in self.freezers.sprites():
            freezer.rect.y += self.settings.flota_velocidad_abajo 
        self.settings.flota_direccion *= -1      

    def _check_events(self): #metodo auxiliar, trabaja dentro de una clase,pero
        #no se ha creado para ser utilizado por el código externo a 
        #dicha clase #siempre con un guion bajo
        
        #Busca eventos de teclado y ratón:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #elif para que quit siempre tenga prioridad
            elif event.type == pygame.KEYDOWN: #detectar teclado
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_posicion = pygame.mouse.get_pos() #devuelve una tupla que
                #contiene las coordenadas de x e y del cursor cuando hace clic
                self._check_play_boton(mouse_posicion)
                               
    def _check_play_boton(self, pos):
        """Inicia el juego cuando el jugador hace clic en play"""
        boton_clic = self.play_boton.rect.collidepoint(pos)
        if boton_clic and not self.game_active: #metodo que comprueba si el
            #punto clic del raton colisiona con la region definida por el rect
            #del boton play
            self.settings.inicializar_dinamica_settings()
            self.stats.reset_stats()
            self.game_active = True
            self.score.prep_score() #perpara un marcador de 0
            self.score.prep_level()
            self.score.prep_gokus()
            #se deshace de los freezers y kames:
            self.freezers.empty()
            self.kames.empty()
            #crea una nueva flota:
            self._crear_flota()
            self.goku.centrar()
            pygame.mouse.set_visible(False) #oculta el raton en pantalla



    def _check_keydown_events(self, event):
        """Responde a pulsaciones de las teclas"""
        if event.key == pygame.K_ESCAPE:
                   sys.exit()
        elif event.key == pygame.K_RIGHT:
             #Mueve la nave hacia la derecha:
            self.goku.moving_right = True #cambiamos el flag 
        elif event.key == pygame.K_LEFT: # o bien derecha o izquierda
            self.goku.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fuego_kame()


    def _fuego_kame(self):
        """Crea un kame y lo añade al grupo de kames""" 
        if len(self.kames) < self.settings.kames_permitidos:
            new_kame = Kame(self) 
            self.kames.add(new_kame) #cada kame es una instancia de Kame, lo que 
            #provoca que se llame al update() de kame, es decir del hijo
            #sprite tiene su propio metodo update() pero no sirve de nada
            

    def _check_keyup_events(self,event):
        """Responde a liberaciones de tecla"""
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
        for kame in self.kames.sprites(): #el metodo sprites() devuelve una 
            #lista de todos los sprites del grupo
            kame.draw_kame()#se dibuja cada bala
        self.freezers.draw(self.screen) #pygame dibuja cada elemetno del grupo
        #en la posicion definida por su atributo rect, self.screen es la 
        #superficie donde se dibuja los elementos

        #dibuja la infomracion de la puntuacion:
        self.score.show_score()

        #dibuja el boton para jugar si el juego esta inactivo:
        if not self.game_active:
            self.play_boton.draw_boton() #se dibuja despues de los demas 
            #elementos, para que sea visible y este por encima de todos los 
            #demas


        pygame.display.flip()#Hace visible la última pantalla dibujada
    

    def _update_kames(self):
        """Actualiza la posicion de los kames y se deshace de las viejas"""
        self.kames.update()#cuando se llama a update en un grupo, el grupo
            #llama automaticamente al metodo update() para cad uno de sussprites
            #llama a kame.update() para cada kame colocado en kames
            #el update() será el update() de cada elemento del grupo, es decir
            #de cada kame
            #Deshacer las balas que han desaparecido:
        for kame in self.kames.copy(): #dado que no se puede eliminar 
                #elementos de una lista o grupo dentro de un bucle, se usa copy
                #que es una copia del grupo
            if kame.rect.bottom <= 0: #bottom = parte inferior
                self.kames.remove(kame)
        self._check_kames_freezer_colisiones()
        

    def _check_kames_freezer_colisiones(self):
        #busca kames que hayan alcanzado a freezers:
        colisiones = pygame.sprite.groupcollide(self.kames, self.freezers, 
                                                True, True)
        #groupcollide busca colisiones entre dos grupos y devuelve un
        #diccionario, donde el par clave-valor se tiene que clave es el kame
        #y el valor es freezer, cuando se solapan se añade un valor al diccionar
        #Los argumentos True indican a pygame que borre las balas y aliesn que 
        #han chocado(True: borra kame, True: borra freezer)
        if colisiones:
            for freezers in colisiones.values():#se pasa en un bucle por todos 
                #los valores que tiene, cada valor es una lista de freezers
                #alcanzados por un splo kame
                self.stats.score += self.settings.freezer_points * len(freezers)
                #len freezers indica la longitud de la lista de freezers que 
                #colisionaron con un solo kame
            self.score.prep_score()
            self.score.check_high_score()
        if not self.freezers:
            #detruye las balas existentes y crea una flota nueva
            self.kames.empty() #vacia el grupo de los kames
            self._crear_flota()
            self.settings.incrementar_velocidad()
            #aumenta el nivel:
            self.stats.level += 1
            self.score.prep_level()
    
    def _check_freezers_abajo(self):
        """Comprueba si freezer llego al borde de abajo"""
        for freezer in self.freezers.sprites():#con sprites accedes al grupo
            #trata esto como si hubieran colisionado
            if self.settings.screen_alto <= freezer.rect.bottom:
                self._goku_freezer_golpe()
                break


if __name__ == '__main__': #se ejecuta si se llama al archivo directamente
    #dice lo que se tiene que ejecutar al momento de abrir el archivo
    #hace una instancia del juego y lo ejecuta:
    a_i = FreezerInvasion()
    a_i.run_game()