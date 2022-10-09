<h1 align="center">Welcome to mock-buddy-video-server 👋</h1>

<p> 
  <a href="#" target="_blank">
    <img alt="License: MIT license" src="https://img.shields.io/badge/License-MIT license-yellow.svg" />
  </a>
</p>

> This repo contains video processing service (microservice) for [Mock-buddy](https://github.com/Karthick47v2/mock-buddy), uses Flask to build WebSocket and RESTful APIs, you can see project description [here](https://github.com/Karthick47v2/mock-buddy). This service is deployed on Heroku.

There are many things we need to consider when doing an effective presentation or speech. We need to face the audience, maintain a good body language, present without fear in our tone many more. This is a vast problem, we are only considering online-based presentations/speeches. So, things considered in this system are, keep the eye on the camera, presenting without fear & interruption. The facial key points detection model will track the user’s activity and give feedback.

Workflow is,

1. Interaction detection

- ### Interaction detection

  System will constantly monitor how user's face is visibile on camera. Lightning and other factors may affect this score. This is one of important things to consider as if auidence can't see speakers face then all the efforts made by speaker to give interactive speech or presentation will be wasted. Also, montitor how interactive the speaker throught the speech/presentation. This is important whether remote or physical speech. Becuase giving presentation/speech with a blank face, without any particular facial expression is like speaking in monotone - no matter how great content is, audience will not be engaged.

  These are computed using face landmark detector. Top-down approach is used to detect landmarks. The workflow is,

  1. Face detection - Detected and cropped face from frames using OpenCV DNN module and [ResNet10 SSD](https://github.com/LZQthePlane/Face-detection-base-on-ResnetSSD).
  2. Face landmark detection - Convolutional Neural Network (CNN) architecture used to built face landmark detector. Model trained on [300W](https://ibug.doc.ic.ac.uk/resources/300-W/) datasets (iBUG, HELEN, AFW, LFPW) (68 landmarks). Training details are in this [repo](https://github.com/Karthick47v2/face-landmark-detector). Cropped faces from face detector fed to trained face landmark detector for prediction.

## Prerequisite

- Python 3.7 or newer

## Install

```
pip install -r requirements.txt
```

## Usage

```sh
python3 app.py
```

## Author

👤 **Karthick T. Sharma**

- Github: [@karthick47v2](https://github.com/karthick47v2)
- LinkedIn: [@Karthick T. Sharma](https://linkedin.com/in/Karthick47)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Karthick47v2/mock-buddy-server/issues).

## Show your support

Give a ⭐️ if this project helped you!
