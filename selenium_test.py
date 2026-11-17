from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome
options = Options()
options.add_argument("--start-maximized")

# Open Chrome automatically
driver = webdriver.Chrome(options=options)

# Open our sample website
import os

file_path = os.path.abspath("sample.html")
driver.get("file:///" + file_path.replace("\\", "/"))

print("Chrome opened successfully!")
print(driver.title)

input("Press Enter to close the browser...")

driver.quit()