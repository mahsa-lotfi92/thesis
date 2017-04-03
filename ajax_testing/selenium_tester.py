# encoding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from selenium import webdriver

browser = None
browser = webdriver.Chrome()

def run():
    """
    Opens vaam site, fill out the form. Returns all Tehran available banks.
    """
    global browser
    # browser = webdriver.Firefox()
    try:
        file = open('selenium_tests.txt')
        for line in file.readlines():
            browser.get("http://localhost:8000")
            browser.implicitly_wait(5)  # seconds
            values = line.split()

            browser.find_element_by_name(values[0]).send_keys(values[1])
            browser.find_element_by_class_name('submit').click()
            print(browser.find_element_by_tag_name('body').text == values[2])
            return 11
    finally:
        browser.close()


if __name__ == '__main__':
    run()
