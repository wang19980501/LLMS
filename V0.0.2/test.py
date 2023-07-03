import time
import streamlit as st


def long_running_task():
    # 模拟耗时的任务
    time.sleep(5)
    return "任务完成"


with st.spinner("执行中，请稍候..."):
    result = long_running_task()

st.success(result)  # 显示任务结果

# 在任务完成后，取消按钮的禁用状态
st.button("点击此处进行下一个操作", key="next_button")
