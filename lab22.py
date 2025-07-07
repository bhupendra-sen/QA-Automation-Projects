# demoqa site date picker practice

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/")
wait=WebDriverWait(driver,10)

widgets = wait.until(EC.presence_of_element_located((By.XPATH,"//h5[text()='Widgets']")))
driver.execute_script("arguments[0].click();", widgets)

date_picker=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Date Picker']")))
driver.execute_script("arguments[0].click();", date_picker)

dob = wait.until(EC.element_to_be_clickable((By.ID, "datePickerMonthYearInput")))
dob.click()

month_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
Select(month_dropdown).select_by_visible_text("August")

year_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
Select(year_dropdown).select_by_visible_text("1999")

day = driver.find_element(By.XPATH, "//div[@aria-label='Choose Saturday, August 28th, 1999']")
day.click()
time.sleep(3)

# date and time
date_time= wait.until(EC.presence_of_element_located((By.ID,"dateAndTimePickerInput")))
driver.execute_script("arguments[0].click()",date_time)
time.sleep(2)
date= wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Choose Saturday, August 28th, 1999']")))
driver.execute_script("arguments[0].click()", date)

select_time= wait.until(EC.presence_of_element_located((By.XPATH,"//li[text()='00:30']")))
driver.execute_script("arguments[0].click()", select_time)
