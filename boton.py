import pygame.font

class Boton:
    """Una clase para crear botones"""


    def __init__(self, juego, msg):
        """Inicializa los atributos del boton"""
        self.screen = juego.screen
        self.screen_rect = self.screen.get_rect()

        #configura las dimensiones y propiedades del boton:
        self.ancho, self.alto = 200, 50
        self.boton_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48) #permite mostrar texto,
        #None indica a pygame fuente predeterminada y 48 es el tamano del texto

        #Crea el objeto rect del boton y lo centra
        self.rect = pygame.Rect(0, 0, self.ancho, self.alto)
        self.rect.center = self.screen_rect.center

        #solo hay que prepara el mensaje del boton una vez
        self._prep_msg(msg)
    

    def _prep_msg(self, msg):
        """Convierte msg en una imagen renderizada y centra el texto"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.boton_color)#convierte el texto
        #almacenado en msg en una imagen, True indica si se activa o desactiva
        #el suavizado de lineas (suaviza los bordes del text), los otros 
        #argumentos son color de fuente y fondo (si no se incluye color de,
        #  fondo, pygame intentara renderizar la fuente con un fondo
        #  transparente)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_boton(self):
        """Dibuja el boton en blanco y luego el mensaje"""
        self.screen.fill(self.boton_color, self.rect) #dibuja parte rectangular
        #del boton
        self.screen.blit(self.msg_image, self.msg_image_rect)#dibuja la imagen
        #de texto en la pantalla, pasandole ina imagen y el rect asociado a ella