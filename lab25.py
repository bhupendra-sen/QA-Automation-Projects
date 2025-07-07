# prctice from abroadsathi.com site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
driver = webdriver.Firefox()
driver.get("https://abroadsathi.com/")
driver.maximize_window()
wait= WebDriverWait(driver,10)

search=wait.until(EC.presence_of_element_located((By.XPATH,"//*[local-name()='svg' and @class='lucide lucide-list-filter pe-4 cursor-pointer']")))
# driver.execute_script("arguments[0].click();", search)
search.click()

country=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='All Countries']")))
country.click()
time.sleep(2)
uk_select=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='United Kingdom']")))
uk_select.click()

degree=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='All Degree']")))
driver.execute_script("arguments[0].click();", degree)
# degree.click()
time.sleep(2)
master_select=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Masters']")))
master_select.click()

cross_button=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='backButton my-auto cursor-pointer mx-2']")))
cross_button.click()
time.sleep(2)

results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'custom-courses-card')]")))
time.sleep(2)
try:
    for result in results:
        print(result.text)
        resultText = result.text.lower()
        assert "united" in resultText, "united is not found"
        assert "master" in resultText, "degree not found"
except AssertionError as ae:
    print(f"Assertion error: {ae}")
except Exception as e:
    print(f"Test failed due to: {e}")
    traceback.print_exc()
finally:
    driver.quit()

