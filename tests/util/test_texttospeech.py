import pytest
from util.texttospeech import TextToSpeech


class TestTextToSpeech:
    @pytest.fixture
    def tts(self):
        return TextToSpeech()

    def test_set_voice(self, tts):
        voices = tts.get_voices()
        for voice in voices:
            voice_id = voice.get('id')
            tts.set_voice(voice_id)
            assert tts.get_voice() == voice_id

    def test_set_volume(self, tts):
        starting_value = tts.get_volume()
        tts.set_volume(-1)
        assert starting_value == tts.get_volume()
        starting_value = tts.get_volume()
        tts.set_volume(101)
        assert starting_value == tts.get_volume()

        for value in range(1, 101, 10):
            tts.set_volume(value)
            volume = tts.get_volume()
            assert volume == value

    def test_set_rate(self, tts):
        starting_value = tts.get_rate()
        tts.set_rate(0)
        assert starting_value == tts.get_rate()
        starting_value = tts.get_rate()
        tts.set_rate(401)
        assert starting_value == tts.get_rate()

        for value in range(1, 401, 25):
            tts.set_rate(value)
            rate = tts.get_rate()
            assert rate == value

