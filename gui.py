from ast import Index

import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')


current_time = sg.Text('', key='current_time')
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button("Add", size=7)

list_box = sg.Listbox(values=functions.get_todos(), size=(57, 10), key='todos', enable_events=True)
edit_button = sg.Button('Edit', size=7)

complete_button = sg.Button('Complete', size=9)
exit_button = sg.Button('Exit', size=7)

window = sg.Window('TODO LIST',
                   layout=[[current_time],
                           [label, input_box, add_button],
                           [list_box, edit_button],
                           [complete_button, exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=500)
    window['current_time'].update(value=time.strftime("%d.%m.%Y %H:%M"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'].capitalize() + '\n')
            functions.update_todo_list(todos)

            window['todos'].update(values=todos)  # update listbox

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.update_todo_list(todos)

                window['todos'].update(values=todos)  # update listbox
            except IndexError:
                sg.popup("Please, select an item first.", title='Warning!', font=('Helvetica', 12),
                         button_justification='right')

        case 'todos':  # update input window whenever user click in list box
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)
                functions.update_todo_list(todos)

                window['todo'].update(value='')       # clear input field
                window['todos'].update(values=todos)  # update listbox
            except IndexError:
                sg.popup("Please, select an item first.", title='Warning!', font=('Helvetica', 12),
                         button_justification='right')

        case 'Exit':
            break

        case sg.WINDOW_CLOSED:
            break

window.close()




