import logging
import getpass

class LoggingApp():
    def __init__(self, log_file):
        self.log_file = log_file
        self.default_log_level = logging.INFO

        # Formatter pour les messages de log
        #log_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
        log_formatter = logging.Formatter('%(asctime)s - User: {} - %(levelname)s - %(name)s - %(message)s'.format(getpass.getuser()))
        # Logger racine pour les messages de log
        root_logger = logging.getLogger()
        root_logger.setLevel(self.default_log_level)

        # Handler pour écrire dans le fichier de log
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.default_log_level)
        file_handler.setFormatter(log_formatter)

        # Ajouter le handler au logger racine
        root_logger.addHandler(file_handler)

        # Créer un logger pour les erreurs
        self.error_logger = logging.getLogger("error_logger")
        self.error_logger.setLevel(logging.ERROR)

        # Handler pour écrire dans le fichier de log pour les erreurs
        error_file_handler = logging.FileHandler(self.log_file)
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(log_formatter)

        # Handler pour écrire dans la console pour les erreurs
        error_console_handler = logging.StreamHandler()
        error_console_handler.setLevel(logging.ERROR)
        error_console_handler.setFormatter(log_formatter)

        # Ajouter les handlers au logger des erreurs
        self.error_logger.addHandler(error_file_handler)
        self.error_logger.addHandler(error_console_handler)

    def set_log_level(self, log_level):
        self.default_log_level = log_level
        logging.getLogger().setLevel(self.default_log_level)

    def log_action(self, func):
        def wrapper(*args, **kwargs):
            log = logging.getLogger(func.__module__)
            log_level = getattr(func, "log_level", self.default_log_level)

            # Ajout de messages de log pour le débogage
            log.log(log_level, f"Entering {func.__name__}")

            try:
                result = func(*args, **kwargs)
                log.log(log_level, f"Successfully called {func.__name__}")
                return result
            except Exception as e:
                log.log(log_level, f"Failed to call {func.__name__}: {str(e)}")
                # Utiliser le logger des erreurs pour les erreurs
                self.error_logger.error(f"Failed to call {func.__name__}: {str(e)}")
                # Ne pas lever à nouveau l'exception ici.
        return wrapper
