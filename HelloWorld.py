import time
from helpers import webHelper

driver = webHelper.initiate_driver()
# driver = None
address ='www.towson.edu'
url = 'https://' + address
if driver:
    try:
        driver.get(url)
        time.sleep(10)

        ## Save source
        # html = driver.page_source
        # print(webHelper.save_source(address, html))

        ## check Element fonts
        # webHelper.get_element_fonts(driver, "*")

        ## check Element inner html (incomplete)
        # webHelper.get_inner_html(driver)

        ## Check consistent use of color
        # webHelper.get_element_colors(driver)

    finally:
        driver.quit()
