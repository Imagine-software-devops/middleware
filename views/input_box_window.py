import curses
import os
from curses.textpad import Textbox, rectangle

from controllers.__main__ import InputBoxWindowController
class InputBoxWindow:
    
    def __init__(self, stdscr):
        
        self.stdscr = stdscr    
        self.popup_height = 16
        self.popup_width = 80
        self.y_position = (curses.LINES - self.popup_height) // 2
        self.x_position = (curses.COLS - self.popup_width) // 2    
        # self.popup = None
        self.input = ""


    def draw(self, config_path, key):   
        
        config_file = os.path.basename(config_path)    
        
        controller = InputBoxWindowController(config_path)
        functions = controller.get_functions()

        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        BLACK_ON_WHITE = curses.color_pair(2)

        if config_file == "app_config.json":
            pass
        else :
            self.popup_win = self.stdscr.subwin(self.popup_height, self.popup_width, self.y_position, self.x_position)
        
            self.popup_win.clear()
            self.popup_win.box()
            self.popup_win.bkgd(' ', curses.color_pair(1))

            self.popup_win.addstr(2, 2, "Entrez le chemin du fichier :")

            rectangle(self.stdscr, self.y_position + 1, self.x_position + 32, self.y_position + 3, self.x_position + 78)
            
            self.popup_win.addstr(5, 2, "Press Enter to confirm, Esc to cancel.")            
            
            self.popup_win.refresh()

            self.popup_win.attron(BLACK_ON_WHITE)     
            input = Textbox(self.popup_win, insert_mode=True)
            input.edit()
            self.popup_win.attroff(BLACK_ON_WHITE)
            
            key = self.stdscr.getch()
            
            # if key == ord('Q') or key == ord('q'):  # Changed curses.KEY_EXIT to the actual escape key value
            #     self.popup_win.clear()
            #     self.popup_win.refresh()
            #     self.popup_win = None
            # else:
            #     pass



            # elif key == 10:  # Changed curses.KEY_ENTER to the actual enter key value
            #     break
            # self.stdscr.getch()
            # self.popup_win.clear()
            # self.popup_win.refresh()  
            # self.popup_win = None                

    # def get_input(self):
    #     return self.input  # It seems like 'input' is not defined, so make sure to define and set it somewhere.

## on appelle la methode draw de la view input_box_window.py et on lui rajouter l'argument path
## on créer un template d'input normalisé puis un personnalisé pour chaque module

## on supprime l'input existant de l'application

## module explorer, 1 ou plusieurs inputbox d'une ligne chacuns
## module chatGPT, 1 textarea, 1 input box apikey, 1 input box choix utilisateur
## module github à voir
## module antivirus, 1 input box apikey, 1 input box pour le path du fichier, 1 input pour un mot de passe de protection du fichier
## module templating, 1 formulaire