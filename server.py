"""
This part contains the server part
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")

def sent_emotion_detector():
    """
    Run the analysis and return the response
    and handle the errors
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is not None :
        return f"For the given statement, the system response is {response}"
    if response['dominant_emotion'] is None :
        return "Invalid text! Please try again"

    return None

@app.route("/")
def render_index_page():
    """
    Render the HTML Page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)
