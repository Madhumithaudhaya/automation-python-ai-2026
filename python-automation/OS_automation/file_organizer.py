import os
import shutil
path =r"D:\GITHUB\automation\folder_organizer.py"
for file in os.listdir(path):
    if file.endswith(".jpg"):
        os.makedirs("Images",exist_ok=True)
        shutil.move(f"{path}/{file}","Images")

    elif file.endswith(".pdf"):
        os.makedirs("Documents",exist_ok=True)
        shutil.move(f"{path}/{file}","Documents")

    elif file.endswith(".py"):
        os.makedirs("Python",exist_ok=True)
        shutil.move(f"{path}/{file}","Python")
