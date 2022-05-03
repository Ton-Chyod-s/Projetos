import PySimpleGUI as sg                              #pip install PySimpleGUI==2.7.0 #pip install --no-cache-dir --upgrade PySimpleGUI

from datetime import date, timedelta                  #importa data e hora   
         
data_hora = date.today()                              #importa a data atual
data = data_hora.strftime('%d/%m/%Y')                 #Formata a data para padrão brasileiro



sg.theme('DarkGrey')                                  # tema da janela

class TelaPython:
        layout = [ 
            
            [sg.Text('Calculo Contas', size=(25, 1), justification='center', font=("Helvetica", 13))],
            [sg.Text('')],
            [sg.Text('Salario:', size=(13, 1)), sg.InputText(key='salario', size=(13, 1))],
            [sg.Text('Cartão:', size=(13, 1)), sg.InputText(key='cartao', size=(13, 1))],
            [sg.Text('Boleto Oi:', size=(13, 1)), sg.InputText(key='bl_1', size=(13, 1))],
            [sg.Text('Boleto CasseMS:', size=(13, 1)), sg.InputText(key='bl_2', size=(13, 1))],
            [sg.Text('Boleto Iss:', size=(13, 1)), sg.InputText(key='iss', size=(13, 1))],
            [sg.Submit('Oks'),sg.Button('Cancelar')],
            
        ]

        janela = sg.Window('', layout, font=("Helvetica", 10))
        
        
            
        while True:
            event, values = janela.Read()

            if event in (None,'Cancelar'):
                break    
  
            salario = float(values['salario'])        
            cartao = float(values['cartao'])
            boleto_1 = float(values['bl_1'])
            boleto_2 = float(values['bl_2'])
            boleto_3 = float(values['iss'])
                
            soma = (cartao + boleto_1 + boleto_2 + boleto_3)
            sub = (salario - soma)

            janela.close()

            if event in (None,'Oks'):
                sg.popup_no_titlebar('Soma Total ',round(soma,2),'Resultado',salario, '-', round(soma,2),round(sub,2))

           
#salario  1039.43

#cartão de credito 557.07
#boleto CasseMS 183.35
#boleto Oi 54.12
#boleto Iss 146
