
import unittest
from unittest.mock import Mock, patch

from EmotionDetector import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetector.emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.1,
                    "disgust": 0.1,
                    "fear": 0.1,
                    "joy": 0.6,
                    "sadness": 0.1
                }
            }]
        }
        mock_post.return_value = response

        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")


if __name__ == "__main__":
    unittest.main()
