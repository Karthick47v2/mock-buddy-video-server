FROM ubuntu:20.04 

WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN apt-get install -y portaudio19-dev ffmpeg python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "--threads", "20", "app:app"]