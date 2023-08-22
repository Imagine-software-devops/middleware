import json
import os
import subprocess
import modules.logging.log as log

class DirectoryTreeWindowController():
        u_name = __name__
        u_name = u_name.replace("__", "")
        logging_app = log.LoggingApp(u_name+".log")
                
        @logging_app.log_action
        # Fonction pour ouvrir le fichier de configuration
        def open_config_file(config_path):
            with open(config_path) as json_file:
                config = json.load(json_file)
                return config
        @logging_app.log_action  
        # Afficher l'arborescence du répertoire courant à l'aide de tree
        def get_directory_tree(config_path, fonction_index):
            config = DirectoryTreeWindowController.open_config_file(config_path)
            current_directory = config["Application"]["Modules"]["Actions"][fonction_index]["CurrentDirectory"]
            tree_command = f"tree -d {current_directory}"
            try:
                tree_output = subprocess.Popen(tree_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)   
                tree_output = tree_output.stdout.read().decode("utf-8")
                return tree_output                
            except Exception as e:
                print(f"Error running tree command: {e}")
    
