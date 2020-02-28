import os
import time
from selenium.common.exceptions import StaleElementReferenceException


def save_source(address, source):
    name = address.replace('.', '-') + '.html'
    path = './data/' + name

    if os.path.exists(path):
        return 'page exists'
    else:
        f = open(path, 'w')
        f.write(source)
        f.close()
        return 'page created'


# Stale Element Exception is raised if wait is not provided
# Need to find a better method than sleep()
def get_element_fonts(driver, selector):
    time.sleep(5)
    elements = driver.find_elements_by_css_selector(selector)
    fonts = []
    for i, e in enumerate(elements):
        try:
            if e.value_of_css_property('display') != "none":
                font_family = map(str.strip, e.value_of_css_property('font-family').split(","))
                fonts.extend(font_family)
        except StaleElementReferenceException as e:
            print(e)
    fonts = list(set(fonts))
    print(fonts)
    print("Number of fonts (including fallbacks): ", len(fonts))


def get_inner_html(driver):
    time.sleep(5)
    elements = driver.find_elements_by_css_selector("*")
    text = ""
    for i, e in enumerate(elements):
        try:
            if e.value_of_css_property('display') != "none":
                inner = driver.execute_script("return arguments[0].textContent", e)
                text = text + " " + inner
        except StaleElementReferenceException as e:
            print(e)
    print(text)

