import pytest
from types import GeneratorType
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
        log_file = tmp_path_factory.mktemp('Logs') / 'eqlog_Character_server.txt'
        log_file.write_text("\n".join(file_data))
        files.append(log_file)
        invalid_file = tmp_path_factory.mktemp('Logs') / 'log.txt'
        invalid_file.write_text("\n".join(file_data))
        files.append(invalid_file)
        return files

    # TODO: Figure out best way to test this
    def test_run_parser(self, build_files):
        for file in build_files:
            handler = LogFileHandler(file)
            parser = handler.run_parser()
            if parser:
                assert type(parser) == GeneratorType

    def test_load_log_file(self, build_files):
        for file in build_files:
            handler = LogFileHandler(file)
            file_data = handler.load_log_file()
            if file_data:
                assert type(file_data) == list
            else:
                assert file_data is None
