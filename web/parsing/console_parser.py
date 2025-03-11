import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Настройка Selenium
options = Options()
options.headless = True  # Запуск без интерфейса браузера
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Базовый URL страницы
base_url = "https://letovo.ru/o-shkole/galereya"

# Список ID галерей
id_list = [376]

for gal_id in id_list:
    url = f"{base_url}/{gal_id}"
    retries = 3  # Количество попыток при ошибке

    for attempt in range(retries):
        driver.get(url)
        try:
            # Ожидание загрузки элементов
            gallery = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "v-slide-group__content"))
            )
            images = gallery.find_elements(By.TAG_NAME, "img")

            # Список ссылок на изображения
            image_urls = []
            for img in images:
                src = img.get_attribute("src")
                if src and (".jpg" in src or ".png" in src):  # Фильтруем только картинки
                    image_urls.append(src)

            # Выводим найденные ссылки на изображения
            print(f"Галерея {gal_id}:")
            for img_url in image_urls:
                print(img_url)
            break  # Если успешно, выходим из цикла
        except Exception as e:
            print(f"Ошибка при обработке галереи {gal_id} (попытка {attempt + 1}): {e}")
            time.sleep(random.uniform(3, 6))  # Случайная задержка перед новой попыткой
    else:
        print(f"Не удалось загрузить галерею {gal_id} после {retries} попыток.")

# Завершаем работу драйвера
driver.quit()