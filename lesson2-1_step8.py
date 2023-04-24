from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    ans_list = ('vasia', 'pupkin', 'pusia@mail.ru')
    for i in range(len(elements)):
        elements[i].send_keys(ans_list[i])

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла 
    #print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

