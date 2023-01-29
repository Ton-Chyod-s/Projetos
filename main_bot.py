from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
from selenium.webdriver.support.expected_conditions import (element_to_be_clickable)
import time 


contato = ['comprovantes','SHEIN']

class bot:
    def __init__(self):
        pass
        
    def navegador(self):
        self.driver = Chrome()
    def site_whatsapp(self):
         self.driver.get("https://web.whatsapp.com/")
         self.driver.maximize_window()
         self.wdw = WebDriverWait(self.driver, 1)
                  
    def prog(self,mensagem):
        for i in contato:
            self.wdw.until(element_to_be_clickable(('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')))
            self.driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').clear()
            self.driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(i)
            time.sleep(3)
            
            try:
                self.wdw.until(element_to_be_clickable(('xpath', '//*[@id="pane-side"]/div[1]/div/div/div[1]')))
                self.driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[1]').click()
                # mandar msg
                self.wdw.until(element_to_be_clickable(('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
                self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
                #self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
                time.sleep(1)
            except:
                pass
        
whatsapp = bot()

class app:
    def __init__(self):
        selected_theme = 'Reddit'
        sg.theme(selected_theme)

        self.layout_login = [
            [sg.Button('Web',size=(5,1)), sg.Text('INFRA',justification='c',size=(9,1)),sg.Button('Login',size=(6,1))],
            [sg.Multiline(size=(25,3),key='mensagem')],
            ]

        window = sg.Window('Tux-Netwin', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True,size=(250,75))

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
                    app()

                if event == 'Ok':
                    dados = {
                            "Contato": values['numero']
                        }
                    with open("contatos.json", 'w') as file:
                        json.dump(dados, file, indent=4)

                    window.close()
                    app()

            window.close()
            
        while True:
            event,values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                break
            
            if event == 'Web':
                whatsapp.navegador()
                whatsapp.site_whatsapp()
            
            if event == 'Login':
                whatsapp.prog(values['mensagem'])
    
        window.close()

if __name__ == "__main__":
    app()