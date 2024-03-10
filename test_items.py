from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), 'There is no "add to basket" button on the page'
