[![Docker pulls](https://img.shields.io/docker/pulls/cumi/face_recognition.svg )](https://hub.docker.com/r/cumi/face_recognition)

this project use powerful [face_recognition](https://github.com/ageitgey/face_recognition) library by [ageitgey](https://github.com/ageitgey).

for client  `dlib`  and  `face_recognition`  no longer need.

### example

this example use demo endpoints https://grei.pythonanywhere.com/api/face_recognition

``` python
import requests
import numpy as np

# face1
files = {
    'file': ('image1.jpg', open('image1.jpg', 'rb')),
}

response = requests.post('https://grei.pythonanywhere.com/api/face_recognition', files=files).json()

face = response['recognized']['face_descriptor'][0]
face = np.asarray(face)

# face2
files2 = {
    'file': ('image2.jpg', open('image2.jpg', 'rb')),
}
response = requests.post('https://grei.pythonanywhere.com/api/face_recognition', files=files2).json()
face2 = response['recognized']['face_descriptor'][0]
face2 = np.asarray(face2)

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

example with php, make sure to install `php-ml` with `composer require php-ai/php-ml`.

```php
<?php
require "vendor/autoload.php";

use Phpml\Math\Distance\Euclidean;
use Phpml\Math\Distance;

function upload($file)
{ 
    $cFile = curl_file_create($file);
    $post = array('file'=> $cFile);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://grei.pythonanywhere.com/api/face_recognition");
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $result=curl_exec($ch);
    curl_close($ch);
    return json_decode($result, true);
}

$descriptor1 = upload("greysia1.jpg")['recognized']['face_descriptor'][0];
$descriptor2 = upload("greysia2.jpg")['recognized']['face_descriptor'][0];
$euclidean = new Euclidean();
$distance = $euclidean->distance($descriptor1, $descriptor2);

if ($distance <= 0.6) {
    echo "Hello, greysia!\n";
} else {
    echo "not greysia!\n";
}

```
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