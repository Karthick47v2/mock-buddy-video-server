FROM ubuntu:jammy
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils portaudio19-dev ffmpeg openjdk-8-jdk software-properties-common apt-transport-https dotnet6
RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.8-dev gcc python3-pip
COPY requirements.txt .
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .
CMD ["python3.7", "app.py"]