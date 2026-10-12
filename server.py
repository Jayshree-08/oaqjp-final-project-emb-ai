from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():

    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return jsonify({"error": "Invalid input! Please provide text."}), 400

    result = emotion_detector(text_to_analyze)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Emotion Detector</title>
        </head>
        <body>
            <h1>Emotion Detector</h1>

            <form action="/emotionDetector" method="get">
                <textarea name="textToAnalyze"
                    placeholder="Enter your text here"
                    rows="5" cols="50"></textarea>
                <br><br>
                <button type="submit">Analyze Emotion</button>
            </form>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
