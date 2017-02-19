# encoding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.support.select import Select


browser = None


def fill_form():
    browser.find_element_by_id('ctl00_ContentPlaceHolder1_tbIDNo').send_keys('0030000009')
    browser.find_element_by_id('ctl00_ContentPlaceHolder1_tbBRNo').send_keys('0000000001')
    browser.find_element_by_id('ctl00_ContentPlaceHolder1_tbBrYear').send_keys('1234')
    Select(browser.find_element_by_id('ctl00_ContentPlaceHolder1_ddlBrDay')).select_by_index(2)
    Select(browser.find_element_by_id('ctl00_ContentPlaceHolder1_ddlBrMonth')).select_by_index(1)
    browser.find_element_by_id('ctl00_ContentPlaceHolder1_chkBoxAlert').click()

    # submit
    browser.find_element_by_id('ctl00_ContentPlaceHolder1_btnContinue0').click()


def get_tehran_options():
    """
    :return: List of name of available banks
    """
    CITY_LABEL = 'تهران'
    # CITY_LABEL = 'قزوين'
    NOT_FOUND_MESSAGE = 'هيچ موردي يافت نشد'
    Select(browser.find_element_by_id('ctl00_ContentPlaceHolder1_ddlState')).select_by_visible_text(CITY_LABEL)
    items = browser.find_element_by_id('ctl00_ContentPlaceHolder1_BulletedList1').find_elements_by_tag_name('li')
    return [x.text for x in items if x.text.strip() != NOT_FOUND_MESSAGE]


def get_available_banks():
    """
    Opens vaam site, fill out the form. Returns all Tehran available banks.
    """
    global browser
    # browser = webdriver.Firefox()
    browser = webdriver.PhantomJS()
    try:
        browser.get("http://ve.cbi.ir/TasReq.aspx")
        browser.implicitly_wait(5)  # seconds
        fill_form()
        banks = get_tehran_options()
        print(banks)
        return banks
    finally:
        browser.close()


if __name__ == '__main__':
    get_available_banks()
