import curses
import json
from pathlib import Path

from .__main__ import CreditsWindow


class OptionsWindow:


    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.popup_height = 16
        self.popup_width = 60
        self.y_position = (curses.LINES - self.popup_height) // 2
        self.x_position = (curses.COLS - self.popup_width) // 2
        self.current_option = 0
        self.languages = ["English", "French", "Spanish"]
        self.selected_language = 0


    def draw(self):
        self.popup_win = self.stdscr.subwin(self.popup_height, self.popup_width, self.y_position, self.x_position)             

        while True:

            self.popup_win.clear()
            self.popup_win.box()
            self.popup_win.bkgd(' ', curses.color_pair(1))

            options = [
                "Language (touche 'L'):",
                "Credits"
            ]

            for i, option in enumerate(options):
                if i == self.current_option:
                    self.popup_win.addstr(6 + 2 * i, 2, option, curses.A_REVERSE)
                else:
                    self.popup_win.addstr(6 + 2 * i, 2, option)

            self.popup_win.addstr(2, 2, "Options Menu:")
            self.popup_win.addstr(15, 2, "Press 'Q' to close")
            
            self.popup_win.addstr(6, 25, self.languages[self.selected_language])
            
            self.popup_win.refresh()

            key = self.stdscr.getch()

            if key == ord('q') or key == ord('Q'):
                break
            elif key == curses.KEY_DOWN:
                self.current_option = min(self.current_option + 1, len(options) - 1)
            elif key == curses.KEY_UP:
                self.current_option = max(self.current_option - 1, 0)
            elif key == ord('l') or key == ord('L'):
                self.selected_language = (self.selected_language + 1) % len(self.languages)

            if options[self.current_option] == "Credits" and key == curses.KEY_ENTER or key == 10 or key == 13:
                self.open_credits()
                self.current_option = 0

        self.popup_win.clear()
        self.popup_win.refresh()


    def open_credits(self):

        config_path = Path("config/app_config.json")
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
            credits_data = config_data.get('Application', {}).get('Crédits', [])

        credits_window = CreditsWindow(self.stdscr, credits_data)
        credits_window.draw(credits_data)
