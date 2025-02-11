"""Module to expose the emotion derector endpoint."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """Function to return emotion detection"""

    text_to_analyse = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyse)

    dominant = emotions["dominant_emotion"]
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions['sadness']

    if dominant is None:
        return " Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


    return response, 200

@app.route("/")
def render_index_page():
    """Function to render the index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
