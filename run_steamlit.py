import streamlit as st
from llm.mixed_llm import MixedLlm

st.title("混合 LLM 問答系統")

question = st.text_input("請輸入您的問題：")

if st.button("提交"):
    mixed_llm = MixedLlm()
    final_answer = mixed_llm.mixed_chat(question)
    st.write("最終回答：")
    st.write(final_answer)