import PySimpleGUI as sg

layout = [
    [sg.Text('What is your name?'),sg.InputText('',key='name')],
    [sg.Text('How old are you?'),sg.InputText('',key='age')],
    [sg.Button('OK'),sg.Button('Cancel')]
]
window = sg.Window('My First Simple GUI App', layout, size=(800,480))

while True:
    event, values = window.read()
    # if event == sg.WIN_CLOSED or event == 'Cancel':
    if event in (None, 'Cancel'):
        break

    sg.Popup(f"Hi {values['name']}. You are {values['age']} years old")
window.close()