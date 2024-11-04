from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



try: 
    # 1. Открыть страницу https://suninjuly.github.io/selects1.html
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    selector_value1 = '#num1'
    selector_value2 = '#num2'
    selector_button = ".btn-default"


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1") # ищем элемент с текстом "Python"

    # 2. Считать значение для переменных num1 & num2.
    num1_element = browser.find_element(By.CSS_SELECTOR, selector_value1)
    num1 = int(num1_element.text)
    num2_element = browser.find_element(By.CSS_SELECTOR, selector_value2)
    num2 = int(num2_element.text)
    # 3. Посчитать num1 + num2.
    y = num1 + num2
    # 4. Ввести ответ в текстовое поле.
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y)) 

    # 7.Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, selector_button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
