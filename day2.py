import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver =webdriver.Firefox()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

Full_Name = driver.find_element(By.XPATH,"//input[@id='userName']")
Full_Name.send_keys("bhupendra")
time.sleep(3)

Email_Address =driver.find_element(By.XPATH,"//input[@class='mr-sm-2 form-control']")
Email_Address.send_keys("bhupendrasen@gmail.com")

Current_Address = driver.find_element(By.XPATH,"//textarea[@placeholder='Current Address']")
Current_Address.send_keys("ktm")

Permanent_Address = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea")
Permanent_Address.send_keys("ktm")
time.sleep(2)
Submit = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
Submit.click()
time.sleep(3)
