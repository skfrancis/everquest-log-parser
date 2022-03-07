from pathlib import Path

import pytest
from src.util.confighandler import ConfigHandler
from src.util.logfilehandler import LogFileHandler


class TestLogFileHandler:
    @pytest.fixture(scope='session')
    def build_files(self, tmp_path_factory):
        files = []
        file_data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            '[Sat Jan 1 00:00:00 2000]',
            '[] Welcome to Everquest!',
            'Welcome to Everquest!',
            ''
        ]
        logs_dir = tmp_path_factory.mktemp('Logs')
        log_file = logs_dir / 'eqlog_Character_server.txt'
        log_file.write_text("\n".join(file_data))
        files.append(log_file)
        invalid_file = logs_dir / 'log.txt'
        invalid_file.write_text("\n".join(file_data))
        files.append(invalid_file)
        return files

    def test_load_log_file(self, build_files):
        app_path = Path.cwd()
        for file in build_files:
            config = ConfigHandler(app_path)
            config.log_file = file
            handler = LogFileHandler(config)
            file_data = handler.load_log_file()
            if file_data:
                assert type(file_data) == list
            else:
                assert file_data is None
