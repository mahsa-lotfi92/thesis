# encoding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from selenium import webdriver


browser = None
browser = webdriver.Chrome()

def fill_form():
    file = open('tests.txt')
    for line in file.readlines():
        values = line.split()
        browser.find_element_by_name(values[0]).send_keys(values[1])
    # submit
    browser.find_element_by_class_name('submit').click()


def run():
    """
    Opens vaam site, fill out the form. Returns all Tehran available banks.
    """
    global browser
    # browser = webdriver.Firefox()
    try:
        browser.get("http://localhost:8000")
        browser.implicitly_wait(5)  # seconds
        fill_form()
        print(browser.find_element_by_tag_name('body').text)
        return 11
    finally:
        browser.close()


if __name__ == '__main__':
    run()
