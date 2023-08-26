# Création d'une classe et de méthodes pour les raccourcis d'actions rapides

import json
import os
import sys
from main import DIR_ROOT
from pathlib import Path

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers import quick_actions_window_controller as QAWC

class QuickActionsConfig:

    config_file = "app_config.json"

    def config_path_contructor(config_file):    
        config_path = Path(DIR_ROOT, "config", config_file)
        return config_path
    
    config_path = config_path_contructor(config_file)

    quick_actions = QAWC.QuickActionsWindowController(config_path)
    actions = quick_actions.get_quick_actions_text()

# Si config_path = app_config
    def get_action(self, config_path, key):
        try : 
            if config_path == Path(DIR_ROOT, "config", "app_config.json"):
                    if key == ord('2'):
                        config_path = QuickActionsConfig.config_path_contructor("antivirus_config.json")
                        return config_path                             
            else:
                if key == ord('0'):
                        config_path = QuickActionsConfig.config_path_contructor("app_config.json")
                        return config_path
        except:
            pass

## Chaque clé "Shortcut" renvoi à la clé "ConfigPath" correspondant au module concerné


# Si config_path = antivirus_config
## Chaque clé "Shortcut" renvoi à la clé "Name" correspondant à la fonction concernée
### Renvoyer les paramètres à la fonction soit un path (le chemin du fichier à envoyer au service VirusTotal) de la clé "UserInput" et une clé API de la clé "ApiKey"
