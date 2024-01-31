from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Github\python-whatsapp-messages\whatsapp-web\data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

phone_number = "+918299231516"
message = "hello"

# URL encoding the message
message = urllib.parse.quote(message)

# Modifying the URL to include the phone number and the message
whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"

# Opening the modified URL
driver.get(whatsapp_url)

# Waiting for the page to load
time.sleep(20)

# Waiting for the send button to be clickable
wait = WebDriverWait(driver, 60)
send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))

# Clicking the send button
send_button.click()

# Simulating the ENTER key press
driver.find_element(By.XPATH, "//div[@contenteditable='true']").send_keys(Keys.ENTER)