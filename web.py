
from flask import Flask, render_template, Response,url_for,redirect,jsonify
from main import out
import time
import cv2

app = Flask(__name__)

m = False

@app.route('/')
def index():
    while True:
        global m
        return render_template('index.html',enable = m)
        


@app.route('/huh')
def test():
    print('test')
    return str(m)

def gen():
    cap = cv2.VideoCapture(0)
    while True:
        try:
            frame,marked = out(cap)
            if marked:
                print(marked)
        except:
            frame,marked = out(cap)
            print(marked)

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        if marked[0]==True:
            global m
            m= marked
            
            
        

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
