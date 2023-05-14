import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
"""IN the layout each row is separated by []"""
window.read()
"""It reads the file and displays the gui and stop further operations
after it"""

window.close()