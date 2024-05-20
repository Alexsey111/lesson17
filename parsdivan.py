import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://www.divan.ru/barnaul/category/svet'

driver.get(url)

time.sleep(10)

svets = driver.find_elements(By.CLASS_NAME, '_Ud0k')

parsed_data = []

for svet in svets:
    try:
        # Получаем название светильника
        title = svet.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        # Получаем цену светильника
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        # Получаем ссылку на светильник
        link = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'стоимость', 'ссылка на изделие'])
    writer.writerows(parsed_data)

