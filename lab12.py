# alert practice using different types of alert
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
wait =WebDriverWait(driver,10)

# simple alert handling
alert= wait.until(EC.element_to_be_clickable((By.ID,"alertButton")))
alert.click()
time.sleep(2)
alert=driver.switch_to.alert
alert.accept()

# timer
timer_alert= wait.until(EC.element_to_be_clickable((By.ID,"timerAlertButton")))
timer_alert.click()
time.sleep(2)
timer_alert=driver.switch_to.alert
timer_alert.accept()

# confirmation alert
con_alert= wait.until(EC.element_to_be_clickable((By.ID,"confirmButton")))
con_alert.click()
time.sleep(2)
con_alert = driver.switch_to.alert
con_alert.dismiss()

# prompt alert
prompt_alert = wait.until(EC.element_to_be_clickable((By.ID,"promtButton")))
prompt_alert.click()
time.sleep(2)
prompt_alert= driver.switch_to.alert
prompt_alert.send_keys("hello")
prompt_alert.accept()






