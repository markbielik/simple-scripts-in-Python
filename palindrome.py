"""
ASSUMPTIONS OF THE PROGRAM:

The program checks if the entered word is a palindrome

"""


def check_palindrome(word):
    backwards = []
    for litter in word:
        backwards.insert(0, litter)
    backwards = "".join(backwards)
    if backwards == word:
        return f"Word {word} is a palindrome"
    else:
        return f"Word {word} is not palindrome"


user_word = input("Enter Your word for check: ")
print(f"\n{check_palindrome(user_word)}")