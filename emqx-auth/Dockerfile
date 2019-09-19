FROM python:3.7.4-alpine3.10

RUN pip3 install --no-cache-dir quart paho-mqtt

WORKDIR /usr/src/app
COPY emqx-auth.py /usr/src/app

CMD [ "hypercorn", "emqx-auth:app", "-b", "0.0.0.0:8000" ]
