class Settings:
    """Clase que guarda las configuraciones del juego"""


    def __init__(self):
        """Inicializa la configuracion del juego"""
        #configuracion de la pantalla:
        self.screen_ancho = 1200
        self.screen_alto = 800
        self.bg_color = (5, 20, 64)#mezcla de colores rojo verde y azu:RGB
        #(255,0,0) es rojo
        #(0,255,0) es verde
        #(0,0,255) es azul


        #configuracion para goku:
        self.goku_velocidad = 1.0 #float para tener un control más preciso