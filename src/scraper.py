from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

def buscar_temperatura_umidade():
    try:
        options = Options()
        options.add_argument('--headless')  # necessário no Codespaces
        driver = webdriver.Firefox(options=options)

        driver.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp")

        temperatura = driver.find_element(By.CLASS_NAME, "temperature").text
        umidade = driver.find_element(By.XPATH, '//li[b[text()="Umidade"]]').text.split(":")[1].strip()

        driver.quit()
        return temperatura, umidade
    except Exception as e:
        print("Erro ao buscar:", e)
        return None, None
