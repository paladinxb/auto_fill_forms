from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Настройка драйвера
driver = webdriver.Chrome()  # Убедись, что у тебя установлен ChromeDriver

# Открываем страницу с формой
driver.get("https://forms.mkrf.ru/e/2579/xTPLeBU7/?ap_orgcode=222088")

# Ждем загрузки страницы
time.sleep(3)

start_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Начать')]"))
)
start_button.click()

# Находим выпадающий список и кликаем по нему
dropdown = driver.find_element(By.CLASS_NAME, "survey-select-widget__selected-items")
dropdown.click()

# Ждем появления вариантов выбора
time.sleep(1)  # Можно заменить на WebDriverWait

# Выбираем нужный вариант (например, "Москва")
option = driver.find_element(By.XPATH, "//div[contains(text(), 'Хабаровский край')]")
option.click()

# Находим элемент <label>, содержащий текст "Библиотека"
label = driver.find_element(By.XPATH, "//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Библиотека')]/..")

label.click()


gender_options = ["Мужской", "Женский"]
selected_gender = random.choice(gender_options)
label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), '{selected_gender}')]/..")
label.click()

age_options = ["Младше 18 лет", "18-24 года", "55-64 года", "65 лет и старше"]
selected_age = random.choice(age_options)
label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Младше 18 лет')]/..")
label.click()

label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Полностью удовлетворен')]/..")
label.click()

next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Далее')]"))
)
next_button.click()
'''
input_element = driver.find_element(By.ID, "question_1561_value_1567")
input_element.click()
'''

input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1567')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1568')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1569')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1570')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1571')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1572')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1573')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1561_value_1574')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Далее')]"))
)
next_button.click()


input_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'question_1576_value_1582')]"))
)
if len(input_elements) >= 2:
    pre_last_element = input_elements[4]
    pre_last_element.click()


next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Далее')]"))
)
next_button.click()


label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Часто, чаще одного раза в месяц')]/..")
label.click()


# Находим элемент <label>, содержащий текст "Библиотека"
label = driver.find_element(By.XPATH, "//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Ничего не хотел(а) бы изменить')]/..")
label.click()


next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Далее')]"))
)
next_button.click()


label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Основное общее (8–9 классов)')]/..")
label.click()

label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Студенты, учащиеся')]/..")
label.click()


label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'Живу достаточно обеспеченно (есть денежные накопления и возможность покупать практически все необходимое для жизни)')]/..")
label.click()


label = driver.find_element(By.XPATH, f"//label[contains(@class, 'question-list__item')]//span[contains(text(), 'С рождения')]/..")
label.click()


end_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Завершить')]"))
)
end_button.click()


time.sleep(20)
driver.quit()