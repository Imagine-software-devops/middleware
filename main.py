# main.py
import curses
from pathlib import Path
from views.curses_ui import CursesUI
import config.quickactions_config as QC

DIR_ROOT = Path(__file__).parent.absolute()

def main(stdscr):  # Ajoutez l'argument stdscr ici
    # On défini le fichier config à utiliser
    config_file = QC.QuickActionsConfig.config_path
    config_path = Path(DIR_ROOT, config_file)
    ui = CursesUI(stdscr)  # Passez stdscr à l'initialisation de CursesUI
    ui.main_loop(config_path)
    ui.close()
    
if __name__ == "__main__":
    curses.wrapper(main)
