import json

# Variable vers le fichier de configuration
# with open('../config/app_config.json') as json_file:
#     config = json.load(json_file)

# Classe pour le contrôleur de fenêtre HeaderWindowController
class HeaderWindowController:

    # Fonction pour ouvrir le fichier de configuration
    def open_config_file(config_path):
        with open(config_path) as json_file:
            config = json.load(json_file)
            return config

    # Afficher le nom de l'application dans le header.
    def get_application_name(config_path):
        config = HeaderWindowController.open_config_file(config_path)
        return config["Application"]["Name"]

    # Récupérer le nom du module dans le fichier de configuration.
    def get_module_name(config_path):
        config = HeaderWindowController.open_config_file(config_path)
        return config["Application"]["Modules"]["Name"]

    # Récupérer le répertoire courant
    def get_current_directory(config_path, fonction_index):
        config = HeaderWindowController.open_config_file(config_path)
        return config["Application"]["Modules"]["Actions"][fonction_index]["CurrentDirectory"]

