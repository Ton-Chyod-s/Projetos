from selenium.webdriver import Chrome, Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

url = "https://fapec.org/processo-seletivo/"
xpath = '//*[@id="PSS_RPA"]/h5/button'


options = Options()
#options.add_argument('-headless')
driver = Firefox(executable_path=GeckoDriverManager().install(),options=options)
#entrando no site
driver.get(url)
wdw = WebDriverWait(driver, 60)

#procurar processo seletivo
wdw.until(element_to_be_clickable(('xpath', xpath)))
processo_seletivo = driver.find_element(By.XPATH,xpath).text

if 'Processo Seletivo Simplificado 031/2023' in processo_seletivo:
    print('deu certo')
else:
    print('nem deu certo')