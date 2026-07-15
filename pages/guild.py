import streamlit as st


st.set_page_config(
    page_title="📜 公會任務板",
    page_icon="📜"
)


st.title("📜 公會任務板")


st.write(
    """
🏰 冒險者公會今日委託已發布！


完成任務，
累積經驗，
讓自己的冒險者之路逐漸成長吧！
"""
)


st.divider()



st.subheader(
    "🌱 今日委託"
)



tasks = [
    (
        "📖 記錄今天的冒險",
        10
    ),
    (
        "📚 學習一件新知識",
        5
    ),
    (
        "🌿 好好照顧自己",
        5
    ),
    (
        "⚔️ 完成一件困難的事情",
        10
    )
]



for task, exp in tasks:

    st.checkbox(
        f"{task}   ⭐ +{exp} EXP"
    )
st.divider()


st.subheader(
    "✍️ 自訂冒險委託"
)


custom_task = st.text_input(
    "今天想完成什麼任務？",
    placeholder="例如：完成一個程式功能"
)


custom_exp = st.number_input(
    "任務獎勵 EXP",
    min_value=1,
    max_value=100,
    value=10
)


if st.button("📜 登錄委託"):

    if custom_task:

        st.success(
            f"""
✨ 新委託已登錄！


⚔️ {custom_task}

⭐ 獎勵：
+{custom_exp} EXP
"""
        )

    else:

        st.warning(
            "請先輸入任務內容喔！"
        )
