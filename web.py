import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']+'\n'
    if new_todo:
        todos.append(new_todo)
        functions.write_todos(todos)

    # clear the input field
    st.session_state['new_todo'] = ''

st.title("Todo App")

for index, todo in enumerate(todos):
    checkbox_todo = st.checkbox(todo, key=todo)
    if checkbox_todo:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add new todo", label_visibility='hidden', placeholder="Add new todo", key='new_todo', on_change=add_todo)
