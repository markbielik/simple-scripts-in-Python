"""
Simple app to censor text.
"""


def censor(word, text):
    censor_text = []
    ver_text = text.split(" ")
    for single_word in ver_text:
        if single_word == word:
            censor_text.append("****")
        else:
            censor_text.append(single_word)
    return " ".join(censor_text)


def censor2(word, text):
    censor_text = []
    ver_text = text.split(" ")
    for single_word in ver_text:
        len_word = len(word) - len(single_word)
        if single_word[1:len_word-1] == word[1:-1]:
            censor_text.append("****")
        else:
            censor_text.append(single_word)
    return " ".join(censor_text)


user_word = input("Search word: ")
user_text = input("Text for search: \n")
print("\nCensor version - censors only the exact word as given by the user")
print(censor(user_word, user_text))
print("\nCensor2 version - more accurate than the previous one")
print(censor2(user_word, user_text))
