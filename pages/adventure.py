import streamlit as st
from datetime import date
from pathlib import Path
import json


from utils.save import save_adventure, load_today_note
from utils.exp import add_exp
from utils.translate import translate_to_english



st.set_page_config(
    page_title="⚔️ 今日冒險紀錄",
    page_icon="⚔️"
)



# =====================
# 回城卷軸
# =====================

if st.button("🏰 回城卷軸"):

    st.switch_page(
        "app.py"
    )



st.title(
    "⚔️ 今日冒險紀錄"
)



# =====================
# 角色確認
# =====================

character = st.session_state.get(
    "character",
    None
)



if character is None:


    st.warning(
        "🏰 尚未選擇冒險者"
    )


    DATA_PATH = Path(
        "data/characters.json"
    )


    with open(
        DATA_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        characters = json.load(f)



    character = st.selectbox(
        "🧙 選擇今天的冒險者",
        list(characters.keys())
    )


    if st.button(
        "⚔️ 開始今日冒險"
    ):

        st.session_state["character"] = character

        st.rerun()



else:

    st.write(
        f"""
✨ 今日由：

## 🧙 {character}

來記錄冒險旅程。
"""
    )



st.divider()



# =====================
# 今日冒險內容
# =====================


weather = st.radio(
    "☀️ 今日天氣",
    [
        "晴天",
        "多雲",
        "陰天",
        "雨天",
        "不想觀察"
    ]
)



adventure_type = st.selectbox(
    "📅 今日探險類型",
    [
        "工作日",
        "學習日",
        "宅家日",
        "出門探險",
        "旅行日",
        "放空日",
        "特殊事件"
    ]
)



quest = st.selectbox(
    "⚔️ 今日主線任務",
    [
        "工作",
        "開會",
        "寫程式",
        "閱讀",
        "看動畫",
        "玩遊戲",
        "運動",
        "彈鋼琴"
    ]
)



# 載入今天舊日記

today_note = load_today_note(
    character
)



note = st.text_area(
    "💬 勇者小記",
    value=today_note,
    placeholder="今天發生了什麼冒險呢？"
)



st.divider()



# =====================
# 日記內容
# =====================


diary = f"""
日期：
{date.today()}


角色：
{character}


天氣：
{weather}


今日類型：
{adventure_type}


主線任務：
{quest}


勇者小記：
{note}


EXP：
+10
"""



# =====================
# 翻譯年糕
# =====================

if st.button(
    "🍡 翻譯年糕"
):

    english_note = translate_to_english(
        note
    )


    st.subheader(
        "🍡 勇者小記英文版"
    )


    st.write(
        english_note
    )



st.divider()



# =====================
# 收錄冒險
# =====================

if st.button(
    "📖 收錄冒險"
):


    file = save_adventure(
        character,
        diary
    )


    result = add_exp(
        character,
        10
    )


    st.success(
        f"""
✨ 冒險已收錄！


📖 日記：
{file}


⭐ 獲得 EXP：
+10


目前狀態：

Lv.{result['level']}
{result['title']}


EXP：
{result['exp']}/{result['level']*50}


完成冒險：
{result['completed']} 次
"""
    )



    if result["level_up"]:

        st.balloons()

        st.success(
            "🎉 恭喜升級！新的冒險篇章開啟！"
        )
