import PySimpleGUI as sg
import  funcao 

class interface:
    def __init__(self):
        #tela inicial 
        sg.theme('Reddit')
        layout_login = [
            [sg.Output(size=(15,1))],
            [sg.Btn('7',size=(2,1)),sg.Btn('8',size=(2,1)),sg.Btn('9',size=(2,1)),sg.Btn('/',size=(2,1))],
            [sg.Btn('4',size=(2,1)),sg.Btn('5',size=(2,1)),sg.Btn('6',size=(2,1)),sg.Btn('x',size=(2,1))],
            [sg.Btn('1',size=(2,1)),sg.Btn('2',size=(2,1)),sg.Btn('3',size=(2,1)),sg.Btn('-',size=(2,1))],
            [sg.Btn(',',size=(2,1)),sg.Btn('0',size=(2,1)),sg.Btn('=',size=(2,1),key='='),sg.Btn('+',size=(2,1))],
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

