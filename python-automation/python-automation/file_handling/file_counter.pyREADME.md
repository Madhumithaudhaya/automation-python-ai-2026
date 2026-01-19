
try:
    with open("sample.txt","r")as file:
        text=file.read()
        lines=text.split("\n")
        words=text.split()
        character=len(text)

        print("lines: ",len(lines))
        print("Words: ",len(words))
        print("Charaters: ",character)
except Exception as e:
    print("error ", e)


