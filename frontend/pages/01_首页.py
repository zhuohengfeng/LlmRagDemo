import streamlit as st

topContainer = st.container(border=True)

chatContainer = st.container(height="stretch", border=True)

inputContainer = st.container(vertical_alignment="bottom", border=True)

with topContainer:
    st.selectbox("选择知识空间", ["知识空间1", "知识空间2"])


with chatContainer:
    with st.chat_message(name="user"):
        st.write("你好")
    with st.chat_message(name="ai"):
        st.write("你好，我是AI助手")

with inputContainer:
    col1, col2 = st.columns([3, 10])
    with col1:
        st.selectbox("选择用户",["用户A", "用户B"], label_visibility="collapsed")
    with col2:
        st.chat_input("输入")