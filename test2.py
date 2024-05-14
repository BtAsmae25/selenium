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
sleep(1)


# Sélection du chemin d'accès par défaut
path_element = driver.find_element(By.CSS_SELECTOR, "path[d='M5 30v-2.792h30V30Zm0-8.625v-2.75h30v2.75Zm0-8.583V10h30v2.792Z']")
path_element.click()

#Ajout de la banque
'''
# Clic sur l'élément "Mes Soldes"
div_element = driver.find_element(By.XPATH, "//div[text()='Mes Soldes']")
div_element.click()
# Sélection de l'option de la banque "BANQUE POSTALE"
div_element = driver.find_element(By.CSS_SELECTOR, "div.account-select-header")
div_element.click()

# Clic sur l'image représentant "BANQUE POSTALE"

image_element = driver.find_element(By.XPATH, "//img[@alt='BANQUE POSTALE']")
image_element.click()
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
'''

#virement
driver.implicitly_wait(7)
# Trouver & Cliquer sur tab de bord
a_element = driver.find_element(By.XPATH, "//a[@href='/']")
a_element.click()


# Trouver & Cliquer sur mes lodins
lodin_element = driver.find_element(By.XPATH, "//a[@href='/transfers']")
lodin_element.click()

'''
# Trouver & Cliquer sur l'élément "ajouter le montant"
input_element = driver.find_element(By.ID, "amount")
input_element.click()

# Entrer la valeur "200" dans l'élément <input>
input_element.send_keys("200")

# Trouver & Cliquer l'élément "motif"
input_element = driver.find_element(By.ID, "motive")
input_element.click()
# Entrer la valeur "test" dans l'élément
input_element.send_keys("test")

# Trouver & Cliquer sur le bouton continue
button_element = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
button_element.click()

# Trouver &  sélectionner un compte bancaire
selec_element = driver.find_element(By.CLASS_NAME, "transfers-bank-check")
selec_element.click()

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

# Trouver & Cliquer sur le button continue
continue_button = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
continue_button.click()

#valider virement
valide_button = driver.find_element(By.CLASS_NAME, "transfers-body-buttons-main")
valide_button.click()

#entrer code Lodin E-Secure
child1_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .segmented-input-field")
child1_element.click()
child1_element.send_keys('1')

child2_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .segmented-input-field").send_keys("1")
child3_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .segmented-input-field").send_keys("1")
child4_element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .segmented-input-field").send_keys("1")

#confirmation du code Lodin E-Secure
confirmation_element = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()

#clic sur valider pour valider le virement
valide_element = driver.find_element(By.ID, "valider").click()


#executer le virement
excute_virement =driver.find_element(By.CSS_SELECTOR, "div:nth-child(2)").click()
'''

#Demande de l'argant
demande_argant = driver.find_element(By.CSS_SELECTOR, ".border-top-right > p").click()

#le montant de recevoir
montant_element =driver.find_element(By.CLASS_NAME,"empty")
montant_element.click()
montant_element.send_keys("200")

#enter le motif
motif_element = driver.find_element(By.ID, "motive")
motif_element.click()
motif_element.send_keys("dddd")

#clic sur le buttin continue
continue_butt = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()

#le choix du compte pour le recevoir de l'argent
slec_banque = driver.find_element(By.CSS_SELECTOR, ".transfers-bank:nth-child(2) p:nth-child(2)").click()

#clic sur le buttin continue
continue_element = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()

#clic sur le buttin continue pour la validation de detail de viremnt
continue_button = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()

# enter le code lodin E_secure
child1 = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .segmented-input-field")
child1.click()
child1.send_keys("1")
child2 = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .segmented-input-field")
child2.click()
child2.send_keys("1")
child3 = driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .segmented-input-field")
child3.click()
child3.send_keys("1")
child4 = driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .segmented-input-field")
child4.click()
child4.send_keys("1")

#confirmation du code
confirmer_button = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()


# Attendre un certain temps (44 secondes)
sleep(44)
