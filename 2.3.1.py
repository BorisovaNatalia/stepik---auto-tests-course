from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    j_button = browser.find_element_by_tag_name("button")
    j_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x =  int(browser.find_element_by_id("input_value").text)


    browser.find_element_by_id("answer").send_keys(calc(x))
    #browser.find_element_by_id("robotCheckbox").click()
    #browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("[type='submit']").click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()