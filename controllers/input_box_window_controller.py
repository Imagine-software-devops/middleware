import json
from typing import Callable, Dict


class MethodRegistry:
    jump_table: Dict[str, Callable] = {}

    # Méthode statique pour enregistrer les actions rapides
    @classmethod
    def register(cls, shortcut: str, description: str) -> Callable:
        def decorator(function: Callable) -> Callable:
            cls.jump_table[shortcut] = function            
            function.shortcut = shortcut            
            function.description = description
            return function
        return decorator

    # Méthode statique pour obtenir la jump_table liée
    @classmethod
    def get_bound_jump_table(cls) -> Dict[str, Callable]:
        return {
            command: function.__get__(None, cls)
            for command, function in cls.jump_table.items()
        }

# Classe pour le contrôleur de fenêtre QuickActionsWindowController
class InputBoxWindowController:
    class Functions(MethodRegistry):
        pass

    # Fonction pour ouvrir le fichier de configuration
    @staticmethod
    def open_config_file(config_path):
        with open(config_path) as json_file:
            config = json.load(json_file)
            return config

    # Créer le menu à partir du fichier de configuration
    def __init__(self, config_path) -> None:
        self.config = self.open_config_file(config_path)
        self.functions = self.Functions.get_bound_jump_table()

    # Obtenir le nom des fonctions    
    def get_functions(self):
        functions = []
        for action in self.config["Application"]["Modules"]["Actions"]:
            @InputBoxWindowController.Functions.register(action["Shortcut"], action["Description"])
            def add_function(action=action, functions=functions):
                functions.append({"shortcut": action["Shortcut"], "target": action["Target"]})
            add_function()
        return functions

