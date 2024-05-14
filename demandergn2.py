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

driver.implicitly_wait(7)
# Trouver & Cliquer sur tab de bord
a_element = driver.find_element(By.XPATH, "//a[@href='/']")
a_element.click()

# Trouver & Cliquer sur mes lodins
lodin_element = driver.find_element(By.XPATH, "//a[@href='/transfers']")
lodin_element.click()
#Demande de l'argant
demande_argant = driver.find_element(By.CSS_SELECTOR, ".border-top-right > p").click()

#le montant de recevoir
montant_element =driver.find_element(By.CLASS_NAME,"empty")
montant_element.click()
montant_element.send_keys("200")

#enter le motif
motif_element = driver.find_element(By.ID, "motive")
motif_element.click()
motif_element.send_keys("test")
sleep(2)

#clic sur le button continue
continue_butt = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()
sleep(2)
#le choix du compte pour le recevoir de l'argent
slec_banque = driver.find_element(By.CSS_SELECTOR, ".transfers-bank:nth-child(2) p:nth-child(2)").click()
sleep(2)
#clic sur le buttin continue
continue_element = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()
sleep(2)
#clic sur le buttin continue pour la validation de detail de viremnt
continue_button = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()
sleep(2)
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
sleep(2)
#confirmation du code
confirmer_button = driver.find_element(By.CSS_SELECTOR, ".transfers-body-buttons-main").click()
sleep(2)
# Attendre un certain temps (2 secondes)
sleep(2)

#click sur le lien pour selectionner banque
link_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div/main/div/div[2]/div/div[3]/div[3]/a")
link_element.click()
sleep(2)

#selec bank
div_elem = driver.find_element(By.XPATH,"//*[@id=':r0:']")
div_elem.click()
div_elem.send_keys("cic")
p_element = driver.find_element(By.XPATH, "//p[contains(text(), 'CIC') and not(contains(text(), 'CIC PROD'))]").click()




#clic sur se connecter
connecter_button=driver.find_element(By.CSS_SELECTOR, ".ei_btn_label")
connecter_button.click()
sleep(1)

#confirmation de la demande
button_confirmer = driver.find_element(By.CSS_SELECTOR, "#R5\\3Alabelsubmit > .ei_btn_label")
button_confirmer.click()

sleep(3)