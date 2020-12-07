def palindrom():
    some_word = str(input("Please enter some word or palindrome: "))
    word = some_word[::-1]
    if some_word == word:
        return "Yes, it`s palindrome"
    else:
        return "No, it`s not palindrome"

print(palindrom())