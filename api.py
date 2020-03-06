import zerorpc

import os
import time
import platform
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


class webHelper(object):

    def __init__(self):
        # Use platform.system() to check platform string for conditionals below
        # print(platform.system())

        self.driver = None

        # Check Chrome version to download appropriate binaries
        # Add binaries to directory (drivers) and specify executable path in Chrome()
        if platform.system() == "Windows":
            self.driver = webdriver.Chrome(
                executable_path='drivers/chromedriver_win32/chromedriver.exe')  # optional argument, if not specified will search path.
        elif platform.system() == 'Linux':
            self.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        elif platform.system() == 'Darwin':
            self.driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        else:
           self.driver = webdriver.Chrome()

        self.driver.get("https://www.towson.edu")

        time.sleep(5)
        self.driver.quit()

    ## Sample test
    # time.sleep(5)  # let the user actually see something!
    # search_box = driver.find_element_by_name('q')
    # search_box.send_keys('chromedriver')
    # search_box.submit()
    # time.sleep(5) # let the user actually see something!

    def save_source(self, address, source):
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
    def get_element_fonts(self, selector):
        elements = self.driver.find_elements_by_css_selector(selector)
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



    def get_inner_html(self):  # incomplete
        elements = self.driver.find_elements_by_css_selector("*")
        text = ""
        for i, e in enumerate(elements):
            try:
                if e.value_of_css_property('display') != "none":
                    inner = self.driver.execute_script("return arguments[0].textContent", e)
                    text = text + " " + inner
            except StaleElementReferenceException as e:
                print(e)
        print(text)



    def get_element_colors(self):
        elements = self.driver.find_elements_by_css_selector("*")
        colors = []
        for i, e in enumerate(elements):
            try:
                if e.value_of_css_property('display') != "none":
                    inner = self.driver.execute_script("return arguments[0].textContent", e)
                    text = text + " " + inner
            except StaleElementReferenceException as e:
                print(e)
        print(colors)


def parse_port():
    return "4242"


def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(webHelper())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()


if __name__ == '__main__':

    main()
