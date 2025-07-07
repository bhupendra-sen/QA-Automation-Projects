# window switching practice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
Wait=WebDriverWait(driver,10)

CurrentWindow=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Open Window']")))
driver.execute_script("arguments[0].click()",CurrentWindow)
time.sleep(4)

# selenium control goes to next windows
driver.switch_to.window(driver.window_handles[1])

# now activity done in new wondow
blog =Wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Blog']")))
driver.execute_script("arguments[0].click()",blog)
time.sleep(4)

 # selenium control goes  back to previous window
driver.switch_to.window(driver.window_handles[0])



