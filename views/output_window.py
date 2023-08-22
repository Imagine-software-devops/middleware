# output_window.py

import curses

class OutputWindow:
    def __init__(self, window):
        self.window = window
        self.text_lines = []

    def add_line(self, line):
        self.text_lines.append(line)

    def draw(self):
        # Effacer la fenêtre de sortie
        self.window.clear()
        # Récupérer la taille de la fenêtre de sortie
        max_y, max_x = self.window.getmaxyx()
        # Dessiner les bordures
        self.window.border(0)        
        # Afficher le texte de la variable 'text' dans la fenêtre de sortie
        text = "Output: "
        self.window.addstr(0, 0, text, curses.color_pair(2))        
        # Dessiner le menu des actions rapides ici
        for y, line in enumerate(self.text_lines):
            if y >= max_y:
                break
            self.window.addstr(y + 1, 0, line, curses.color_pair(2))
        self.window.refresh()
