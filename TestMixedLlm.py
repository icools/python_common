import unittest
from llm.mixed_llm import MixedLlm

class TestMixedLlm(unittest.TestCase):

    def test_mixed_chat(self):
        mixed_llm = MixedLlm()
        question = "請問今天的天氣如何？"
        
        # Act
        final_answer = mixed_llm.mixed_chat(question)
        
        # Assert
        self.assertTrue(final_answer)  # 確認最終回答不為空
        self.assertIn("samba_nova", mixed_llm.responses)
        self.assertIn("groq", mixed_llm.responses)
        self.assertIn("gemini_flash", mixed_llm.responses)
        self.assertTrue(mixed_llm.responses["samba_nova"])  # 確認 Samba Nova 回應不為空
        self.assertTrue(mixed_llm.responses["groq"])  # 確認 Groq 回應不為空
        self.assertTrue(mixed_llm.responses["gemini_flash"])  # 確認 Gemini Flash 回應不為空

if __name__ == '__main__':
    unittest.main()