from googletrans import Translator


def translate_to_english(text):

    translator = Translator()

    result = translator.translate(
        text,
        src="zh-tw",
        dest="en"
    )

    return result.text
