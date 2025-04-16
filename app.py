from flask import Flask, request, send_file
from TTS.api import TTS
import os

app = Flask(__name__)

# 모델 불러오기 (Render에서 실행 가능)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to("cpu")

@app.route("/tts", methods=["POST"])
def tts_endpoint():
    data = request.get_json()
    text = data.get("text", "")
    output_path = data.get("output_path", "output.wav")  # 파일명 외부에서 받음

    # TTS 생성 (단일 화자, 속도 조절 없음)
    tts.tts_to_file(text=text, file_path=output_path)

    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    # Render 호환 포트
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)