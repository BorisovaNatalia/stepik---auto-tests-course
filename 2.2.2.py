from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x =  browser.find_element_by_id("input_value").text

    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_id("robotCheckbox").click()

    rb = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()