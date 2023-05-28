from cli import converter
import PySimpleGUI as sg

sg.theme("Black")
label1 = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input_inches = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")

exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[label1, input_feet],
                           [label2, input_inches],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    #
    # My code start:

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    if values['feet'] or values['inches'] is not None:
        print(event, values)
        feet_input = values['feet']
        inches_input = values['inches']
        meters = converter(feet_input, inches_input)
        print(meters)
        window["output"].update(value=meters)

    #
    #
    # feet = float(values["feet"])
    # inches = float(values["inches"])
    #
    # result = converter(feet, inches)
    # window["output"].update(value=f"{result} m", text_color="white")
window.close()
