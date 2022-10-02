FROM ubuntu:20.04 

WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN apt-get install -y software-properties-common
RUN apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk 

RUN apt-get install -y python3-pip python3-wheel

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "--threads", "20", "app:app"]