# pratical from demoqa.com [dropable part]
from selenium import webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core.driver import Driver
from webdriver_manager.drivers.ie import IEDriver

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://demoqa.com")
elements = driver.find_element(By.XPATH,"//div[@class='avatar mx-auto white']")
driver.execute_script("arguments[0].click()",elements)
interactions = driver.find_element(By.XPATH,"(//div[@class='header-text'])[5]")
driver.execute_script("arguments[0].click()",interactions)
dropable  = driver.find_element(By.XPATH,"//span[text()='Droppable']")
driver.execute_script("arguments[0].click()",dropable)
dragme = driver.find_element(By.ID,"draggable")
drophere = driver.find_element(By.ID,"droppable")
actions.drag_and_drop(dragme,drophere).perform()
accept = driver.find_element(By.XPATH,"//a[@class='nav-item nav-link']")
accept.click()

source  = driver.find_element(By.ID,"acceptable")
target = driver.find_element(By.XPATH,"//div[@id='acceptDropContainer']//div[@id='droppable']")
actions.drag_and_drop(source,target).perform()
notaccept = driver.find_element(By.ID,"notAcceptable")
targett = driver.find_element(By.XPATH,"//div[@id='acceptDropContainer']//div[@id='droppable']")
actions.drag_and_drop(notaccept,targett).perform()

prevent = driver.find_element(By.XPATH,"//a[@class='nav-item nav-link'][2]")
prevent.click()
draggme = driver.find_element(By.ID,"dragBox")
targettt = driver.find_element(By.ID,"notGreedyDropBox")
actions.drag_and_drop(draggme,targettt).perform()

draggme = driver.find_element(By.ID,"dragBox")
targetttt = driver.find_element(By.ID,"notGreedyInnerDropBox")
actions.drag_and_drop(draggme,targetttt).perform()


# draggme = driver.find_element(By.ID,"dragBox")
# targettttt = driver.find_element(By.ID,"greedyDropBox")
# actions.drag_and_drop(draggme,targettttt).perform()
#
# # draggme = driver.find_element(By.ID,"dragBox")
# draggme = driver.find_element(By.ID,"dragBox")
# # driver.execute_script("arguments[0].scrollIntoView(false);", draggme)
# targetttttt = driver.find_element(By.ID,"greedyDropBoxInner")
# actions.drag_and_drop(draggme,targetttttt).perform()

revert = driver.find_element(By.XPATH,"//a[@class='nav-item nav-link'][3]")
revert.click()
willrevert = driver.find_element(By.ID,"revertable")
go = driver.find_element(By.XPATH,"//div[@id='revertableDropContainer']//div[@id='droppable']")
actions.drag_and_drop(willrevert,go).perform()

notrevert = driver.find_element(By.ID,"notRevertable")
goo = driver.find_element(By.XPATH,"//div[@id='revertableDropContainer']//div[@id='droppable']")
actions.drag_and_drop(notrevert,goo).perform()












