from app import app  # app.py에서 Flask 인스턴스를 불러옴

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)