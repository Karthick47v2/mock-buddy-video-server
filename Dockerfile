FROM ubuntu:jammy
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.7 python3-pip
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]