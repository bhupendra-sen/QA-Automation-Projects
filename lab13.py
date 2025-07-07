# implement dropdown by using different selenium method
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
wait =WebDriverWait(driver,10)

# select by visible text
country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "country")))
select = Select(country_dropdown)
select.select_by_visible_text("Australia")
time.sleep(2)

# select by value
select.select_by_value("usa")
time.sleep(2)

# select by index
select.select_by_index(2)
time.sleep(2)

