"""
This part contains the server part
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/EmotionDetection")
def emotion_detector():
    text_to_analyze = requests.args.get(text_to_analyze)
    response = emotion_detector(text_to_analyze)
    return f"For the given statement, the system respon is {response}"

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)