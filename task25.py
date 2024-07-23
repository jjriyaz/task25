import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# Setup WebDriver path and options
paths = r"C:\Users\DELL\Desktop\New folder\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
# Navigate to the IMDb Advanced Name Search page
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()
# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)

driver.execute_script("window.scrollTo(0, 500)")
expand_all_element = driver.find_element(By.XPATH, '//*[@data-testid="adv-search-expand-all"]')
expand_all_element.click()

name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="test-nametext"]')))
driver.execute_script("arguments[0].click();", name_input)
driver.find_element(By.XPATH,'//input[@name="name-text-input"]').send_keys("kaththi")
credits = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[8]/div[2]/div/div/div/div[1]/input')
driver.execute_script("arguments[0].click();", credits)

# Find the credit input element
credit = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[8]/div[2]/div/div/div/div[1]/input')
gender = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[2]/div/section/button[1]/span')
driver.execute_script("arguments[0].click();", gender)
# Use ActionChains to input text and select the first suggestion
actions = ActionChains(driver)
actions.send_keys_to_element(credit, "indian")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
actions.pause(2)  # Pause briefly to ensure the selection
actions.send_keys(Keys.ENTER)  # Press the Enter key to select
actions.perform()

# Confirmation
print("Search performed successfully.")

# Close the browser
driver.quit()