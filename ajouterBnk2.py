from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Spécifier le chemin d'accès au pilote Chrome téléchargé
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
sleep(1)

# Sélection du chemin d'accès par défaut
path_element = driver.find_element(By.CSS_SELECTOR, "path[d='M5 30v-2.792h30V30Zm0-8.625v-2.75h30v2.75Zm0-8.583V10h30v2.792Z']")
path_element.click()
#Ajout de la banque


# Clic sur l'élément "Mes Soldes"
div_element = driver.find_element(By.XPATH, "//div[text()='Mes Soldes']").click()
div_element

# Sélection de l'option de la banque "BANQUE POSTALE"
divv_element = driver.find_element(By.CSS_SELECTOR, "div.account-select-header")
divv_element.click()


# Clic sur l'image représentant "BANQUE POSTALE"
image_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='BANQUE POSTALE']"))
)
ActionChains(driver).move_to_element(image_element).click().perform()

# Clic sur le bouton "Continuer"
button_element = driver.find_element(By.CSS_SELECTOR, "button.account-button-main")
button_element.click()

# Trouver & Clic sur le bouton "Confirmer"
confirmer_button = driver.find_element(By.XPATH, "//div/button[text()='Confirmer']")
confirmer_button.click()

# Attendre implicitement jusqu'à ce que l'élément "Valider" soit disponible
driver.implicitly_wait(7)

# Clic sur le bouton "Valider"
button_valider = driver.find_element(By.ID, "valider")
button_valider.click()


#supprimer la banque
div1 =driver.find_element(By.CSS_SELECTOR, ".balance-stepper-item:nth-child(1) svg")
div1.click()
supp_bank = driver.find_element(By.CSS_SELECTOR, ".balance-stepper-item-header-settings-item:nth-child(2)")
supp_bank.click()
div2 = driver.find_element(By.CSS_SELECTOR, ".balance-stepper-item-header-settings-toggle > svg")
div2.click()

supp_bank2 = driver.find_element(By.CSS_SELECTOR, ".balance-stepper-item-header-settings-toggle > svg")


supp_bank3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".balance-stepper-item-header-settings-item:nth-child(2)"))
)
ActionChains(driver).move_to_element(supp_bank3).click().perform()
sleep(7)