# practice from training rcvacademy site
from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://training.rcvacademy.com/test-automation-practice-page")
driver.maximize_window()
wait= WebDriverWait(driver,10)

# checkbox
check_box= driver.find_element(By.XPATH,"//label[text()='Cypress']")
check_box.click()

# radio button
radio=driver.find_element(By.XPATH,"//label[text()='Python']")
radio.click()

# normal dropdown
normal_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,"//select[@class='form-control zen-custom-elm']")))
select = Select(normal_dropdown)
select.select_by_visible_text("Software Testing Mentor")
time.sleep(2)

# simple alert
simple_alert= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@type='button'])[1]")))
simple_alert.click()
time.sleep(2)
simple_alert=driver.switch_to.alert
simple_alert.accept()

# prompt alert
prompt_alert= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@type='button'])[2]")))
prompt_alert.click()
time.sleep(2)
prompt_alert=driver.switch_to.alert
prompt_alert.send_keys("hello")
prompt_alert.accept()

# confirmation alert
confirmation_alert= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@type='button'])[3]")))
confirmation_alert.click()
time.sleep(2)
confirmation_alert=driver.switch_to.alert
confirmation_alert.accept()

new_window = wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[text()='CLICK ME'])[1]")))
new_window.click()

click_rvcacademy = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Click to visit RCV Academy!']")))
click_rvcacademy.click()

# Mouse hover
links = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Our Links']")))
actions = ActionChains(driver)
actions.move_to_element(links).perform()

# select item
select_item = wait.until(EC.presence_of_element_located((By.XPATH,"//li[text()='Item 4']")))
select_item.click()

# drag and drop
actions = ActionChains(driver)
dragme = driver.find_element(By.ID,"draggable")
drophere = driver.find_element(By.ID,"droppable")
actions.drag_and_drop(dragme,drophere).perform()

# tooltip part
age = wait.until(EC.presence_of_element_located((By.ID, "age")))
age.send_keys("25")

# slider exmaple
slider_handle = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='slider']//span | //div[@id='slider']//a")))
driver.execute_script("arguments[0].scrollIntoView(true);", slider_handle)
time.sleep(1)
actions = ActionChains(driver)
actions.click_and_hold(slider_handle).move_by_offset(40, 0).release().perform()
time.sleep(2)

# iframe
iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='RCV Academy eLearning Portal']")))
driver.switch_to.frame(iframe)
all_courses = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "All Courses")))
all_courses.click()
support = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "SUPPORT")))
support.click()
time.sleep(2)




















