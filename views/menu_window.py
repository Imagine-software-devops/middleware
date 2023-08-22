# menu_window.py

import curses
from controllers.__main__ import MenuWindowController as MWC

class MenuWindow:
    def __init__(self, window):
        self.window = window

    def draw(self, config_path):
        # Dessiner les bordures
        self.window.border(0)    

        # Afficher le texte de la variable 'menu_text' dans la fenêtre de sortie
        menu_text = MWC.create_menu(config_path)
        self.window.addstr(1, 1, menu_text, curses.color_pair(1))

        self.window.refresh()
