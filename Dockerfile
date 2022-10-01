FROM ubuntu:latest
WORKDIR /app
# RUN apt-get update && apt-get upgrade -y && apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common apt-transport-https dotnet6

RUN apt-get update && apt-get upgrade -y && apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk

# RUN apk add --update python3-dev py3-pip py3-wheel

RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.7-dev gcc python3-pip python3-wheel

COPY requirements.txt .
RUN pip3 install --upgrade pip wheel && pip3 install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]