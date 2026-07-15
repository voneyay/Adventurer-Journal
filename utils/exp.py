import json
from pathlib import Path


CHARACTER_PATH = Path("data/characters.json")


# 等級稱號
LEVEL_TITLES = {
    1: "見習冒險者",
    2: "初階冒險者",
    3: "旅程記錄者",
    5: "資深冒險者",
    10: "傳說冒險者"
}


def load_characters():

    with open(
        CHARACTER_PATH,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def save_characters(data):

    with open(
        CHARACTER_PATH,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_title(level):

    # 找最高符合等級的稱號
    title = "見習冒險者"

    for lv, name in LEVEL_TITLES.items():
        if level >= lv:
            title = name

    return title



def add_exp(character, amount=10):

    characters = load_characters()

    user = characters[character]


    # 增加經驗
    user["exp"] += amount


    # 完成冒險數增加
    user["completed"] += 1


    level_up = False


    # 升級規則：
    # 需要 EXP = 當前等級 * 50

    need_exp = user["level"] * 50


    if user["exp"] >= need_exp:

        user["exp"] -= need_exp

        user["level"] += 1

        level_up = True


    user["title"] = get_title(
        user["level"]
    )


    save_characters(characters)


    return {
        "level": user["level"],
        "exp": user["exp"],
        "title": user["title"],
        "level_up": level_up,
        "completed": user["completed"]
    }
