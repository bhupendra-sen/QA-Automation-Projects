import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 10)
firstName = driver.find_element(By.ID,"firstName")
driver.execute_script("arguments[0].scrollIntoView(true)", firstName)
firstName.send_keys("Aayush")

lastName = driver.find_element(By.ID,"lastName")
driver.execute_script("arguments[0].scrollIntoView(true)", lastName)
lastName.send_keys("Niraula")

email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
driver.execute_script("arguments[0].scrollIntoView(true)", email)
email.send_keys("aayushniraulaherodon@gmail.com")

gender = driver.find_element(By.XPATH,"//label[@for='gender-radio-1']")
driver.execute_script("arguments[0].scrollIntoView(true)", gender)
gender.click()

mobileNumber = driver.find_element(By.ID,"userNumber")
driver.execute_script("arguments[0].scrollIntoView(true)", mobileNumber)
mobileNumber.send_keys("9852012345")

#selecting the date
inputDate = wait.until(EC.element_to_be_clickable(
    (By.ID,"dateOfBirthInput")))
driver.execute_script("arguments[0].scrollIntoView(true)", inputDate)
inputDate.click()

#selecting the month
month = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//select[@class = 'react-datepicker__month-select']")))
Select(month).select_by_visible_text("January") #month object

#selecting the year
year = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "select.react-datepicker__year-select")))
year.click()
Select(year).select_by_visible_text("2002")


#selecting the day
day = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='7' and not(contains(@class, 'outside-month'))]")))
day.click()

# #Handling Subjects
# subjects = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//div[@id = 'subjectsContainer]")))
# driver.execute_script("arguments[0].scrollIntoView(true);",subjects)
# subjects.send_keys("Math")
# selectedOption = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option') and contains(text(), 'Maths')]")))
# selectedOption.click()

#upload files

uploadFiles = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
driver.execute_script("arguments[0].scrollIntoView(true)", uploadFiles)
uploadFiles.send_keys("C:\\Users\\aayus\\OneDrive\\Desktop\\IDcardDesign")


hobbies = driver.find_element(By.XPATH,"//label[@for='hobbies-checkbox-1']")
driver.execute_script("arguments[0].scrollIntoView(true)", hobbies)
hobbies.click()

currentAddress = driver.find_element(By.ID,"currentAddress")
driver.execute_script("arguments[0].scrollIntoView(true)", currentAddress)
currentAddress.send_keys("Kathmandu, Nepal")

# Step 1: Click the dropdown
selectDropDown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@id = 'state']")))
driver.execute_script("arguments[0].scrollIntoView(true)", selectDropDown)
selectDropDown.click()


# Step 2: Select "Rajasthan" option
optionSelected = wait.until(EC.element_to_be_clickable(
     (By.XPATH, "//div[text() = 'Uttar Pradesh']")))
optionSelected.click()

time.sleep(2)
submitButton = driver.find_element(By.XPATH, "//button[text() = 'Submit']")
driver.execute_script("arguments[0].scrollIntoView(true)", submitButton)
submitButton.submit()

time.sleep(2)
