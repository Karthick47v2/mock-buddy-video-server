FROM ubuntu:latest   

WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.7 python3.7-dev gcc python3-pip python3-wheel

RUN update-alternatives --set python /usr/bin/python3.7

COPY requirements.txt .
RUN pip3 install --upgrade pip wheel && pip3 install -r requirements.txt
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "--threads", "10", "app:app"]