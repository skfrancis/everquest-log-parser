import logging
from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime


class DBHandler:
    def __init__(self, app_path, player_data):
        self.logger = logging.getLogger(__name__)
        self.player_data = player_data
        self.db_path = app_path / 'config'
        self.engine = self.build_engine()
        self.create_table_models()

    def build_engine(self):
        self.db_path.mkdir(parents=True, exist_ok=True)
        db_file = self.db_path / 'appdata.db'
        self.logger.debug(f"Database file: {db_file}")
        return create_engine(f"sqlite:///{db_file}", echo=False)

    def create_table_models(self):
        metadata = MetaData()
        log_table = self.player_data['character'] + '_' + self.player_data['server']
        self.logger.debug(f"Log Table: {log_table}")
        Table(
            log_table, metadata,
            Column('timestamp', DateTime),
            Column('text', String)
        )
        metadata.create_all(self.engine, checkfirst=True)
