FROM cumi/face_recognition
MAINTAINER guangrei <grei@tuta.io>

ADD ./webapp/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

RUN useradd -m myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT wsgi 