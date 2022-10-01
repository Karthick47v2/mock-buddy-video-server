FROM ubuntu:jammy
WORKDIR /app
RUN apt-get update && apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.7 python3-pip
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]