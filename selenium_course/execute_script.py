from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
x_elem = browser.find_element_by_id("input_value")
x = x_elem.text
y = calc(int(x))
click1 = browser.find_element_by_id("answer")
click1.send_keys(y)
browser.execute_script('return arguments[0].scrollIntoView(center);')
opt1 = browser.find_element_by_id("robotCheckbox").click()
opt2 = browser.find_element_by_id("robotsRule").click()
btn1 = browser.find_element_by_css_selector("button.btn").click()