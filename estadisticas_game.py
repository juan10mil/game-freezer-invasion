class GameStats:
    """Sigue las estadisticas del juego"""

    def __init__(self, juego):
        """Inicializa las estadisticas"""
        self.settings = juego.settings
        self.reset_stats()
        self.high_score = 0 #no deberia restablecerse nunca
        

    def reset_stats(self):
        """Inicializa las estadisticas que pueden cambiar"""
        self.vidas_restantes = self.settings.vidas
        self.score = 0 #se reiniican los scores cuando se reinicia stats
        self.level = 1

    
