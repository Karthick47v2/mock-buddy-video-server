FROM alpine:latest
WORKDIR /app
# RUN apt-get update && apt-get upgrade -y && apt-get install -y portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common apt-transport-https dotnet6
RUN apk update && apk upgrade 
RUN apk add --no-cache portaudio-dev ffmpeg openjdk8 make automake gcc g++ subversion

RUN apk add --update python3-dev py3-pip dotnet6

# RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.9-dev gcc python3-pip
COPY requirements.txt .
RUN pip3 install --upgrade wheel
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]