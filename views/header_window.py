import curses
from controllers.__main__ import HeaderWindowController as HWC

class HeaderWindow:
    def __init__(self, window):
        self.window = window

    def draw(self, config_path):

        # Dessiner les bordures
        self.window.border(0)

        # Afficher le texte des variables 'app_name', 'module_name' et 'current_directory' dans la fenêtre de sortie
        
        # ASCII art redimensionné
        ascii_art = r"""       
        ┏┓  ┏┓   
┃┃┓┏┃┃┏┓┏
┣┛┗┫┗┛┣┛┛
   ┛  ┛  
        """
        
        lines = ascii_art.strip().split('\n')
        max_y, max_x = self.window.getmaxyx()
        
        # Redimensionner le texte ASCII art en fonction de la largeur de la fenêtre
        max_width = min(max_x, max(len(line) for line in lines))
        scaled_ascii_art = '\n'.join(line[:max_width] for line in lines)
        
        # Ajuster la position verticale pour centrer l'ASCII art
        y = max_y // 3        
        x = max_x // 2 - max_width // 2
        for i, line in enumerate(scaled_ascii_art.split('\n')):
            self.window.addstr(y + i, x, line, curses.color_pair(1))

        module_name = HWC.get_module_name(config_path)
        
        # Ajuster la position verticale du nom du module à gauche
        y_module = max_y // 2
        x_module = 4  
        self.window.addstr(y_module, x_module, module_name, curses.color_pair(1))  

        current_directory = f"Répertoire courant: {HWC.get_current_directory(config_path, 0)}"
        
        # Ajuster la position verticale du répertoire courant à droite
        y_current = max_y // 2

        # Ajuster la position horizontale en fonction de la largeur de la fenêtre
        x_current = max_x - len(current_directory) - 4  # Placer à droite
        self.window.addstr(y_current, x_current, current_directory, curses.color_pair(1))
        
        self.window.refresh()
