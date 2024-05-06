import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_get_address_by_cep_correios():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    time.sleep(1)

    campo_endereco = navegador.find_element(By.NAME, "endereco")
    cep = "02323000"
    campo_endereco.send_keys(cep)
    campo_endereco.submit()
    time.sleep(1)

    botao_enviar = navegador.find_element(By.XPATH, "//button[text()='Buscar']")
    botao_enviar.click()

    table = navegador.find_element(By.ID, "resultado-DNEC")
    time.sleep(1)

    endereco = table.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
    bairro = table.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
    cidade = table.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text
    
    time.sleep(1)
    navegador.execute_script(f"alert('CEP: {cep} | Logradouro : {endereco} | Bairro: {bairro} | Cidade: {cidade}')")
    time.sleep(4)
    alert = navegador.switch_to.alert
    alert.accept()

    navegador.close()
    navegador.quit()
