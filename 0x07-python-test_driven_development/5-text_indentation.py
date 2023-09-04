#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        for n in range(0, len(text)):
            if (text[n] == "." or text[n] == "?"
                or text[n] == ":"):
                print("{}".format(text[n]))
                print()
            elif text[n] == " " and (text[n - 1] == "." 
                or text[n - 1] == "?" or text[n - 1] == ":"):
                continue
            elif (text[n] != "." and text[n] != "?" and text[n] != ":"):
                print(text[n], end="")