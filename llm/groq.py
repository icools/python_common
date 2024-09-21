# groq.py
from groq import Groq
import os

class GroqApi:
    def __init__(self):
        self.api_key = os.getenv("GROQ_KEY")
        self.client = Groq(api_key=self.api_key)

    def call_gemma(self, question):
        print("groq gemma2 thinking...")
        
        completion = self.client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": question}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion #.choices[0].message.content.strip()