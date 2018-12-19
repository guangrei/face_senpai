[![Docker pulls](https://img.shields.io/docker/pulls/cumi/face_recognition.svg )](https://hub.docker.com/r/cumi/face_recognition)

this project use powerful [face_recognition](https://github.com/ageitgey/face_recognition) library by [ageitgey](https://github.com/ageitgey).

for client  `dlib`  and  `face_recognition`  no longer need.

### example

this example with demo server https://face-senpai.herokuapp.com

``` python
import requests
import numpy as np
import jsonpickle
import jsonpickle.ext.numpy as jsonpickle_numpy
import json

jsonpickle_numpy.register_handlers()

# face1
files = {
    'file': ('image1.jpg', open('image1.jpg', 'rb')),
}

response = requests.post('https://face-senpai.herokuapp.com/', files=files)

face = jsonpickle.decode(json.loads(response.content.decode("utf-8"))["msg"])

# face2
files2 = {
    'file': ('image2.jpg', open('image2.jpg', 'rb')),
}
response2 = requests.post('https://face-senpai.herokuapp.com/', files=files2)
face2 = jsonpickle.decode(json.loads(response2.content.decode("utf-8"))["msg"])

print("face1 descriptor:")
print(face)
print("face2 descriptor:")
print(face2)
print("face compare:")

distance = np.linalg.norm([face] - face2, axis=1)

compare = list(distance <= 0.6)
if compare[0]:
    print("match!")
else:
    print("no match!")
```
before run, make sure to install required dependency `pip install numpy jsonpickle requests` 

### Run & Deploy

run locally:
```
$ git clone https://github.com/anigrab/face_senpai.git
$ cd face_senpai/webapp
$ pip install -r requirements.txt
$ gunicorn --bind 0.0.0.0:8080 wsgi
```
deploy to heroku:
```
$ git clone https://github.com/anigrab/face_senpai.git
$ cd face_senpai
$ cp heroku/* .
$ heroku create
$ heroku container:login
$ heroku container:push web
$ heroku container:release web
```
deploy to zeit:
```
$ git clone https://github.com/anigrab/face_senpai.git
$ cd face_senpai
$ cp zeit/* .
$ now
```
deploy to openshift:
```
$ git clone https://github.com/anigrab/face_senpai.git
$ cd face_senpai
$ cp openshift/* .
$ docker build -t openshift-face-senpai .
$ oc new-project anigrab
$ oc new-app openshift-face-senpai --name face-senpai
$ oc expose svc face-senpai --name=face-senpai
```
more server coming soon...