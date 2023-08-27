import json
from typing import Callable, Dict

# Classe pour enregistrer les actions rapides
class MethodRegistry:
    jump_table: Dict[str, Callable] = {}

    # Méthode statique pour enregistrer les actions rapides
    @classmethod
    def register(cls, shortcut: str, target: str, description: str) -> Callable:
        def decorator(quick_action: Callable) -> Callable:
            cls.jump_table[shortcut] = quick_action            
            quick_action.shortcut = shortcut
            quick_action.target = target
            quick_action.description = description
            return quick_action
        return decorator

    # Méthode statique pour obtenir la jump_table liée
    @classmethod
    def get_bound_jump_table(cls) -> Dict[str, Callable]:
        return {
            command: quick_action.__get__(None, cls)
            for command, quick_action in cls.jump_table.items()
        }

# Classe pour le contrôleur de fenêtre QuickActionsWindowController
class QuickActionsWindowController:
    class QuickActions(MethodRegistry):
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
        self.quick_actions = self.QuickActions.get_bound_jump_table()

    # Obtenir le texte des actions rapides
    def get_quick_actions_text(self):
        actions = []        
        for action in self.config["Application"]["Modules"]["Actions"]:
            @QuickActionsWindowController.QuickActions.register(action["Shortcut"], action["Target"],action["Description"])
            def action_function(action=action, actions=actions):
                actions.append(f"{action['Shortcut']}: {action['Description']}")
            action_function()           
        quick_actions_text = "Actions rapides :\n\n" + ", ".join(actions)
        return quick_actions_text
    
    def get_targets(self):
        targets = []
        for action in self.config["Application"]["Modules"]["Actions"]:
            @QuickActionsWindowController.QuickActions.register(action["Shortcut"], action["Target"], action["Description"])
            def add_target(action=action, targets=targets):
                targets.append({"shortcut": action["Shortcut"], "target": action["Target"]})
            add_target()
        return targets



