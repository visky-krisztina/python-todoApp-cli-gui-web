import os
FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    # If the file does not exist, create it
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write('')  # Create an empty file

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")