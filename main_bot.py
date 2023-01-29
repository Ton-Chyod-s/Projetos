from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class bot:
    def __init__(self):
        pass
    def navegador(self):
        self.driver = Chrome()
    def site_whatsapp(self):
         self.driver.get("https://web.whatsapp.com/")
    
whatsapp = bot()

if __name__ == "__main__":
    whatsapp
    whatsapp.navegador()
    whatsapp.site_whatsapp()