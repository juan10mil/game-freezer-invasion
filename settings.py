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
        self.goku_velocidad = 7.0 #float para tener un control más 
        self.vidas = 3
        #configuracion para el kame:
        self.kame_speed = 9.0
        self.kame_ancho = 3
        self.kame_alto = 50
        self.kame_color = (51,130,204)
        self.kames_permitidos = 3

        #configuraciones de freezer:
        self.freezer_velocidad = 11.0
        self.flota_velocidad_abajo = 35
        #Bandera: flota_direccion 1 representa derecha, -1 izquierda
        self.flota_direccion = 1