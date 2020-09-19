from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    n1 = int(browser.find_element_by_id("num1").text)
    n2 = int(browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(n1 + n2))

    browser.find_element_by_css_selector("[type='submit']").click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()