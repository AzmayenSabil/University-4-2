from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://qa-practice.netlify.app/bugs-form.html")

# Typing into a text field using By.ID
text_field = driver.find_element(By.ID, "firstName")
text_field.send_keys("Azmayen")
# Assertion for first name field value
assert text_field.get_attribute("value") == "Azmayen", "First name value assertion failed"
print("First name value assertion passed")

# Typing into a text field using By.ID
text_field = driver.find_element(By.ID, "lastName")
text_field.send_keys("Sabil")
# Assertion for last name field value
assert text_field.get_attribute("value") == "Sabil", "Last name value assertion failed"
print("Last name value assertion passed")

# Typing into a text field using By.ID
text_field = driver.find_element(By.ID, "phone")
text_field.send_keys("01833352501")
# Assertion for phone number field value
assert text_field.get_attribute("value") == "01833352501", "Phone number value assertion failed"
print("Phone number value assertion passed")

# Handling Dropdowns using By.ID
# Selecting an option by visible text
dropdown = Select(driver.find_element(By.ID, "countries_dropdown_menu"))
dropdown.select_by_value("Bangladesh")

# Typing into a text field using By.ID
text_field = driver.find_element(By.ID, "emailAddress")
text_field.send_keys("azmayensabil@gmail.com")
# Assertion for email address field value
assert text_field.get_attribute("value") == "azmayensabil@gmail.com", "Email address value assertion failed"
print("Email address value assertion passed")

# Typing into a text field using By.ID
text_field = driver.find_element(By.ID, "password")
text_field.send_keys("admin123")
# Assertion for password field value
assert text_field.get_attribute("value") == "admin123", "Password value assertion failed"
print("Password value assertion passed")

checkbox2 = driver.find_element(By.ID, "exampleCheck1")
checkbox2.click()
checkbox2_checked = checkbox2.is_selected()
# Assertion for the first checkbox
assert checkbox2_checked, "Checkbox is not clicked"
print("Test Passed: Checkbox is clicked")


# Clicking a button using By.ID
button = driver.find_element(By.ID, "registerBtn")
button.click()

time.sleep(2)

# Locate the element containing the success message
success_message_element = driver.find_element(By.ID, "results-section")

# Extract the text from the element
success_message = success_message_element.text

# Print the success message
print("Registration Successful:", success_message)

# Close the browser
driver.quit()
