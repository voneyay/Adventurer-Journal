import streamlit as st
import json
from pathlib import Path


st.set_page_config(
    page_title="🏰 冒險者公會",
    page_icon="🏰"
)


DATA_PATH = Path("data/characters.json")


def load_characters():

    with open(
        DATA_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



characters = load_characters()



# 公會首頁

st.title("🏰 冒險者公會")


st.write(
    """
🌟 歡迎回來，冒險者~


新的旅程正在等待開啟( •̀ᄇ• ́)ﻭ✧ 


今天要由誰來紀錄自己的冒險呢？
"""
)


st.divider()



st.subheader(
    "📜 冒險者名單"
)



for name, info in characters.items():


    st.subheader(
        f"✨ {name}"
    )


    st.write(
        f"""
🪄 職業：
{info['title']}


⭐ 等級：
Lv.{info['level']}


🌟 經驗值：
{info['exp']} EXP


📖 已完成冒險：
{info['completed']} 次
"""
    )


    if st.button(
        f"⚔️ 開始 {name} 的冒險",
        key=name
    ):

        st.session_state["character"] = name

        st.switch_page(
            "pages/adventure.py"
        )


    st.divider()
