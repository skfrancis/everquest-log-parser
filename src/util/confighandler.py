

class ConfigHandler:
    def __init__(self, app_path):
        self.version = '0.0.7 alpha'
        self.app_path = app_path
        self.log_file = None
        self.character_info = None
        self.log_table = None

    def log_table_config(self, character_info):
        self.character_info = character_info
        self.log_table = character_info['character'] + '_' + character_info['server']
