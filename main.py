from flask import Flask, render_template, Response
from camera import VideoCamera # importing VideoCamera class from camera.py


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # to call the index.html file we have created in template folder

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.92.68.21', debug=True)  # To open the interface in browser just use the  '127.92.68.21.5000/' 
