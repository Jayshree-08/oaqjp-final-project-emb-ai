import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_empty_text(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

    def test_whitespace_text(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
