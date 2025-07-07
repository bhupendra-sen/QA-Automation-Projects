# prctice form of demoqa site using expected condition
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
driver = webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
wait =WebDriverWait(driver,10)
first_name =wait.until(EC.presence_of_element_located((By.ID ,"firstName")))
first_name.send_keys("bhupendra")
last_name =wait.until(EC.presence_of_element_located((By.ID,"lastName")))
last_name.send_keys("sen")
email =wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
email.send_keys("test@gmail.com")
gender = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Male']")))
driver.execute_script("arguments[0].click();", gender)
number = wait.until(presence_of_element_located((By.ID,"userNumber")))
number.send_keys("9815685325")
dob = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
dob.click()
month_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
Select(month_dropdown).select_by_visible_text("August")
year_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
Select(year_dropdown).select_by_visible_text("1999")
day = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='28' and not(contains(@class, 'outside-month'))]")
day.click()

# subjectinput
subject_input = wait.until(EC.presence_of_element_located((By.ID, "subjectsInput")))
subject_input.send_keys("c")
computer= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Computer Science']")))
driver.execute_script("arguments[0].click();", computer)
hobby = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Music']")))
driver.execute_script("arguments[0].click();", hobby)
# upload picture
file_path = os.path.abspath("C:\\Users\\user\\Pictures\\Screenshots\\Screenshot 2024-08-21 142216.png")
picture_upload = wait.until(EC.presence_of_element_located((By.ID, "uploadPicture")))
picture_upload.send_keys(file_path)
address = wait.until(EC.presence_of_element_located((By.ID, "currentAddress")))
address.send_keys("ktm")

# state by text method
state = wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='text'])[7]")))
state.send_keys("N")
op = wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='NCR']")))
driver.execute_script("arguments[0].click();",op)

# # city by text method
city = wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='text'])[8]")))
city.send_keys("D")
opp =  wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='Delhi']")))
driver.execute_script("arguments[0].click();",opp)


submit = wait.until(EC.element_to_be_clickable((By.ID,"submit")))
submit.click()

