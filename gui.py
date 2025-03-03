import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button("Add", size=7)

list_box = sg.Listbox(values=functions.get_todos(), size=(57, 10), key='todos', enable_events=True)
edit_button = sg.Button('Edit', size=7)

complete_button = sg.Button('Complete', size=7)
exit_button = sg.Button('Exit', size=7)

window = sg.Window('TODO LIST',
                   layout=[[label, input_box, add_button],
                           [list_box, edit_button],
                           [complete_button, exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event, values, sep='\n')
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'].capitalize() + '\n')
            functions.update_todo_list(todos)

            window['todos'].update(values=todos)  # update listbox

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.update_todo_list(todos)

            window['todos'].update(values=todos)  # update listbox

        case 'todos':  # update input window whenever user click in list box
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            todos = functions.get_todos()
            todo_to_complete = values['todos'][0]
            todos.remove(todo_to_complete)
            functions.update_todo_list(todos)

            window['todo'].update(value='')       # clear input field
            window['todos'].update(values=todos)  # update listbox

        case 'Exit':
            break

        case sg.WINDOW_CLOSED:
            break

window.close()




