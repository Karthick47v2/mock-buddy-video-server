FROM ubuntu:jammy
WORKDIR /app
RUN apt-get update && apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]