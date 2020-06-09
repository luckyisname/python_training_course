from

link = "http://suninjuly.github.io/math.html?"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_css_selector("label.form-check-label")
option1.click()
option2 = browser.find_element_by_css_selector("input#robotsRule.form-check-input")
option2.click()
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_css_selector("input#answer.form-control")
input1.send_keys(y)
button = browser.find_element_by_css_selector("button.btn")
button.click()