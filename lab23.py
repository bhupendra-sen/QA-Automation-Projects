# automation practice on omayo.blogspot.com sie

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
actions=ActionChains(driver)
wait=WebDriverWait(driver,10)

# search= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='ENqPLc'")))
# search.click()
# search.send_keys("hello")

page_one=wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Page One']")))
page_one.click()

# order list
order_list= driver.find_element(By.ID,"HTML25")
num =order_list.find_elements(By.TAG_NAME,"li")
for number in num:
    print(number.text)

# unorder list
unod= driver.find_element(By.ID,"HTML26")
num=unod.find_elements(By.TAG_NAME,"li")
for number in num:
    print(number.text)

 # text area field
text_area= wait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='ta1']")))
text_area.click()
text_area.send_keys("hello world")

# multi selection box
multi_select= Select(wait.until(EC.presence_of_element_located((By.ID,"multiselect1"))))
multi_select.select_by_value("volvox")
multi_select.select_by_visible_text("Hyundai")

# older newslaterm
old_newspaper=Select(wait.until(EC.presence_of_element_located((By.ID,"drop1"))))
old_newspaper.select_by_visible_text("doc 2")

# window switching
NewWindow=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='SeleniumTutorial']")))
driver.execute_script("arguments[0].click()",NewWindow)
time.sleep(4)
driver.switch_to.window(driver.window_handles[1])
time.sleep(4)
driver.switch_to.window(driver.window_handles[0])

# button with same attribute value
submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
driver.execute_script("arguments[0].scrollIntoView(true)", submit)
submit.click()
login= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Login']")))
driver.execute_script("arguments[0].scrollIntoView(true)",login)
login.click()
register = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
driver.execute_script("arguments[0].scrollIntoView(true)", register)
register.click()

# check this
check_this =wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Check this']")))
check_this.click()
time.sleep(11)
my_option= wait.until(EC.element_to_be_clickable((By.ID,"dte")))
my_option.click()

clickBtn = wait.until(EC.element_to_be_clickable((By.ID, "alert2")))
driver.execute_script("arguments[0].scrollIntoView(true)", clickBtn)
clickBtn.click()
alert = driver.switch_to.alert
alert.accept()

# open popup window
pop_window = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Open a popup window']")))
driver.execute_script("arguments[0].scrollIntoView(true)", pop_window)
driver.switch_to.window(driver.window_handles[0])

# upload file
file_upload = wait.until(EC.element_to_be_clickable((By.ID, "uploadfile")))
driver.execute_script("arguments[0].scrollIntoView(true)", file_upload)
file_upload.send_keys("D:\\PycharmProjects\\pythonProject1\\email_validation_demo.csv")

# timer button
timerBtn = wait.until(EC.element_to_be_clickable((By.ID, "timerButton")))
driver.execute_script("arguments[0].click()", timerBtn)

# double click
double_click = driver.find_element(By.XPATH, "//button[text()=' Double click Here   ']")
driver.execute_script("arguments[0].scrollIntoView(true)", double_click)
actions.double_click(double_click).perform()
driver.switch_to.alert.accept()
# header text
head= driver.find_element(By.XPATH,"//h2[@class='date-header']")
print(head.text)

# text field two
text_area= wait.until(EC.presence_of_element_located((By.XPATH,"(//textarea[@rows='10'])[2]")))
text_area.click()
text_area.send_keys("hello world again")

# html form
username= wait.until(EC.presence_of_element_located((By.XPATH,"//(//input[@type='text'])[1]']")))
username.send_keys("bhupendra")
password= wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='password'])[1]")))
password.send_keys("Admin@123")
login=wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='button']")))
login.click()

# iframe 1
iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='iframe1']")))
driver.switch_to.frame(iframe)
link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='What is Selenium']")))
link.click()

 # back from iframe before switching to another iframe
driver.switch_to.default_content()

iframe2 = wait.until(EC.presence_of_element_located((By.ID, "iframe2")))
driver.switch_to.frame(iframe2)
selenium_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='What is Selenium']")))
selenium_link.click()
driver.switch_to.default_content()

# simple login page
username= wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='text'])[2]")))
username.send_keys("bhupendra")
password= wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='password'])[2]")))
password.send_keys("Admin@123")
login=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='button']")))
login.click()
cancel=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='reset']")))
cancel.click()

# text print()
print_text=driver.find_element(By.XPATH,"//p[@title='Free Selenium tutorials']")
print(print_text.text)

# search
search_text=wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@title='search'])[1]")))
search_text.click()
search_text.send_keys("Selenium")
search_button=wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@title='search'])[2]")))
search_button.click()

#radio button
RadioButton=wait.until(EC.element_to_be_clickable((By.ID,"radio1")))
driver.execute_script("arguments[0].click()",RadioButton)

#AlertDemo
AlertDemo=wait.until(EC.element_to_be_clickable((By.ID,"alert1")))
driver.execute_script("arguments[0].click()",AlertDemo)

AlertDemo=driver.switch_to.alert
time.sleep(1)
AlertDemo.accept()

#Prompt alert
Prompt_alert=wait.until(EC.element_to_be_clickable((By.ID,"prompt")))
driver.execute_script("arguments[0].click()",Prompt_alert)

prompt_alert=driver.switch_to.alert
prompt_alert.send_keys("hello")
time.sleep(1)
prompt_alert.accept()

# confirmation alert
con_alert= wait.until(EC.element_to_be_clickable((By.ID,"confirm")))
con_alert.click()
time.sleep(2)
con_alert = driver.switch_to.alert
con_alert.dismiss()

# locate using name attritude
name=wait.until(EC.presence_of_element_located((By.NAME,"textboxn")))
name.send_keys("hey")

# locate using class attritude
name=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"classone")))
name.send_keys("hello")

# car select
car_select = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Car']")))
driver.execute_script("arguments[0].click();", car_select)

# # select multiple option
select_multiple= wait.until((EC.presence_of_element_located(By.ID,"HTML33")))
driver.execute_script("arguments[0].click()",select_multiple)
book =select_multiple.find_element(By.XPATH,"//input[@value='Bag']")
book.click()
# laptop =wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Laptop']")))
#

