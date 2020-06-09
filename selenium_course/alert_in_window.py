from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_css_selector("button.btn.btn-primary")
option1.click()
alert = browser.switch_to.alert
alert.accept()
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_css_selector("input#answer.form-control")
input1.send_keys(y)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()