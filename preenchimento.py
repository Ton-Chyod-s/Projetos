from selenium.webdriver import Chrome, Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

options = Options()
options.add_argument('-headless')
driver = Firefox(executable_path=GeckoDriverManager().install(),options=options)