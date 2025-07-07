from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://demoqa.com/")
elements =driver.find_element(By.XPATH,"//div[@class='avatar mx-auto white']")
driver.execute_script("arguments[0].click()",elements)
interactions = driver.find_element(By.XPATH,"(//div[@class='header-text'])[5]")
driver.execute_script("arguments[0].click()",interactions)
draggable = driver.find_element(By.XPATH,"//span[text()='Dragabble']")
driver.execute_script("arguments[0].click()",draggable)
dragme = driver.find_element(By.XPATH,"//div[text()='Drag me']")
actions.click_and_hold(dragme).move_by_offset(100,2).release().perform()
Axix = driver.find_element(By.XPATH,"//a[@class='nav-item nav-link']")
Axix.click()
onlyx = driver.find_element(By.XPATH,"//div[text()='Only X']")
actions.click_and_hold(onlyx).move_by_offset(200,2).release().perform()
onlyy = driver.find_element(By.XPATH,"//div[text()='Only Y']")
actions.click_and_hold(onlyy).move_by_offset(200,2).release().perform()
container = driver.find_element(By.XPATH,"//a[@id='draggableExample-tab-containerRestriction']")
driver.execute_script("arguments[0].click()",container)
con1 = driver.find_element(By.XPATH,"//div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']")
actions.click_and_hold(con1).move_by_offset(200,2).release().perform()
con2 = driver.find_element(By.XPATH,"//div[@class='ui-widget-header ui-draggable ui-draggable-handle']")
actions.click_and_hold(con2).move_by_offset(200,2).release().perform()






