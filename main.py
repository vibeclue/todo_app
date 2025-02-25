def get_todos(filepath: str='todos.txt')-> list:
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r', encoding='UTF-8') as file:
        return file.readlines()

def update_todo_list(todo_list: list, filepath: str='todos.txt') -> None:
    """ Write the to-do items list to a text file """
    with open(filepath, 'w', encoding='UTF-8') as file:
        file.writelines(todo_list)

print("Hey! It's your todo list!")
print()


while True:
    user_action = input('Enter your action: ').lower().strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo =" ".join(user_action.split()[1:])
        todos = get_todos()
        todos.append(todo + '\n')
        update_todo_list(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for i in range(len(todos)):
            print(f'{i + 1}) {todos[i].capitalize().rstrip()}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action.split()[1]) - 1
        except ValueError:
            print("You need to enter a number of todo list!")
        else:
            todos = get_todos()
            todos[number] = input("Enter new todo: ") + "\n"
            update_todo_list(todos)

    elif user_action.startswith('del'):
        try:
            number = int(user_action.split()[1]) - 1
        except ValueError:
            print("You need to enter a number!")
        else:
            todos = get_todos()
            deleted_item = todos.pop(number)
            print(f'You have removed "{deleted_item.strip()}"')
            update_todo_list(todos)

    elif user_action.startswith('exit'):
        break
    else:
        print("unknown command")


print("The program is closed")