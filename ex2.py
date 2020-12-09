some_word = str(input("Please enter some word or palindrome: "))
word = some_word[::-1]

def palindrom(some_word, word):
    if some_word == word:
        return "Yes, it`s palindrome"
    else:
        return "No, it`s not palindrome"

print(palindrom(some_word, word))
