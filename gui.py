import FreeSimpleGUI as sg
import time
import functions

now = time.strftime("%b %d, %A,  %Y %H:%S")

sg.theme("Black")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
window = sg.Window(now,
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font=('Helvetica', 16))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip()

                todos = functions.get_todos()

                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item first!", font=('Helvetica', 20))
            except ValueError:
                sg.popup("This todo is no longer in the list. Please try again.", font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()

                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=('Helvetica', 20))
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
window.close()