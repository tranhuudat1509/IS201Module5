import streamlit as st
from modules import helper_functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    helper_functions.write_current_list(todos)

todos = helper_functions.get_current_list()
st.title("Todo App")
st.subheader("This is the todo app.")
st.write("The app increase the productivity.")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(idx)
        helper_functions.write_current_list(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new item", on_change=add_todo, key='new_todo')