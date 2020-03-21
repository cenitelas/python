import os

tree = os.walk(".")
extensions = ('.cpp', '.c', '.cs', '.cls', '.vbp,', '.cxx', '.cc', '.java')


def get_files_path(tree):
    files_path = []
    for d, dirs, files in tree:
        progFiles = filter(lambda x: x.endswith(extensions), files)
        for f in progFiles:
            files_path.append(f"{d}/{f}")
    return files_path


def get_todo_in_file(path):
    todos = []
    with open(path) as file:
        lines = file.readlines()
    for line in lines:
        if line.find("TODO") >= 0:
            todo = line.split("TODO ")[1]
            todos.append((lines.index(line), todo))
    return todos


tasks = open('tasks.txt', 'w')

for path in get_files_path(tree):
    todos = get_todo_in_file(path);
    if len(todos) > 0:
       file_name = path.split("/")[len(path.split("/"))-1]
       for line, todo in todos:
           tasks.writelines(f"В файле {file_name} по пути {path} есть TODO:\n строка {line}: {todo}\n\n")

tasks.close()

