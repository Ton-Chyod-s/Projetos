import pywhatkit 
import keyboard
import time
from datetime import datetime
import PySimpleGUI as sg

class bot:
    def __init__(self):
        self.contato = ['+5567991799956']
        self.imagem = '1662693303800 (1).jpg'

        def mensagem_imagem(self):
            while len(self.contato) >= 1:
                # Send a WhatsApp Message to a Contact 
                pywhatkit.sendwhats_image(self.contato[0],self.imagem, "um teste ae", datetime.now().hour, datetime.now().minute + 1)
                del self.contato[0]
                time.sleep(5)
                keyboard.press_and_release('ctrl + w')

        def mensagem_texto(self):
            # Send a WhatsApp Message to a Contact at 1:30 PM
            pywhatkit.sendwhatmsg(self.contato[0], "um teste ae", datetime.now().hour, datetime.now().minute + 1)
            del self.contato[0]
            time.sleep(5)
            keyboard.press_and_release('ctrl + w')

sg.theme('DarkAmber')

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()