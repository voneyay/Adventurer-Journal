import streamlit as st
import json
from pathlib import Path


st.set_page_config(
    page_title="📖 冒險者名冊",
    page_icon="📖 "
)


st.title("📖 冒險者名冊")


character = st.session_state.get(
    "character",
    "程程"
)


path = Path(
    "data/characters.json"
)


with open(
    path,
    "r",
    encoding="utf-8"
) as f:

    characters = json.load(f)


user = characters[character]


st.subheader(
    f"🧙 {character}"
)


st.write(
    f"""
### Lv.{user['level']}

{user['title']}
"""
)


st.divider()


st.metric(
    "⭐ EXP",
    f"{user['exp']} / {user['level']*50}"
)


st.metric(
    "📖 完成冒險",
    f"{user['completed']} 次"
)


st.divider()


st.write(
    "🌱 繼續累積冒險，讓角色成長吧！"
)
