import PySimpleGUI as sg
import salario


selected_theme = 'Reddit'
sg.theme(selected_theme)

layout_login = [
        [sg.Text('Salário:\t'),sg.Stretch(),sg.Input(size=(6,1),key='salario'),sg.Btn('ok',size=(3,1))],
        [sg.Output(size=(25,6))],
        ]

window = sg.Window('Divisão', icon=' ',layout=layout_login, keep_on_top=True, finalize = True)

while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
            break
        
        if event == 'ok':
            salario.salario(values['salario'])

window.close()