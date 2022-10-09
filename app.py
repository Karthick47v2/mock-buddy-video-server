"""Process client requests"""

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

from src.face_model import FaceModel

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
    result = fm.get_vid_feedback()
    fm.reset()
    return result


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
    socketio.run(app, port=5000)
