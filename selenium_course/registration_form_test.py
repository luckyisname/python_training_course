from selenium import webdriver
import time

TARGET_PAGE = 'http://suninjuly.github.io/registration2.html'

browser = webdriver.Chrome()
browser.get(TARGET_PAGE)

browser.find_element_by_css_selector('.first[required]').send_keys('George')
browser.find_element_by_css_selector('.second[required]').send_keys('Miller')
browser.find_element_by_css_selector('.third[required]').send_keys('filthyfrank@mail.com')

browser.find_element_by_css_selector('button.btn').click()
time.sleep(1)

welcome_text = browser.find_element_by_tag_name("h1").text

assert 'Поздравляем! Вы успешно зарегистировались!' == welcome_text
