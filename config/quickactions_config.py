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
    config_path = Path(DIR_ROOT, "config", config_file)
    quick_actions = QAWC.QuickActionsWindowController(config_path)
    actions = quick_actions.get_quick_actions_text()
    


# Si config_path = app_config
## Chaque clé "Shortcut" renvoi à la clé "ConfigPath" correspondant au module concerné


# Si config_path = antivirus_config
## Chaque clé "Shortcut" renvoi à la clé "Name" correspondant à la fonction concernée
### Renvoyer les paramètres à la fonction soit un path (le chemin du fichier à envoyer au service VirusTotal) de la clé "UserInput" et une clé API de la clé "ApiKey"
