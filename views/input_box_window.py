# input_box_window.py

import curses

class InputBoxWindow:
    def __init__(self, window):
        self.window = window

    def draw(self): 
        text = "Input box: "
        self.window.clear()
        # Récupérer les dimensions de la fenêtre
        max_y, max_x = self.window.getmaxyx()
        # Dessiner les bordures
        self.window.border(0)
        print("InputBoxWindow size (max_x, max_y):", max_x, max_y)  # Ajout de cette ligne pour vérifier la taille de la fenêtre
        # Calculer la position x pour centrer le texte dans la fenêtre
        x_pos = (max_x - len(text)) // 2

        if len(text) >= max_x - 3:
            # Si le texte est trop long, redimensionner la fenêtre pour qu'elle puisse accueillir le texte complet
            self.window.resize(1, len(text) + 3)  # +3 pour éviter tout débordement sur les côtés

        self.window.addstr(0, 0, text, curses.color_pair(2))  # Ajout du texte à la position (0, 0) dans la fenêtre
        self.window.refresh()


