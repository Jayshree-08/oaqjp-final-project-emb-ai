# Emotion Detector

## Project Description
This project detects emotions in a given text using the IBM Watson NLP Emotion Detection API.

## Features
- Detects anger
- Detects disgust
- Detects fear
- Detects joy
- Detects sadness
- Identifies the dominant emotion
- Flask web application
- Input validation and error handling

## Project Structure

EmotionDetector/
    EmotionDetection/
        __init__.py
        emotion_detection.py
    test_emotion_detection.py
    server.py
    requirements.txt
    README.md

## Installation

Install dependencies:

pip install -r requirements.txt

## Run Tests

python -m unittest test_emotion_detection.py

## Run Application

python server.py

Open http://127.0.0.1:5000 in your browser.

## API Endpoint

GET /emotionDetector?textToAnalyze=Your text here
