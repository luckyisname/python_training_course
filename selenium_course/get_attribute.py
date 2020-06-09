from selenium import webdriver
from selenium.webdriver.common.keys import Keys
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
assert "Robot" in browser.title

option1 = browser.find_element_by_css_selector("#robotCheckbox").click()
option2 = browser.find_element_by_css_selector("#robotsRule").click()

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_elm = browser.find_element_by_css_selector("#treasure")
x = x_elm.get_attribute("valuex")
y = calc(x)
input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)
btn1 = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/button[1]").click()







