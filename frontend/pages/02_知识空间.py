import streamlit as st
import pandas as pd

st.title("知识空间")

# 设置按钮
with st.container():
    col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
    with col2:
        st.button("新建")
    with col3:
        st.button("编辑")
    with col4:
        st.button("删除")


# 创建表格
data = {
    "编号":["1", "2", "3"],
    "名称":["知识空间1", "知识空间2", "知识空间3"],
    "创建时间":["2022-01-01", "2022-01-02", "2022-01-03"]
}

df = pd.DataFrame(data)

st.dataframe(df, hide_index=True, selection_mode="single-row", on_select="rerun")