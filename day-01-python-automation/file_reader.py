
file_path = "sample.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:\n")
        print(content)

except FileNotFoundError:
    print("File not found. Please check the file path.")

except Exception as e:
    print("Something went wrong:", e)
