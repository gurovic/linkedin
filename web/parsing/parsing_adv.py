import json
import re
import requests
import zipfile
import os
import io

def load_ph(a, b, ind):
    global photo_links_or
    zip_filename = "photos" + str(ind) + ".zip"
    photo_links = []
    print(ind, a, b)
    for i in range(a, b):
        photo_links.append(photo_links_or[i])

    #print("photo_links: ", photo_links)
    count = 0

    # Создаём или открываем ZIP-архив для записи
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        for i, url in enumerate(photo_links):
            try:
                # Загружаем изображение
                response = requests.get(url)
                response.raise_for_status()  # Проверяем успешность запроса

                # Определяем имя файла для архива
                file_name = f"photo_{i + 1}.jpg"

                # Записываем изображение в архив в бинарном режиме
                with zip_file.open(file_name, 'w') as image_file:
                    image_file.write(response.content)

                print(f"Сохранено: {file_name}")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при скачивании {url}: {e}")
    print(f"✅ Все фото сохранены в {zip_filename}")

f = open("photos.json", "r")
photos = json.load(f)

with open("photos.txt", "w", encoding="utf-8") as file:
    file.write(str(photos))
ph = str(photos)

#регулярное выражение для поиска "https:" + до ближайшего '
pattern = r"https:[^']*'"

# Находим все такие подстроки
matches = re.findall(pattern, ph)
matches_1 = []
for i in matches:
    matches_1.append(i[:-1])
#print(matches_1)

photo_links_or = matches_1.copy()
#print(photo_links_or)
for i in range(50, 100):
    load_ph(i * 50, (i + 1)*50 - 1, i)

f.close()