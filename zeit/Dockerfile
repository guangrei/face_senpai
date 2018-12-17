FROM cumi/face_recognition
MAINTAINER guangrei <grei@tuta.io>

ADD ./webapp/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

EXPOSE 80

CMD gunicorn --bind 0.0.0.0:80 wsgi 