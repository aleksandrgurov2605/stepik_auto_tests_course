from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    # 1. Открыть страницу https://suninjuly.github.io/math.html.
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    selector_value = '#treasure'
    selector_answer = '#answer'
    selector_checkbox = '#robotCheckbox'
    selector_radio = "[value='robots']"
    selector_button = ".btn-default"

    # 2. Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = int(x_element.get_attribute("valuex"))
    # 3. Посчитать математическую функцию от x (код для этого приведён ниже).
    y = calc(x)
    # 4. Ввести ответ в текстовое поле.
    input_answer = browser.find_element(By.CSS_SELECTOR, selector_answer)
    input_answer.send_keys(y)
    # 5. Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.CSS_SELECTOR, selector_checkbox)
    checkbox.click()
    # 6. Выбрать radiobutton "Robots rule!".
    radio = browser.find_element(By.CSS_SELECTOR, selector_radio)
    radio.click()
    # 7.Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, selector_button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
