import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="📚 冒險圖書館",
    page_icon="📚"
)


st.title("📚 冒險圖書館")


character = st.session_state.get(
    "character",
    "程程"
)


st.write(
    f"""
🧙 目前正在閱讀：

## {character}

過去的冒險紀錄
"""
)


st.divider()


# 找角色資料夾

folder = Path("data") / character


if not folder.exists():

    st.info(
        "目前還沒有任何冒險紀錄。"
    )

else:

    diaries = sorted(
        folder.glob("*.txt"),
        reverse=True
    )


    if len(diaries) == 0:

        st.info(
            "目前還沒有任何冒險紀錄。"
        )


    else:

        selected_diary = st.selectbox(
            "📖 選擇想閱讀的冒險",
            diaries,
            format_func=lambda x: x.stem
        )


        st.divider()


        st.subheader(
            f"📜 {selected_diary.stem} 的冒險"
        )


        with open(
            selected_diary,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()


        st.text(
            content
        )
