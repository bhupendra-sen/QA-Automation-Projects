from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

driver = webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
actions.send_keys("bhupendra")
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys("sen")
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys("bhupendrasen10@gmail.com").send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.SPACE).send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys("9815685325").send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.TAB+Keys.ARROW_RIGHT+Keys.ENTER).perform()
sub = driver.find_element(By.XPATH,"//div[@id='subjectsContainer']")
sub.click()
sub_input = driver.find_element(By.XPATH,"//div[@id='subjectsContainer']")
actions.click(sub_input).send_keys("c").perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.SPACE).send_keys(Keys.TAB+Keys.TAB).perform()
driver.execute_script("document.getElementById('uploadPicture').click();")
upload_input = driver.find_element(By.ID, "uploadPicture")
upload_input.send_keys("C:\\Users\\user\\Pictures\\Screenshots\\Screenshot 2024-08-21 142216.png")

time.sleep(1)
actions.send_keys(Keys.TAB).perform()
add = driver.find_element(By.ID,"currentAddress")
add.send_keys("Ktm")

actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.ARROW_DOWN+Keys.ENTER).perform()
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.ARROW_DOWN+Keys.ENTER).perform()
actions.send_keys(Keys.ENTER).perform()






