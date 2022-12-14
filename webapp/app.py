import face_recognition
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import facelib


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            result = {"status": "error", "reason": "invalid request!"}
            return jsonify(result)
        file = request.files['file']
        if file.filename == '':
            result = {"status": "error", "reason": "file empty!"}
            return jsonify(result)
        if file and facelib.verify_ext(file.filename) and facelib.verify_image(file):
            result = facelib.recognize(file)
            return jsonify(result)
    result = {"status": "pending", "reason": "listen for request!"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
