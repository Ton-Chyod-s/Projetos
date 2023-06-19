from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://fapec.org/processo-seletivo/"
processo = "//button[contains(text(), 'Processo Seletivo Simplificado 031/2023 – contratação temporária – Inscrições abertas 14/06/2023 à 16/06/2023 até às 23:59')]"

options = webdriver.ChromeOptions()
# options.add_argument('--headless'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wdw = WebDriverWait(driver, 1)

# Abrir a página
driver.get(url)

# Executar um script JavaScript para ocultar o elemento de notificação de cookies
driver.execute_script("document.getElementsByClassName('cookie-notice-container')[0].style.display = 'none';")

for linha in range(1,2):
    processo =f'//*[@id="accordion"]/div[{linha}]'
    #clicar na linha desejada
    wdw.until(EC.element_to_be_clickable((By.XPATH, processo)))
    sleep(1)
    driver.find_element(By.XPATH, processo).click()

    for i in range(1,3):
        xpath_elemento = f'//*[@id="collapse-{linha}"]/div/div[{i}]'
        try:
            wdw.until(EC.element_to_be_clickable((By.XPATH, xpath_elemento)))
            texto = driver.find_element(By.XPATH, xpath_elemento).text
            print(texto)
        except:
            print('não tem mais linha')
            break
        
'''# procurar o elemento <a> com o texto "Resultado Final"
wdw.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Resultado Final')]")))
resultado_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Resultado Final')]")
link = resultado_element.get_attribute("href")

print('Link:', link)'''


