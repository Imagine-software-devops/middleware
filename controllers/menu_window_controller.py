import json

# Classe pour le contrôleur de fenêtre MenuWindowController
class MenuWindowController:
    
    # Fonction pour ouvrir le fichier de configuration
    def open_config_file(config_path):
        with open(config_path) as json_file:
            config = json.load(json_file)
            return config
    
    # Créer le menu à partir du fichier de configuration
    def create_menu(config_path):
        config = MenuWindowController.open_config_file(config_path)
        menu_text = "Menu :\n"
        for item in config["Application"]["Modules"]["Actions"]:
            menu_text += f"\n\n      {item['Description']}"
        return menu_text
    
        