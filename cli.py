from functions import *

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        if not todos:
            print("The list is empty.")  # If the list is empty, print a message
        else:
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Edit your todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            removed_todo = todos[number-1].strip('\n')
            todos.pop(number-1)

            write_todos(todos)
            print(f"Todo number {number} ('{removed_todo}') was completed and removed.")
        except IndexError:
            print("There is no todo with this number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("Bye")
