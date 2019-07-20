import PySimpleGUI as sg
from summarizer import SingleModel
import os

data = ''
min_length = 40
max_length = 300

def printFunc():
    with open(values['Browse'], 'r') as file:
        data = file.read()
        # sg.Popup(data, location=(0, 0))
        # Data = ''.join(data)
        # print(Data)
        print(str(data))
        runSummarizer(str(data), int(min_length), int(max_length))
        sg.Popup('Summarizer running... Check your output.txt file in a few minutes.')

def printMultiline():
    data = values['Multiline']
    runSummarizer(data, min_length, max_length)

def runSummarizer(body, minLength, maxLength):
    model = SingleModel()
    result = model(body, min_length=minLength, max_length=maxLength)
    full = ''.join(result)
    # save output to file, with incremental filename
    i = 0
    while os.path.exists("results/output%s.txt" % i):
        i += 1
    f = open("results/output%s.txt" % i, "w")
    f.write(full)
    f.close()
    sg.Popup('Summary complete.')
    # exit()

layout = [
    [sg.Text('BERT Text Extractor Summarizer')],
    [sg.Text('Min Word Length:'), sg.InputText(key='minLen')],
    [sg.Text('Max Word Length:'), sg.InputText(key='maxLen')],
    [sg.Text('Paste your text here:'), sg.Multiline(key='Multiline', size=(35, 10))],
    [sg.Text('Or browse your text file:', size=(25, 1)), sg.FileBrowse()],
    [sg.Button('Run'), sg.Button('Exit')],
]

window = sg.Window('BERT Launcher', layout)

while True:
    (event, values) = window.Read()
    if event in (None, 'Exit'):
        break
    print(event, values)
    if values['maxLen']:
        max_length = int(values['maxLen'])
    if values['minLen']:
        min_length = int(values['minLen'])
    if values['Multiline']:
        printMultiline()
    if values['Browse']:
        printFunc()
window.Close()
