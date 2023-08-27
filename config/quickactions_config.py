from main import DIR_ROOT
from pathlib import Path
from controllers import quick_actions_window_controller as QAWC

class QuickActionsConfig:

    config_file = "app_config.json"

    def config_path_contructor(config_file):    
        config_path = Path(DIR_ROOT, "config", config_file)
        return config_path
    
    config_path = config_path_contructor(config_file)

    def get_action(self, config_path, key):     
            quick_actions = QAWC.QuickActionsWindowController(config_path)
            quick_actions_text, targets = quick_actions.get_quick_actions_text()
            if config_path == Path(DIR_ROOT, "config", "app_config.json"):              
                config_path = QuickActionsConfig.config_path_contructor(targets[int(chr(key))-1])
                return config_path                                
            else:
                if key == ord('0'):
                        config_path = QuickActionsConfig.config_path_contructor("app_config.json")
                        return config_path    


### Renvoyer les paramètres à la fonction soit un path (le chemin du fichier à envoyer au service VirusTotal) de la clé "UserInput" et une clé API de la clé "ApiKey"
