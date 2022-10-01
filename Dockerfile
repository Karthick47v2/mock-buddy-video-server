FROM alpine:latest
WORKDIR /app
# RUN apt-get update && apt-get upgrade -y && apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common apt-transport-https dotnet6
RUN apk update && apk upgrade 
RUN apk add --no-cache \
    portaudio-dev=19.7.0 \
    ffmpeg=5.1.2-r1 \
    openjdk8=8.242.08-r0

RUN apk add --update python3-dev=3.5.1-r0

# RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.9-dev gcc python3-pip
COPY requirements.txt .
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]