import time
import platform
from selenium import webdriver

# Use platform.system() to check platform string for conditionals below
# print(platform.system())

driver = None

# Check Chrome version to download appropriate binaries
# Add binaries to directory (drivers) and specify executable path in Chrome()
if platform.system() == "Windows":
    driver = webdriver.Chrome(executable_path='drivers/chromedriver_win32/chromedriver.exe')  # optional argument, if not specified will search path.
elif platform.system() == 'Linux':
    driver = webdriver.Chrome(executable_path='drivers/chromedriver_win32/chromedriver.exe')
elif platform.system() == 'Darwin':
    driver = webdriver.Chrome(executable_path='drivers/chromedriver_win32/chromedriver.exe')
else:
    driver = webdriver.Chrome()

if driver:
    try:
        driver.get('http://www.google.com/')
        time.sleep(5) # let the user actually see something!
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('chromedriver')
        search_box.submit()
        time.sleep(5) # let the user actually see something!
    finally:
        driver.quit()
