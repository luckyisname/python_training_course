from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

import os
file_path = os.path.abspath("C:/Users/lolikkekov/PycharmProjects/untitled/fileupload.txt")

pole1 = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/input[1]").send_keys("Garry")
pole2 = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/input[2]").send_keys("Potter")
pole3 = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/input[3]").send_keys("garrymotherfucker@mail.com")
opt1 = browser.find_element_by_css_selector("input[type=file]").send_keys("file_path")

