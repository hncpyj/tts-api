from TTS.api import TTS

tts = TTS(model_name="tts_models/en/vctk/vits")
print(tts.speakers)