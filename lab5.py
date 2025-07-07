from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://demoqa.com")
action = ActionChains(driver)
elements =driver.find_element(By.XPATH,"//div[@class='avatar mx-auto white'] ")
driver.execute_script("arguments[0].click()",elements)
button = driver.find_element(By.XPATH,"//span[contains(@class,'text') and contains(text(),'Buttons')]")
button.click()
doubleclick = driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-primary') and contains(text(),'Double Click Me')])[1]")
action.double_click(elements).perform()

clickme = driver.find_element(By.XPATH,"(//button[contains(@class,'btn btn-primary') and contains(text(),'Click Me')])[3]")

clickme.click()










