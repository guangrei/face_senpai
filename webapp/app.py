import face_recognition
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import jsonpickle
import jsonpickle.ext.numpy as jsonpickle_numpy

jsonpickle_numpy.register_handlers()
# variable
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
CORS(app)

# function


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_result(file_stream):
    img = face_recognition.load_image_file(file_stream)
    facer = face_recognition.face_encodings(img)
    if len(facer) > 0:
        result = {"status": "success", "msg": jsonpickle.encode(facer[0])}
        return jsonify(result)
    else:
        result = {"status": "failed", "msg": "no face found!"}


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            result = {"status": "failed", "msg": "invalid request!"}
            return jsonify(result)
        file = request.files['file']
        if file.filename == '':
            result = {"status": "failed", "msg": "file empty!"}
            return jsonify(result)
        if file and allowed_file(file.filename):
            return process_result(file)
    result = {"status": "pending", "msg": "listen for request!"}
    return jsonify(result)


# main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
