# keyword action pratical
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
name= driver.find_element(By.ID,"firstName")
actions.click(name).send_keys("bhupendra"+Keys.ENTER).perform()

lastname= driver.find_element(By.ID,"lastName")
actions.click(lastname).send_keys("sen"+Keys.ENTER).perform()

email= driver.find_element(By.ID,"userEmail")
actions.click(email).send_keys("bhupendrasen10@gmail.com"+Keys.ENTER).perform()
Gender = driver.find_element(By.XPATH,"//label[@class='custom-control-label']")
actions.click(Gender).perform()
Mobile_number = driver.find_element(By.ID,"userNumber")
actions.click(Mobile_number).send_keys("9815685326"+Keys.ENTER).perform()
# dob_input = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
# actions.click(dob_input).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).send_keys("28 August 1999"+Keys.ENTER).perform()
# time.sleep(1)

subject_input = driver.find_element(By.ID, "subjectsInput")
actions.click(subject_input).send_keys("c").key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
time.sleep(1)
hobbies= driver.find_element(By.XPATH,"//label[@class='custom-control-label']")
actions.click(hobbies).perform()



























