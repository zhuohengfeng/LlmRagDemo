import streamlit as st
import pandas as pd

st.title("知识库")

# 设置按钮
with st.container():
    col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
    with col2:
        st.button("上传")
    with col3:
        st.button("编辑")
    with col4:
        st.button("删除")


# 创建表格
data = {
    "编号":["1", "2", "3"],
    "文件名":["文件名1", "文件名2", "文件名3"],
    "文件类型": ["txt", "pdf", "docx"],
    "归属空间": ["空间1", "空间2", "空间3"],
    "创建时间":["2022-01-01", "2022-01-02", "2022-01-03"]
}

df = pd.DataFrame(data)

st.dataframe(df, hide_index=True, selection_mode="single-row", on_select="rerun")