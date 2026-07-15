from pathlib import Path
from datetime import date


def save_adventure(
    character,
    content
):

    folder = Path("data") / character

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    today = date.today().isoformat()

    file_path = folder / f"{today}.txt"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return file_path



def load_today_note(character):

    folder = Path("data") / character

    today = date.today().isoformat()

    file_path = folder / f"{today}.txt"


    # 今天沒有寫過日記
    if not file_path.exists():
        return ""


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()


    # 找勇者小記區域
    if "勇者小記：" in content:

        note = content.split(
            "勇者小記：",
            1
        )[1]


        # 如果後面還有其他欄位，切掉
        if "EXP：" in note:

            note = note.split(
                "EXP：",
                1
            )[0]


        return note.strip()


    return ""
