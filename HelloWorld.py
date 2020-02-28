import time
import platform
from selenium import webdriver
from helpers import webHelper

# Use platform.system() to check platform string for conditionals below
# print(platform.system())

driver = None

# Check Chrome version to download appropriate binaries
# Add binaries to directory (drivers) and specify executable path in Chrome()
if platform.system() == "Windows":
    driver = webdriver.Chrome(executable_path='drivers/chromedriver_win32/chromedriver.exe')  # optional argument, if not specified will search path.
elif platform.system() == 'Linux':
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
elif platform.system() == 'Darwin':
    driver = webdriver.Chrome(executable_path='drivers/chromedriver')
else:
    driver = webdriver.Chrome()

# driver = None
address = 'www.towson.edu'
url = 'https://' + address
if driver:
    try:
        driver.get(url)

        ## Sample test
        # time.sleep(5)  # let the user actually see something!
        # search_box = driver.find_element_by_name('q')
        # search_box.send_keys('chromedriver')
        # search_box.submit()
        # time.sleep(5) # let the user actually see something!

        ## Save source
        # html = driver.page_source
        # print(webHelper.save_source(address, html))

        ## Get Element fonts
        # webHelper.get_element_fonts(driver, "*")

        ## Get Element inner html
        webHelper.get_inner_html(driver)
    finally:
        driver.quit()
