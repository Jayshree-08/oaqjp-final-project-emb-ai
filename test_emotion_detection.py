import unittest
from unittest.mock import Mock, patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def run_test(self, expected_emotion):
        emotions = {
            "anger": 0.1,
            "disgust": 0.1,
            "fear": 0.1,
            "joy": 0.1,
            "sadness": 0.1
        }
        emotions[expected_emotion] = 0.8

        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{"emotion": emotions}]
        }

        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=response
        ):
            result = emotion_detector("Test sentence")
            self.assertEqual(
                result["dominant_emotion"], expected_emotion
            )

    def test_anger(self):
        self.run_test("anger")

    def test_disgust(self):
        self.run_test("disgust")

    def test_fear(self):
        self.run_test("fear")

    def test_joy(self):
        self.run_test("joy")

    def test_sadness(self):
        self.run_test("sadness")


if __name__ == "__main__":
    unittest.main()