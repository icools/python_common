import unittest
from llm.mixed_llm import MixedLlm

class TestMixedLlm(unittest.TestCase):

    def test_mixed_chat(self):
        mixed_llm = MixedLlm()
        question = "請問今天的天氣如何？"

        final_answer = mixed_llm.mixed_chat(question)
        summeries = mixed_llm.summarize_responses(question)

        self.assertTrue(final_answer)
        self.assertIn("samba_nova", mixed_llm.responses)
        self.assertIn("groq", mixed_llm.responses)
        self.assertTrue(mixed_llm.responses["samba_nova"])
        self.assertTrue(mixed_llm.responses["groq"])
        self.assertTrue(summeries)

if __name__ == '__main__':
    unittest.main()