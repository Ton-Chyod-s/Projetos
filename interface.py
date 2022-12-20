import PySimpleGUI as sg
import  funcao as calc

class interface:
    def __init__(self):
        #tela inicial 
        sg.theme('Reddit')
        layout_login = [
            [sg.Output(size=(22,3))],
            [sg.Text('Input\t'),sg.Input(size=(15,1))],
            ]

        window = sg.Window('Calculadora',layout=layout_login, finalize = True)
        
        while True:
            event, values = window.read()    
            if event == sg.WIN_CLOSED:
                break
            
            if event == '=':
                pass
                    
        window.close()
        
interface()

