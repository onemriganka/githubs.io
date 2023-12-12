from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/split-video', methods=['POST'])
def split_video():
    video_file = request.files['video-file']
    video_file.save('video.mp4')
    split_video('video.mp4')
    result = ''
    for i in range(1, num_parts+1):
        result += f'part{i}.mp4\n'
    return result

if __name__ == '__main__':
    app.run()
