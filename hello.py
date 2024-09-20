from typing import Final
from samba_nova import chat_with_samba_nova

def chat(message):
    return chat_with_samba_nova(message)

content: Final = chat("到底是公蝦小還是母蝦小").choices[0].message.content

print(content)
