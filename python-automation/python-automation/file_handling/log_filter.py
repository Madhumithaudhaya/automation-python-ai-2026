

with open("sample.txt","r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
