from flask import Flask, request, send_file
from TTS.api import TTS
import os

app = Flask(__name__)

# 가장 가벼운 단일 화자 모델
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to("cpu")

@app.route("/tts", methods=["POST"])
def tts_endpoint():
    data = request.get_json()
    text = data.get("text", "")
    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False, host="0.0.0.0", port=port)