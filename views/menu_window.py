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
        
        # Calculer la position pour afficher le texte légèrement à gauche
        y = 2
        x = 4  # Décalage à gauche

        # Afficher le texte dans la fenêtre avec le décalage calculé
        lines = menu_text.split('\n')
        for i, line in enumerate(lines):
            self.window.addstr(y + i, x, line, curses.color_pair(1))

        self.window.refresh()






