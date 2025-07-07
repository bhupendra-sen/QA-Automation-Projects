
# demoqa site pracice form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
Name = driver.find_element(By.ID,"firstName")
Name.send_keys("bhupendra ")
Email_Address = driver.find_element(By.ID,"userEmail")
Email_Address.send_keys("bhupendrasen@gamail.com")
Gender = driver.find_element(By.XPATH,"//label[@class='custom-control-label']")
Gender.click()
Mobile_number = driver.find_element(By.ID,"userNumber")
Mobile_number.send_keys("9815655323")
# selecting date
dateofbirth = driver.find_element(By.ID,"dateOfBirthInput")
dateofbirth.click()
# selectmonth
month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
Select(month_dropdown).select_by_visible_text("August")
year_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
Select(year_dropdown).select_by_visible_text("1999")
day = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='28' and not(contains(@class, 'outside-month'))]")
day.click()
subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("c")
computer_science_option =driver.find_element(By.XPATH,"//div[text()='Computer Science']")
driver.execute_script("arguments[0].click();", computer_science_option)
hobbies= driver.find_element(By.XPATH,"//label[@class='custom-control-label']")
hobbies.click()

file_path = os.path.abspath("C:\\Users\\user\\Pictures\\Screenshots\\Screenshot 2024-08-21 142216.png")

picture_upload = driver.find_element(By.ID, "uploadPicture")
picture_upload.send_keys(file_path)

currentaddres = driver.find_element(By.ID,"currentAddress")
currentaddres.send_keys("ktm")

state_dropdown = driver.find_element(By.ID, "state")
driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
state_dropdown.click()
time.sleep(1)
ncr_option = driver.find_element(By.ID, "react-select-3-option-0")
ncr_option.click()

city_dropdown = driver.find_element(By.ID, "city")
driver.execute_script("arguments[0].scrollIntoView(true);", city_dropdown)
city_dropdown.click()
time.sleep(1)
delhi_option = driver.find_element(By.ID, "react-select-4-option-0")
delhi_option.click()
submit =driver.find_element(By.ID,"submit")
submit.click()








