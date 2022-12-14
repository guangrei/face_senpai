# -*-coding:utf8;-*-
import numpy
import face_recognition
import imagesize


def convert_obj(obj):
    if isinstance(obj, numpy.ndarray):
        return obj.tolist()
    return obj


def recognize(imgFile):
    img = face_recognition.load_image_file(imgFile)
    facer = face_recognition.face_encodings(img)
    res = {}
    res['status'] = 'success'
    res['recognized'] = {}
    res['recognized']['face_count'] = len(facer)
    res['recognized']['face_descriptor'] = []
    for i in facer:
        res['recognized']['face_descriptor'].append(convert_obj(i))
    return res


def verify_image(img):
    width, height = imagesize.get(img)
    return width > 0

def verify_ext(filename):
    ALLOWED_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif')
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
