from flask import Flask, request, send_file
from TTS.api import TTS
from pydub import AudioSegment
import uuid

app = Flask(__name__)
# tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False).to("cpu")

@app.route("/tts", methods=["POST"])
def tts_endpoint():
    data = request.get_json()
    text = data.get("text", "")
    speaker = data.get("speaker", "p261")  # 기본값: 남성 화자
    speed = data.get("speed", 1.25)        # 기본값: 1.25배속

    file_id = str(uuid.uuid4())
    original_path = f"original_{file_id}.wav"
    speedup_path = f"output_{file_id}.wav"

    # TTS 생성 (원본 저장)
    tts.tts_to_file(text=text, speaker=speaker, file_path=original_path)

    # 속도 조절하여 새로운 파일 생성
    sound = AudioSegment.from_wav(original_path)
    faster = sound.speedup(playback_speed=speed)
    faster.export(speedup_path, format="wav")

    # 속도 조절된 버전 리턴
    return send_file(speedup_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True, port=5000)