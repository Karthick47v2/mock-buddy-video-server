FROM ubuntu:jammy
WORKDIR /app
RUN sudo apt-get update && sudo apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install python3.7
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]