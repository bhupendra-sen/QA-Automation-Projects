# pratice from demoqa/select menu
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
driver = webdriver.Firefox()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
wait= WebDriverWait(driver,10)
print(" SELECT VALUE ")
select_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='withOptGroup']//div[text()='Select Option']")))
select_value.click()
time.sleep(1)
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Group 1, option 2']")))
option.click()
time.sleep(1)
selected2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='withOptGroup']//div[contains(@class, 'singleValue')]")))
option2= selected2.text
print("Selected:", option2)
assert option2 == "Group 1, option 2", " Select Value mismatch"
print(" Select Value Assertion Passed")

