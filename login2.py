from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest
from time import sleep

@allure.severity(allure.severity_level.NORMAL)
class TestLodin:

    @allure.severity(allure.severity_level.MINOR)
    def test_navigateur(self):
        # Spécifier le chemin d'accès au pilote Chrome téléchargé
        chrome_driver_path = "C:\\Users\\ASMAE BOUAZZATI\\Downloads\\chromedriver-win64\\chromedriver.exe"

        # Creer une instance du service Chrome
        service = Service(chrome_driver_path)
        # Creer une instance du pilote Chrome en utilisant le service
        driver = webdriver.Chrome(service=service)

        # Charger une page web
        driver.get("https://app.lodinpay.com/")
        # Allure
        status = driver.find_element(By.CLASS_NAME, 'margin-r-xs').is_displayed()
        if status:
            assert True
        else:
            assert False

        driver.close()

@allure.severity(allure.severity_level.NORMAL)
def test_list():
    pytest.skip('Skipping test')


@allure.severity(allure.severity_level.CRITICAL)
def test_login():
    chrome_driver_path = "C:\\Users\\ASMAE BOUAZZATI\\Downloads\\chromedriver-win64\\chromedriver.exe"
    # Creer une instance du service Chrome
    service = Service(chrome_driver_path)
    # Creer une instance du pilote Chrome en utilisant le service
    driver = webdriver.Chrome(service=service)

    # Charger une page web
    driver.get("https://app.lodinpay.com/")

    # Redimensionner la fenêtre du navigateur
    adressemail_input = driver.set_window_size(758, 824)

    # Recherche et saisie de l'adresse e-mail dans le champ "contact"
    adressemail_input = driver.find_element(By.ID, "contact")
    adressemail_input.click()
    adressemail_input.send_keys('pafojo6316@gosarlar.com')

    # Recherche et clic sur le bouton "Continuer"
    button = driver.find_element(By.CSS_SELECTOR, ".button-main")
    button.click()
    sleep(1)

    # Saisie du mot de pass à six chiffres
    for _ in range(6):
        button = driver.find_element(By.XPATH, "//button[contains(text(), '1')]")
        button.click()

    # Clic sur le bouton "Continuer" après avoir saisi le code de vérification
    cnx_button = driver.find_element(By.CSS_SELECTOR, ".button-main")
    cnx_button.click()

    # Vérification du titre de la page
    act_title = driver.title

    if act_title == "Lodin":
        driver.close()
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(),name="testLoginScreen",attachment_type=AttachmentType.PNG)
        driver.close()
        assert False

    sleep(66)
