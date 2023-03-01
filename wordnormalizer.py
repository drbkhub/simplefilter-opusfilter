"""
простой скрипт для исправления слов в которых есть латинские 
или кириллические символы с одинаковым отображением (для русского и английского алфавитов).

>>> milk = "Mолоко"
>>> milk_bad = "Молoко"
>>> milk == milk_bad
False
>>> milk == correct(milk_bad)
True
"""


class LanguageDetectionError(Exception):
    pass


rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


rus_eng_map = {
    "а": "a",
    "е": "e",
    "о": "o",
    "р": "p",
    "с": "c",
    "у": "y",
    "х": "x",
    "А": "A",
    "В": "B",
    "Е": "E",
    "Н": "H",
    "О": "O",
    "Р": "P",
    "С": "C",
    "Т": "T",
    "Х": "X",
    "К": "K",
    "М": "M",
}

all_chars = {char for char in rus_eng_map.keys()}
all_chars.update({char for char in rus_eng_map.values()})

rus_eng_trans_table = str.maketrans(rus_eng_map)
eng_rus_trans_table = str.maketrans(
    dict((value, key) for key, value in rus_eng_map.items())
)

color_rus_trans_table = str.maketrans(
    dict((value, "\033[31m" + value + "\033[0m") for value in rus)
)
color_eng_trans_table = str.maketrans(
    dict((value, "\033[31m" + value + "\033[0m") for value in eng)
)


def _langis(word):
    rus_count = 0
    eng_count = 0
    both = 0
    nowhere = 0
    for char in word:
        if char in rus:
            if char in all_chars:
                both += 1
                continue
            rus_count += 1
        elif char in eng:
            if char in all_chars:
                both += 1
                continue
            eng_count += 1
        else:
            nowhere += 1

    return rus_count, eng_count, both, nowhere


def is_correct(word):
    r, e = False
    for char in word:
        if char in rus:
            if e:
                return False
            r = True
        elif char in eng:
            if r:
                return False
            e = True
    return True


def langis(word):
    rus_count, eng_count, both, nowhere = _langis(word)
    if rus_count == eng_count or rus_count and eng_count:
        # raise LanguageDetectionError
        return

    if rus_count >= eng_count:
        return "rus"
    return "eng"


def correct(word, lang=None):
    lang_detected = langis(word)
    if not lang_detected:
        return word

    if lang == "rus" or lang_detected == "rus":
        table = eng_rus_trans_table
        return word.translate(table)

    elif lang == "eng" or lang_detected == "eng":
        table = rus_eng_trans_table
        return word.translate(table)


def to_bad(word, lang=None):
    table = rus_eng_trans_table
    if lang == "eng" or langis(word) == "eng":
        table = eng_rus_trans_table

    return word.translate(table)


def color(word, lang=None):
    lang = lang if lang else langis(word)
    table = color_rus_trans_table
    if lang == "eng":
        table = color_eng_trans_table

    return word.translate(table)


# print(color(("""together - вместе
# twenty - двацать
# with - с
# call - звонить, звонок
# happen - случаться, происходить
# hear - слышать
# how - как
# idea - идея
# little - мало
# a lot - много""")))
