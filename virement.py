from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

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
sleep(2)
# Sélection du chemin d'accès par défaut
path_element = driver.find_element(By.CSS_SELECTOR, "path[d='M5 30v-2.792h30V30Zm0-8.625v-2.75h30v2.75Zm0-8.583V10h30v2.792Z']")
path_element.click()
sleep(2)


#virement
driver.implicitly_wait(7)
# Trouver & Cliquer sur tab de bord
a_element = driver.find_element(By.XPATH, "//a[@href='/']")
a_element.click()
sleep(2)

# Trouver & Cliquer sur mes lodins
lodin_element = driver.find_element(By.XPATH, "//a[@href='/transfers']")
lodin_element.click()
sleep(2)

# Trouver & Cliquer sur l'élément "ajouter le montant"
input_element = driver.find_element(By.ID, "amount")
input_element.click()
sleep(2)

# Entrer la valeur "200" dans l'élément <input>
input_element.send_keys("200")
sleep(2)

# Trouver & Cliquer l'élément "motif"
input_element = driver.find_element(By.ID, "motive")
input_element.click()
# Entrer la valeur "test" dans l'élément
input_element.send_keys("test")
sleep(2)

# Trouver & Cliquer sur le bouton continue
button_element = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
button_element.click()
sleep(2)

# Trouver &  sélectionner un compte bancaire
selec_element = driver.find_element(By.CLASS_NAME, "transfers-bank-check")
selec_element.click()
sleep(2)

# Trouver & Cliquer surle bouton "Continue"
button_continue = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
button_continue.click()
driver.implicitly_wait(7)

# Trouver & Cliquer sur Choisisser un bénéficiaire
benef_element = driver.find_element(By.XPATH,"/html/body/div/div/div/main/div/div[2]/div/div[2]/div/button[1]/p")
benef_element.click()

# Trouver & Cliquer sur  bénéficiaire
choisir_benef = driver.find_element(By.XPATH, "//p[text()='Allali Ahemad']")
choisir_benef.click()
sleep(2)

# Trouver & Cliquer sur le button continue
continue_button = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
continue_button.click()
sleep(2)

#valider virement
valide_button = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
valide_button.click()
sleep(2)

#entrer code Lodin E-Secure
child1_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .segmented-input-field")
child1_element.click()
child1_element.send_keys('1')
sleep(2)

child2_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .segmented-input-field").send_keys("1")
child3_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .segmented-input-field").send_keys("1")
child4_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .segmented-input-field").send_keys("1")

#confirmation du code Lodin E-Secure
confirmation_element = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()
sleep(2)

#clic sur valider pour valider le virement
valide_element = driver.find_element(By.ID, "valider").click()
sleep(2)


#executer le virement
excute_virement =driver.find_element(By.CSS_SELECTOR, "div:nth-child(2)").click()
sleep(2)