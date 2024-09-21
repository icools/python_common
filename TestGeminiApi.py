import unittest
from llm.gemini_api import GeminiApi, GeminiModel

class TestGeminiApi(unittest.TestCase):

    def test_call_gemini_flash(self):
        gemini_api = GeminiApi()
        responses = gemini_api.call_gemini_flash("電車難題怎麼解")
        print(responses)
        self.assertIsNotNone(responses)

if __name__ == '__main__':
    unittest.main()