# quick_actions_window.py

import curses
from controllers.__main__ import QuickActionsWindowController as QAWC

class QuickActionsWindow:
    def __init__(self, window):
        self.window = window

    def draw(self, config_path):
      
        # Dessiner les bordures
        self.window.border(0)

        # Créer une instance du contrôleur de fenêtre QuickActionsWindowController
        controller = QAWC(config_path)

        # Obtenir le texte des actions rapides
        menu_text = controller.get_quick_actions_text()

        # Afficher le texte de la variable 'text' dans la fenêtre de sortie
        self.window.addstr(1, 1, menu_text, curses.color_pair(1))
        
        # Dessiner le menu des actions rapides ici
        self.window.refresh()
