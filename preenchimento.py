from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg
from time import sleep
import webbrowser

selected_theme = 'Reddit'
sg.theme(selected_theme)
options = Options()
#options.add_argument("--headless")  # Executar o navegador em modo headless (sem exibição)

# Definir um diretório diferente para o perfil do Chrome
options.add_argument("user-data-dir=/caminho/do/diretorio/selenium")

# Verificar se o ChromeDriver está instalado corretamente

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wdw = WebDriverWait(driver, 1)

# Abrir a página
url = "https://fapec.org/processo-seletivo/"
driver.get(url)

# Executar um script JavaScript para ocultar o elemento de notificação de cookies
driver.execute_script("document.getElementsByClassName('cookie-notice-container')[0].style.display = 'none';")

# Encontrar o botão do processo desejado
processo_text = "Processo Seletivo Simplificado 031/2023 – Contratação Temporária – Inscrições abertas 14/06/2023 à 20/06/2023 até às 18:00"
processo_xpath = f"//button[contains(text(), '{processo_text}')]"
sleep(.5)
wdw.until(EC.element_to_be_clickable((By.XPATH, processo_xpath)))
driver.find_element(By.XPATH, processo_xpath).click()

for i in range(1,10):
    resultados = []
    # Percorrer os elementos dentro do card
    for tabela in range(1, 5):
        xpath_elemento = f"//*[@id='collapse-{i}']/div/div[{tabela}]"
        try:
            wdw.until(EC.element_to_be_clickable((By.XPATH, xpath_elemento)))
            texto = driver.find_element(By.XPATH, xpath_elemento).text
            
            # Modificar o seletor XPath para obter o link específico dentro de cada elemento
            link_elemento = driver.find_element(By.XPATH, f"{xpath_elemento} //*[@class='arquivo-processo-seletivo']//a")
            link = link_elemento.get_attribute("href")
            
            # Adicionar os resultados à lista
            resultados.append((texto, link))
            
        except:
            break
  
    sleep(1)
    # Criar uma lista de strings com os elementos separados
    elementos_separados = []
    for tupla in resultados:
        for elemento in tupla:
            elementos_separados.append(elemento)

    # Criar o layout para o pop-up
    layout = [[sg.Text(text, enable_events=True, key=f"-LINK-{i}")] for i, text in enumerate(elementos_separados)]

    # Criar a janela de pop-up
    janela_popup = sg.Window("Resultados", layout, keep_on_top=True)

    try:
        while True:
            evento, valores = janela_popup.read()
            if evento == sg.WINDOW_CLOSED:
                break
            elif evento.startswith('-LINK-'):
                link_numero = int(evento.split('-')[2])
                link = elementos_separados[link_numero]
                webbrowser.open(link)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



    # Fechar a janela de pop-up
    janela_popup.close()




    