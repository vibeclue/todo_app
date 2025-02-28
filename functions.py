FILEPATH = 'todos.txt'


def get_todos(filepath: str=FILEPATH)-> list:
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r', encoding='UTF-8') as file:
        return file.readlines()

def update_todo_list(todo_list: list, filepath: str=FILEPATH) -> None:
    """ Write the to-do items list to a text file """
    with open(filepath, 'w', encoding='UTF-8') as file:
        file.writelines(todo_list)