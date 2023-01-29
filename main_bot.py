from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
from selenium.webdriver.support.expected_conditions import (element_to_be_clickable)
import time 

menssagem = 'lol'
contato = ['amor','Minha Oi']

class bot:
    def __init__(self):
        pass
    def navegador(self):
        self.driver = Chrome()
    def site_whatsapp(self):
         self.driver.get("https://web.whatsapp.com/")
         self.driver.maximize_window()
         self.wdw = WebDriverWait(self.driver, 60)
         
    def prog (self):
        for i in contato:
            self.wdw.until(element_to_be_clickable(('xpath', f"//*[@title='{i}']")))
            self.driver.find_element(By.XPATH,f"//*[@title='{i}']").click()
            # mandar msg
            self.wdw.until(element_to_be_clickable(('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
            self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(menssagem)
            time.sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    
whatsapp = bot()

class app:
    def __init__(self):
        selected_theme = 'Reddit'
        sg.theme(selected_theme)

        self.layout_login = [
            [sg.Button('Web',size=(5,1)), sg.Text('INFRA',justification='c',size=(9,1)),sg.Button('Login',size=(6,1))],
            [sg.Combo(['Firefox','Chrome','Internet Explorer','Edge']),sg.Checkbox('V-tal',key='home')],
            ]

        window = sg.Window('Tux-Netwin', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True,size=(250,75))

        while True:
            event,values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                break
            
            if event == 'Web':
                whatsapp.navegador()
                whatsapp.site_whatsapp()
            
            if event == 'Login':
                whatsapp.prog()
    
        window.close()

if __name__ == "__main__":
    app()