from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg


options = Options()
#options.add_argument('--headless')

# Definir um diretório diferente para o perfil do Chrome
options.add_argument("user-data-dir=/caminho/do/diretorio/selenium")

# Verificar se o ChromeDriver está instalado corretamente
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except Exception as e:
    print(f"Erro ao instalar o ChromeDriver: {e}")

wdw = WebDriverWait(driver, 1)

# Abrir a página
url = "https://fapec.org/processo-seletivo/"
driver.get(url)

# Executar um script JavaScript para ocultar o elemento de notificação de cookies
driver.execute_script("document.getElementsByClassName('cookie-notice-container')[0].style.display = 'none';")

# Encontrar o botão do processo desejado
processo_text = "Processo Seletivo Simplificado 031/2023 – contratação temporária – Inscrições abertas 14/06/2023 à 16/06/2023 até às 23:59"
processo_xpath = f"//button[contains(text(), '{processo_text}')]"
wdw.until(EC.element_to_be_clickable((By.XPATH, processo_xpath)))
driver.find_element(By.XPATH, processo_xpath).click()

resultados = []
# Percorrer os elementos dentro do card
for tabela in range(1, 5):
    xpath_elemento = f"//*[@id='collapse-1']/div/div[{tabela}]"
    try:
        wdw.until(EC.element_to_be_clickable((By.XPATH, xpath_elemento)))
        texto = driver.find_element(By.XPATH, xpath_elemento).text
        link_elemento = driver.find_element(By.XPATH, "//*[@class='arquivo-processo-seletivo']//a")
        link = link_elemento.get_attribute("href")
        
        # Adicionar os resultados à lista
        resultados.append((texto , link))
        
    except:
        print('Não há mais elementos')
        break
    
#fechar driver
driver.quit()

if len(resultados) > 0:
    primeiro_elemento = resultados[0]
    texto_elemento1, link_elemento1 = primeiro_elemento
    try:
        segundo_elemento = resultados[1]
        texto_elemento2, link_elemento2 = primeiro_elemento
        sg.popup('', texto_elemento1, link_elemento1, keep_on_top=True)
    except:
        pass
    sg.popup('', texto_elemento1, link_elemento1, keep_on_top=True)
else:
    print('A lista de resultados está vazia.')


    