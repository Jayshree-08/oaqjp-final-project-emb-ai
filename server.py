
from flask import Flask, request, render_template
from EmotionDetector import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze", "").strip()

    if not text:
        return "Invalid input! Please enter text to analyze.", 400

    try:
        result = emotion_detector(text)

        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again.", 400

        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    except Exception:
        app.logger.exception("Emotion detection failed")
        return "Emotion detection service is unavailable.", 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
