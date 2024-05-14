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

# Sélection le chemin d'accès
path_element = driver.find_element(By.CSS_SELECTOR, "path[d='M5 30v-2.792h30V30Zm0-8.625v-2.75h30v2.75Zm0-8.583V10h30v2.792Z']")
path_element.click()

#clic sur Réglages
wait = WebDriverWait(driver, 10)
reglages_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/ul/li[6]/a')))
reglages_button.click()


#clic sur le buttin changer mot de passe
changer_pswrd = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[1]/a').click()

#selection la banque
select_bnk = driver.find_element(By.XPATH, "//p[contains(text(), 'CIC') ]").click()

#clicer sur le button s'authentifier auprès de la banque
sauthentifier_bnk = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/form/button').click()

#clicer sur le button  se connecter

secnct = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ei_btn_label')))
secnct.click()
sleep(2)

#clicer sur le button accepter de donner accès aux comptes de banque à Lodin
accepter_button = driver.find_element(By.XPATH, '//*[@id="I0:btnConfirmSubmission:labelsubmit"]/span[2]').click()
sleep(2)

#clicer sue le button suivant
suvivant_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/a/div').click()

#les etape pour changer le mot de passe
input_ancienPswr = driver.find_element(By.XPATH, '//*[@id="old_password"]')
input_ancienPswr.click()
input_ancienPswr.send_keys('111111')

input_newPswrd = driver.find_element(By.XPATH, '//*[@id="new_password"]')
input_newPswrd.click()
input_newPswrd.send_keys('111111')

input_ConfirmerNewPswrd = driver.find_element(By.XPATH, '//*[@id="confirm_new_password"]')
input_ConfirmerNewPswrd.click()
input_ConfirmerNewPswrd.send_keys('111111')

#clicer sur le button changer le mot de passe
chng_pswrd = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div/form/button').click()
sleep(2)

#clicer sur le button continuer

continuer_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/button')))
continuer_button.click()



sleep(5)