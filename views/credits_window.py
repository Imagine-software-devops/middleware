import curses


class CreditsWindow:


    def __init__(self, stdscr, credits_data):
        self.stdscr = stdscr
        self.popup_height = len(credits_data) + 4  # Hauteur basée sur le nombre de contributeurs
        self.popup_width = 60
        self.y_position = (curses.LINES - self.popup_height) // 2
        self.x_position = (curses.COLS - self.popup_width) // 2


    def draw(self, credits_data):
        self.popup_win = self.stdscr.subwin(self.popup_height, self.popup_width, self.y_position, self.x_position)

        self.popup_win.clear()
        self.popup_win.box()
        self.popup_win.bkgd(' ', curses.color_pair(1))

        self.popup_win.addstr(2, 2, "")
        
        for i, credit in enumerate(credits_data):
            self.popup_win.addstr(2 + i, 10, credit)

        self.popup_win.addstr(3 + len(credits_data), 2, "Press any key to close")
        self.popup_win.refresh()

        # si on appui sur une touche, on ferme la fenêtre
        self.stdscr.getch()
        self.popup_win.clear()
        self.popup_win.refresh()
        self.popup_win = None

