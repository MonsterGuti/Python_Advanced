import os

files = {}
directory = "../"  # You can change this to "." for current dir


def get_files(folder, level):
    if level == -1:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = os.path.splitext(element)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        elif os.path.isdir(f):
            get_files(f, level - 1)


get_files(directory, 1)

sorted_extensions = sorted(files.items())

with open("report.txt", "w") as report:
    for ext, file_list in sorted_extensions:
        report.write(f"{ext}\n")
        for file in sorted(file_list):
            report.write(f"- - - {file}\n")
