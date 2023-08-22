# header_window.py

import curses
from controllers.__main__ import HeaderWindowController as HWC

class HeaderWindow:
    def __init__(self, window):
        self.window = window

    def draw(self, config_path):

        # Dessiner les bordures
        self.window.border(0)

        # Afficher le texte des variables 'app_name', 'module_name' et 'current_directory' dans la fenêtre de sortie
        app_name = HWC.get_application_name(config_path)
        self.window.addstr(1, 1, app_name, curses.color_pair(1))

        module_name = HWC.get_module_name(config_path)
        self.window.addstr(1, self.window.getmaxyx()[1] // 3, module_name, curses.color_pair(1))

        current_directory = f"Répertoire courant: {HWC.get_current_directory(config_path, 0)}"
        self.window.addstr(1, self.window.getmaxyx()[1] * 2 // 3, current_directory, curses.color_pair(1))
        
        self.window.refresh()
