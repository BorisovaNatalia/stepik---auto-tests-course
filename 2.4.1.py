from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button.click()

    x =  int(browser.find_element_by_id("input_value").text)


    browser.find_element_by_id("answer").send_keys(calc(x))
    #browser.f
    # e
    # ййind_element_by_id("robotCheckbox").click()
    #browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("[type='submit']").click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()