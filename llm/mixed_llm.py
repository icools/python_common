# mixed_llm.py is a class that combines the responses from Samba Nova, Groq, and Gemini Flash. It uses threading to call the three APIs concurrently and then summarizes the responses. The main function takes user input and calls the mixed_chat method to get the final answer.
from typing import Final
from llm.samba_nova import chat_with_samba_nova
import threading
from llm.groq import GroqApi, GroqModel
from llm.gemini_api import GeminiApi, GeminiModel

class MixedLlm:
    def __init__(self):
        self.responses = {}
        self.threads = []

    def call_samba_nova(self, question):
        response = chat_with_samba_nova(question)
        self.responses["samba_nova"] = response.choices[0].message.content.strip()

    def call_groq(self, question):
        groq_api = GroqApi()
        response = groq_api.call_gemma(question, GroqModel.GEMMA2_9B_IT)
        self.responses["groq"] = response.choices[0].message.content.strip()

    def call_gemini_flash(self, question):
        gemini_api = GeminiApi()
        response = gemini_api.call_gemini_flash(question, self.responses)
        self.responses["gemini_flash"] = response.choices[0].message.content.strip()

    def summarize_responses(self, question):
        return f"總結回答：{self.responses}"

    def mixed_chat(self, question):
        self.threads.append(threading.Thread(target=self.call_samba_nova, args=(question,)))
        self.threads.append(threading.Thread(target=self.call_groq, args=(question,)))
        #self.threads.append(threading.Thread(target=self.call_gemini_flash, args=(question,)))

        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()

        return self.summarize_responses(question)