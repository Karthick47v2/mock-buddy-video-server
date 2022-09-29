"""Process client requests"""

import os
import datetime

from flask import Flask, request, json
from flask_socketio import SocketIO
from flask_cors import CORS

from src.face_model import FaceModel
from src.audio_util import AudioUtil
from src.slide import Slide
from src.lang import LangChecker

# create app instance with CORS
app = Flask(__name__)
cors = CORS(app)

# socket comm
socketio = SocketIO(app, cors_allowed_origins="*")

# initialize models
fm = FaceModel()


# Restful APIs
@app.get('/init/')
def init_model():
    """Initialize or reset result variables

    Returns:
        dict[str,str]: response
    """
    fm.reset()
    return {'status': 200}


@app.get('/vid_fb/')
def get_vid_fb():
    """Return feedback

    Returns:
        dict[str,str]: response
    """
    return fm.get_vid_feedback()


@app.post('/slide_analyze/')
def analyze_slide():
    """Extract slide and analyze for improvements

    Returns:
        dict[str,str]: response
    """
    slide = Slide(request.json['url'], datetime.datetime.now().strftime(
        '%m_%d_%Y_%H_%M_%S') + '.pptx')
    slide.extract_pptx()

    info = slide.get_data()

    # check for spelling and grammatical errors
    lang_tool = LangChecker(slide.get_txt())
    suggestions = lang_tool.get_results()

    # delete slide after processing
    if os.path.exists(slide.filename):
        os.remove(slide.file_name)

    return {
        'slide_count': info[0],
        'word_count': json.dumps(info[1]),
        'shape_count': info[2],
        'font_count': json.dumps(info[3]),
        'mistake': json.dumps(suggestions)
    }


@app.post('/audio_out/')
def get_audio():
    """Process audio file sent from client

    Returns:
        dict[str,str]: response
    """
    try:
        audio_file = request.files['file']
        # name as M_D_Y_H_M_S format in order to avoid overwriting issue
        audio_file = AudioUtil(file_name=datetime.datetime.now().strftime(
            '%m_%d_%Y_%H_%M_%S') + '.wav')

        audio_file.change_audio_format(audio_file)

        # upload audio to ggl storage (mandatory for transcribing long audio (> 1mins))
        audio_file.storage.upload_to_bucket(audio_file.file_name)

        speech_rate = audio_file.get_speech_rate()

        # delete existing file in storage (local and cloud)
        audio_file.storage.delete_file(audio_file.file_name)
        if os.path.exists(audio_file.file_name):
            os.remove(audio_file.file_name)

        return {
            'status': 200,
            'wpm': speech_rate
        }
    # pylint: disable=broad-except
    except Exception:
        return {
            'status': 400
        }


# SocketIO events
@socketio.on('process_frame')
def detect_facial_points(uri):
    """Detect facial keypoints from request => send prediction as response

    Args:
        uri (str): base64 encoded frame
    """
    fm.detect_face(uri)


@socketio.on('connect')
def connected():
    """Trigger when new client connects"""
    print("[Clinet Connected]")


@socketio.on('disconnect')
def disconnected():
    """Trigger when client disconnects"""
    print("[Client Disconnected]")


# main thread
if __name__ == '__main__':

    # currently using eventlet server for socket production-env
    # socket will also take care of restful api calls
    socketio.run(app, port=5000, debug=True)
