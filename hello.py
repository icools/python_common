from llm.mixed_llm import MixedLlm

if __name__ == "__main__":
    question = input("請輸入您的問題：")
    mixed_llm = MixedLlm()
    final_answer = mixed_llm.mixed_chat(question)
    print("最終回答：")
    print(final_answer)