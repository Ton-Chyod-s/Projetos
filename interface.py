import PySimpleGUI as sg
import  funcao 

class interface:
    def __init__(self):
        #tela inicial 
        sg.theme('Reddit')
        layout_login = [
            [sg.Output(size=(28,2))],
            [sg.Text('Input\t'),sg.Input(size=(15,1),key='calculo'),sg.Btn('OK')],
            ]

        window = sg.Window('Calculadora',layout=layout_login, finalize = True)
        
        while True:
            event, values = window.read()    
            if event == sg.WIN_CLOSED:
                break
            
            if event == 'OK':
                funcao.calc(values['calculo'])
                    
        window.close()
        
interface()

