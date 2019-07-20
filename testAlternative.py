import PySimpleGUI as sg
import subprocess

# Please check Demo programs for better examples of launchers      
def ExecuteCommandSubprocess(command, *args):
    try:
        sp = subprocess.Popen([command, *args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        pass

def printFunc(value):
    with open(value['Browse'], 'r') as file:
        data = file.read()
        # print(data)
        sg.Popup(data)

layout = [
    [sg.Text('Script output....', size=(40, 1))],
    [sg.Output(size=(88, 20))],
    [sg.Button('script1'), sg.FileBrowse(), sg.Button('Summarize'), sg.Button('EXIT')],
    [sg.Text('Manual command', size=(15, 1)), sg.InputText(focus=True), sg.Button('Run', bind_return_key=True)]
]


window = sg.Window('BERT launcher', layout)

# ---===--- Loop taking in user input and using it to call scripts --- #      

while True:      
    (event, value) = window.Read()
    if event == 'EXIT' or event is None:
        break # exit button clicked
    if event == 'script1':
        ExecuteCommandSubprocess('python', '--version')
    elif event == 'Browse':
        # printFunc(value)
        ExecuteCommandSubprocess('python', '--version')
    elif event == 'Summarize':
        ExecuteCommandSubprocess('start.py')
    elif event == 'Run':
        ExecuteCommandSubprocess(value[0])