<h1 align="center">Welcome to mock-buddy-server 👋</h1>

<p> 
  <a href="#" target="_blank">
    <img alt="License: MIT license" src="https://img.shields.io/badge/License-MIT license-yellow.svg" />
  </a>
</p>

> This repo contains backend for [Mock-buddy](https://github.com/Karthick47v2/mock-buddy), uses Flask to build WebSocket and RESTful APIs, you can see project description [here](https://github.com/Karthick47v2/mock-buddy). Backend is deployed on Heroku.

There are many things we need to consider when doing an effective presentation or speech. We need to face the audience, maintain a good body language, present without fear in our tone many more. This is a vast problem, we are only considering online-based presentations/speeches. So, things considered in this system are, keep the eye on the camera, presenting without fear & interruption. The facial key points detection model will track the user’s activity and speech emotion recognition model will classify if there are any fear in their tone and give feedback about their talk. Futhermore, Google Speech-To-Text API also used to detect users speech rate along with [VAD](https://github.com/wiseman/py-webrtcvad).

Workflow is,

1. Visual score calculation
2. Vocal score calculation

- ### Visual score calculation

  System will compute 3 different scores based on camera feed. Those are,

  - Visibility score - Represents how user's face is visibile on camera. Lightning and other factors may affect this score. This is one of important things to consider as if auidence can't see speakers face then all the efforts made by speaker to give interactive speech or presentation will be wasted.
  - Interactivity score - Represents how interactive the speaker throught the speech/presentation. This is important whether remote or physical speech. Becuase giving presentation/speech with a blank face, without any particular facial expression is like speaking in monotone - no matter how great content is, audience will not be engaged.
  - Posture score - [***SOON***] Represents wheter user looking at monitor.........

  These are computed using face landmark detector. Top-down approach is used to detect landmarks. The workflow is,

  1. Face detection - Detected and cropped face from frames using OpenCV DNN module and [ResNet10 SSD](https://github.com/LZQthePlane/Face-detection-base-on-ResnetSSD).
  2. Face landmark detection - Convolutional Neural Network (CNN) architecture used to built face landmark detector. Model trained on [300W](https://ibug.doc.ic.ac.uk/resources/300-W/) datasets (iBUG, HELEN, AFW, LFPW) (68 landmarks). Training details are in this [repo](https://github.com/Karthick47v2/face-landmark-detector). Cropped faces from face detector fed to trained face landmark detector for prediction.

- ### Vocal score calculation

  System will compute 2 different scores based on speech. Those are,

  - Speech confidence score - Represents how good user's voice throughout the speech. This will highly affect the engagement of audience because if the speaker is not confident about their speech then audience engagement rate will decrease over time. Giving speech without fear and engaging speech instead of monotonous speech are keypoints for increasing audience engagement.
  - Speech rate - Represents how many words spoken per minute. Speaker needs to be aware of his speech rate will doing presentation/speech, because even if we practice carefully, they may speech at faster rate due to joy or slower rate due to fear.

  Speech confidence score is calculated using speech emotion classifier's output. CNN architecture used to built speech emotion classifier (aka recognition). Model trained on [RAVDESS](https://github.com/Karthick47v2/face-landmark-detector) dataset. Training details are in this [repo](https://github.com/Karthick47v2/speech-emotion-classifier).

  Speech rate was calculated by dividing number of words spoken by time taken. Recorded speech was transcribed using Google Speech-to-Text API and spoken time was calculated accurately with help of [VAD](https://github.com/wiseman/py-webrtcvad).

## Prerequisite

- Google cloud account (+ Google cloud bucket)
- Set environment variables (`GOOGLE_APPLICATION_CREDENTIALS` - path to google_credentials.json, `GOOGLE_CREDENTIALS` - content of file)

## Install

Server environment needs portaudio19-dev, libsndfile-dev, ffmpeg to process audio files

Ex- For Ubunutu,

```sh
sudo apt install portaudio19-dev libsndfile-dev ffmpeg
```

```sh
pip install -r requirements.txt
```

## Usage

Tested on python 3.7 and 3.8

```sh
python3.7 app.py
```

## Author

👤 **Karthick T. Sharma**

- Github: [@karthick47v2](https://github.com/karthick47v2)
- LinkedIn: [@Karthick T. Sharma](https://linkedin.com/in/Karthick47)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Karthick47v2/mock-buddy-server/issues).

## Show your support

Give a ⭐️ if this project helped you!
