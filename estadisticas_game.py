class GameStats:
    """Sigue las estadisticas del juego"""

    def __init__(self, juego):
        """Inicializa las estadisticas"""
        self.settings = juego.settings
        self.reset_stats()

    def reset_stats(self):
        """Inicializa las estadisticas que pueden cambiar"""
        self.vidas_restantes = self.settings.vidas