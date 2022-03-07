import logging
from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime


class DBHandler:
    def __init__(self, config_handler):
        self.logger = logging.getLogger(__name__)
        self.config_handler = config_handler
        self.db_path = config_handler.app_path / 'config'
        self.engine = self.build_engine()
        self.metadata = MetaData()
        self.create_table_models()

    def build_engine(self):
        self.db_path.mkdir(parents=True, exist_ok=True)
        db_file = self.db_path / 'appdata.db'
        self.logger.debug(f"Database file: {db_file}")
        return create_engine(f"sqlite:///{db_file}", echo=False)

    def create_table_models(self):
        self.logger.debug(f"Log Table: {self.config_handler.log_table}")
        Table(
            self.config_handler.log_table, self.metadata,
            Column('timestamp', DateTime),
            Column('text', String)
        )
        self.metadata.create_all(self.engine, checkfirst=True)

    def insert(self, table, data):
        db_table = Table(table, self.metadata, autoload=True, autoload_with=self.engine)
        return self.engine.execute(db_table.insert(), data)
