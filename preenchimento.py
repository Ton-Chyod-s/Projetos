from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://fapec.org/processo-seletivo/"
processo = '//*[@id="PSS_RPA"]/h5/button'


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wdw = WebDriverWait(driver, 10)

# Abrir a página
driver.get(url)

# Executar um script JavaScript para ocultar o elemento de notificação de cookies
driver.execute_script("document.getElementsByClassName('cookie-notice-container')[0].style.display = 'none';")

#clicar na linha desejada
wdw.until(EC.element_to_be_clickable((By.XPATH, processo)))
driver.find_element(By.XPATH, processo).click()

for i in range(1,2):
    linha = f'//*[@id="accordion"]/div[{i}]'
    xpath_elemento = f'//*[@id="collapse-{i}"]/div/div'
    
    wdw.until(EC.element_to_be_clickable((By.XPATH, xpath_elemento)))
    texto = driver.find_element(By.XPATH, xpath_elemento).text
    
    
    
        
'''# procurar o elemento <a> com o texto "Resultado Final"
wdw.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Resultado Final')]")))
resultado_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Resultado Final')]")
link = resultado_element.get_attribute("href")

print('Link:', link)'''


