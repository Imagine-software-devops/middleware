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

         # Calculer les dimensions de la fenêtre
        max_y, max_x = self.window.getmaxyx()

        # Calculer la position pour afficher le texte légèrement à gauche
        y = max_y // 2 - 1 # Centrer verticalement
        x = 2  # Décalage à gauche

        # Afficher le texte dans la fenêtre avec le décalage calculé
        lines = menu_text.split('\n')
        for i, line in enumerate(lines):
            self.window.addstr(y + i, x, line, curses.color_pair(1))

        # Dessiner le menu des actions rapides ici
        self.window.refresh()
