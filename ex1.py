text_file = open("home_task.txt", "w", encoding='utf-8')
while True:
    some_text = input("Please enter some sentence or ENTER for exit: ")
    if some_text != "":
        text_file.write(some_text+"\n")
    if some_text == "":
        break
text_file.close()