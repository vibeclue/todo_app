import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button("Add")

exit_button = sg.Button('Exit')

window = sg.Window('TODO LIST',
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.update_todo_list(todos)
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break
window.close()




