import os

try:
    os.remove("file_to_be_deleted")
except FileNotFoundError:
    print("File already deleted!")