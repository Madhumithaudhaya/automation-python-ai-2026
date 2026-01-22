# Script:
# This program reads a CSV file and prints only the clean rows.
# A row is considered clean if it contains no empty values.
# The csv.reader() function is used to read the CSV file line by line.
# The all() function checks that every value in the row is non-empty.
# Only rows that satisfy this condition are printed.

import csv

def clean_csv(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if all(row):  # checks no empty values
                print(row)

if __name__ == "__main__":
    clean_csv("data.csv")
