import pyttsx3
import logging


class TextToSpeech:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.engine = pyttsx3.init()

    def speak(self, text_to_speak):
        self.engine.say(text_to_speak)
        self.engine.runAndWait()

    def get_voice(self):
        voice = self.engine.getProperty('voice')
        self.logger.debug(f"Voice is currently: {voice}")
        return voice

    def set_voice(self, voice_id):
        self.engine.setProperty('voice', voice_id)
        self.engine.runAndWait()

    def get_voices(self):
        voice_data = []
        voices = self.engine.getProperty('voices')
        for index in range(voices.__len__()):
            voice_data.append({
                'id': voices[index].id,
                'name': voices[index].name,
            })
        return voice_data

    def get_volume(self):
        volume = int(float(self.engine.getProperty('volume').__str__()) * 100)
        self.logger.debug(f"Volume is currently: {volume}")
        return volume

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            new_volume = volume / 100
            self.engine.setProperty('volume', new_volume)
            self.engine.runAndWait()
        else:
            self.logger.debug(f"Invalid volume [0 to 100]: {volume}")

    def get_rate(self):
        speech_rate = int(self.engine.getProperty('rate').__str__())
        self.logger.debug(f"Speech rate is currently: {speech_rate}")
        return speech_rate

    def set_rate(self, rate):
        if 0 < rate <= 400:
            self.engine.setProperty('rate', rate)
            self.engine.runAndWait()
        else:
            self.logger.debug(f"Invalid speech rate [1 to 400]: {rate}")
