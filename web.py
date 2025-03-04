import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo:
        todos.append(new_todo + '\n')
        functions.update_todo_list(todos)


st.title("Todo app")
st.subheader("List of todo:")

# todos list
todos: list = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo: ",
              label_visibility='hidden',
              placeholder="Enter a new todo...",
              on_change=add_todo,
              key="new_todo")


