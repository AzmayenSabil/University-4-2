from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://qa-practice.netlify.app/checkboxes")


# Clicking a checkbox
checkbox1 = driver.find_element(By.ID, "checkbox1")
checkbox1.click()

time.sleep(2)

checkbox2 = driver.find_element(By.ID, "checkbox2")
checkbox2.click()

# Verifying if the checkboxes are clicked
checkbox1_checked = checkbox1.is_selected()
checkbox2_checked = checkbox2.is_selected()

time.sleep(2)


# Assertion for the first checkbox
assert checkbox1_checked, "Checkbox 1 is not clicked"
print("Test Passed: Checkbox 1 is clicked")

# Assertion for the second checkbox
assert checkbox2_checked, "Checkbox 2 is not clicked"
print("Test Passed: Checkbox 2 is clicked")

# Close the browser
driver.quit()
