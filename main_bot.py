import pywhatkit 
import keyboard
import time
from datetime import datetime
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('Contatos'), sg.InputText()],
            [sg.Text('Mensagem'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Bot Whatsapp', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


'''
contato = ['+5567991799956']

while len(contato) >= 1:
    # Send a WhatsApp Message to a Contact 
    pywhatkit.sendwhats_image(contato[0],'1662693303800 (1).jpg', "um teste ae", datetime.now().hour, datetime.now().minute + 1)
    del contato[0]
    time.sleep(5)
    keyboard.press_and_release('ctrl + w')
'''