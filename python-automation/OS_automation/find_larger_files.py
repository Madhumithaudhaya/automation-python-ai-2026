# Script:
# This program finds and prints files larger than a given size (in MB)
# within a directory and all of its subdirectories.
# It uses os.walk() to recursively traverse the directory structure.
# For each file, it checks the file size using os.path.getsize().
# If the file size is greater than the specified limit, the file path is printed.
# The size is converted from megabytes (MB) to bytes before comparison.

import os

def find_larger_files(directory_path, size_mb):
    size_bytes = size_mb * 1024 * 1024

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.getsize(full_path) > size_bytes:
                print(full_path)

if __name__ == "__main__":
    find_larger_files(".", 0)
