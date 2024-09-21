# gemini_api.py
import os
from enum import Enum
import google.generativeai as genai

class GeminiModel(Enum):
    GEMINI_1_5_FLASH_EXP_0827 = "gemini-1.5-flash-exp-0827"

class GeminiApi: 
    DEFAULT_GENERATION_CONFIG = {
        "temperature": 0.8,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    def __init__(self):
        GEMINI_KEY = os.getenv("GEMINI_KEY")
        genai.configure(api_key=GEMINI_KEY)

    def call_gemini_flash(self, question, generation_config=None):
        print("gemini flash thinking...")
        
        if generation_config is None:
            generation_config = self.DEFAULT_GENERATION_CONFIG
        
        model = genai.GenerativeModel(
            model_name=GeminiModel.GEMINI_1_5_FLASH_EXP_0827.value,
            generation_config=generation_config,
        )
        
        chat_session = model.start_chat(history=[])
        return chat_session.send_message(question)