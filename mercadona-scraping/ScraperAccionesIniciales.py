from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def ScrapingInicio(driver):
    # Se aceptan las cookies
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'button.ui-button ui-button--small ui-button--primary ui-button--positive'.replace(' ', '.'))))\
        .click()

    # Se introduce el código postal a 46001
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'input.ym-hide-content')))\
        .send_keys("46001")

    # Se acepta ventana de código postal
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'button.button-primary button-big'.replace(' ', '.'))))\
        .click()