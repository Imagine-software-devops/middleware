# curses_ui.py
import curses
import signal
import sys
from .__main__ import HeaderWindow, MenuWindow, DirectoryTreeWindow, OutputWindow, InputBoxWindow, QuickActionsWindow


class CursesUI:
    def __init__(self, stdscr):        
        self.stdscr = stdscr
        self.height, self.width = self.stdscr.getmaxyx()
        curses.start_color()
        curses.curs_set(0)
        curses.noecho()
        self.stdscr.keypad(True)
        self.init_colors()
        self.init_signal_handler()

    def init_colors(self):
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)

    def draw_header(self, config_path):
        header = HeaderWindow(self.stdscr.subwin(self.height // 10, self.width, 0, 0))
        header.draw(config_path)

    def draw_menu(self, config_path):
        menu = MenuWindow(self.stdscr.subwin(self.height * 4 // 5, self.width // 3, self.height // 10, 0))
        menu.draw(config_path)

    def draw_directory_tree(self, config_path):
        directory_tree = DirectoryTreeWindow(self.stdscr.subwin(self.height * 4 // 5, self.width * 2 // 3, self.height // 10, self.width // 3 + 1))
        directory_tree.draw(config_path)

    def draw_output(self):
        output = OutputWindow(self.stdscr.subwin(self.height * 5 // 100, self.width * 2 // 3, self.height * 75 // 100 + 1, self.width // 3 + 1))
        output.draw()

    def draw_input(self):
        input_box = InputBoxWindow(self.stdscr.subwin(self.height * 5 // 100, self.width * 2 // 3, self.height * 80 // 100 + 1, self.width // 3 + 1))
        input_box.draw()

    def draw_quick_actions(self, config_path):
        quick_actions = QuickActionsWindow(self.stdscr.subwin(self.height // 10, self.width, self.height * 90 // 100, 0))
        quick_actions.draw(config_path)

    def init_signal_handler(self):
        signal.signal(signal.SIGINT, self.handle_signal)

    def handle_signal(self, sig, frame):
        # Quand le signal SIGINT (Ctrl-C) est capturé, fermer proprement l'application
        self.close()
        sys.exit(0)

    def main_loop(self, config_path):
        from config.quickactions_config import QuickActionsConfig
        while True:
            self.stdscr.clear()
            self.draw_header(config_path)
            self.draw_menu(config_path)
            self.draw_directory_tree(config_path)
            self.draw_output()
            self.draw_input()
            self.draw_quick_actions(config_path)
            self.stdscr.refresh()
            key = self.stdscr.getch()    
            if key == ord('q'):
                break        
            config_path = QuickActionsConfig.get_action(self, config_path, key)
    def close(self):
        curses.endwin()