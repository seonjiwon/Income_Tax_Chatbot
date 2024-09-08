# pip install langchain langchainhub langchain_commuinty langchain-core langchain-openai python-dotenv langchain-pinecone
import streamlit as st

from dotenv import load_dotenv
from llm import get_ai_response


st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

st.title("🤖 소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다!")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []


print(f"before == {st.session_state.message_list}")

#다음 질문이 들어오면 지금 까지의 질문을 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#질문이 들어오면 그 질문을 쓰고 저장
if user_question := st.chat_input(placeholder="소득세에 관련된 모든것을 답해 드립니다!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})


print(f"after == {st.session_state.message_list}")