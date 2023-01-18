import pywhatkit 
import keyboard
import time
from datetime import datetime
import PySimpleGUI as sg
import json
import os

def endereco(procurar = True):
    if procurar:
        sg.theme('Reddit')
        local = sg.popup_get_folder(r'Selecione o caminho dos Arquivos',' ',r'C:\Users\klayton.dias\Desktop')
        try:
            caminho = os.chdir(local)
        except:
            pass
        aplicativo()
        
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

class aplicativo:
    def __init__(self):
        sg.theme('Reddit')
        menu_def = ['&Arquivo', ['&Contato', '&Mensagem', '&Imagem']],

        layout = [  
            [sg.Menu(menu_def)],
            [sg.Text(size=(16,5))],
            [sg.Button('Enviar'), sg.Button('Sair'), sg.Button('Test')] 
            ]

        # Create the Window
        aplicativo_window = sg.Window('Bot Whatsapp', layout, keep_on_top=True,)

        def contato():
            layout = [
                [sg.Text('Contato')],
                [sg.Multiline(size=(16,5),key='numero')],
                [sg.Button('Ok'), sg.Button('Voltar')] ]

            # Create the Window
            window = sg.Window('Bot Whatsapp', layout)

            # Event Loop to process "events" and get the "values" of the inputs
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:   # if user closes window or clicks cancel
                    break

                if event == 'Voltar':
                    window.close()
                    aplicativo()

                if event == 'Ok':
                    dados = {
                            "Contato_1": '+55' + values['numero']
                        }
                    with open("contatos.json", 'w') as file:
                        json.dump(dados, file, indent=4)

                    window.close()
                    aplicativo()

            window.close()
            
        def mensagem():
            layout = [
                [sg.Text('Mensagem')],
                [sg.Multiline(size=(16,5),key='mensagem')],
                [sg.Button('Ok'), sg.Button('Voltar')] ]

            # Create the Window
            window = sg.Window('Bot Whatsapp', layout)

            # Event Loop to process "events" and get the "values" of the inputs
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:   # if user closes window or clicks cancel
                    break

                if event == 'Voltar':
                    window.close()
                    aplicativo()

                if event == 'Ok':
                    dados = {
                            "msg": values['mensagem']
                        }
                    with open("credenciais.json", 'w') as file:
                        json.dump(dados, file, indent=4)

                    window.close()
                    aplicativo()

            window.close()

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event,values = aplicativo_window.read()
            if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                break

            if event =='Contato':
                aplicativo_window.close()
                contato()

            if event == 'Imagem' :
                aplicativo_window.close()
                endereco()

            if event == 'Mensagem' :
                aplicativo_window.close()
                mensagem()

            if event == 'Test':
                with open("credenciais.json", encoding='utf-8') as meu_json:
                        dado = json.load(meu_json)
                info = dado['email']   
                tr = dado['login']
                senha = dado['senha']

                print(info, tr, senha)

        aplicativo_window.close()

if __name__ == '__main__':
    aplicativo()
    