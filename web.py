
from flask import Flask, render_template, Response
from main import out
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    cap = cv2.VideoCapture(0)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
    while True:
        frame,marked = out(cap)
        if marked:
            print(marked)
            break
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
