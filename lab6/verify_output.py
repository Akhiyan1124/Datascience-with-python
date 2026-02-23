import os

files = [
    "students.txt",
    "sales_data.csv",
]

for file in files:
    if os.path.exists(file):
        print(f"{file} exists.")
    else:
        print(f"{file} NOT found.")
