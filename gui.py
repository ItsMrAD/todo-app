import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock', size=43)
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo", size=36, key="todo")
add_button = sg.Button(size=10, image_source="add.png",
                       mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(size=10, image_source="edit.png",
                        mouseover_colors="LightBlue2",
                        tooltip="Edit Todo", key="Edit")
complete_button = sg.Button(size=10, image_source="complete.png",
                            mouseover_colors="LightBlue2",
                            tooltip="Complete Todo", key="Complete")
exit_button = sg.Button(size=10, key="Exit", image_source="exit.png",
                        mouseover_colors="LightBlue2",
                        tooltip="Exit Program")

window = sg.Window('My To-Do App',
                   layout=[[clock, exit_button],
                           [label],
                           [input_box, add_button, edit_button, complete_button],
                           [list_box]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip()

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select an item first",
                         font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                print(todo_to_complete)
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select an item first",
                         font=("Helvetica", 15))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0].strip())
        case sg.WIN_CLOSED:
            break

window.close()
