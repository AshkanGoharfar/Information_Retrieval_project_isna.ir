import string

stop_words = []


def collect_stop_words():
    english_alphabet = list(string.ascii_lowercase)
    for item in list(string.ascii_uppercase):
        english_alphabet.append(item)
    stop_words = ['»', '.', '«', '،', '؟', '"', '#', ')', '(', '*', ',', '-', '/', ':', '[', ']', '،', '?', '…', '۰',
                  '۱',
                  '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '-', '+', '=', '@', '$', '$', '%', '^', '&', '-', '_', '{',
                  '}',
                  '\'', '/', ';', '  ', '>', '<', '•', '٪', '؛']
    persian_alphabet = ["ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
                        "ظ",
                        "ع", "غ", "ف", "ق",
                        "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]

    with open("chars.txt") as file_in:
        for line in file_in:
            stop_words.append(' ' + str(line) + ' ')

    with open("stop_words.txt", encoding="utf8") as file_in:
        for line in file_in:
            stop_words.append(' ' + str(line) + ' ')
    # with open("nonverbal.txt") as file_in:
    #     try:
    #         for line in file_in:
    #             stop_words.append(' ' + str(line) + ' ')
    #     except:
    #         pass
    #
    # with open("persian.txt") as file_in:
    #     try:
    #         for line in file_in:
    #             stop_words.append(' ' + str(line) + ' ')
    #     except:
    #         pass
    #
    # with open("short.txt") as file_in:
    #     try:
    #         for line in file_in:
    #             stop_words.append(' ' + str(line) + ' ')
    #     except:
    #         pass

    for item in english_alphabet:
        stop_words.append(item)

    for item in persian_alphabet:
        stop_words.append(' ' + item + ' ')

    return stop_words

print(collect_stop_words())