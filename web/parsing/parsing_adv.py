import json
import re
import requests
import zipfile
import os
import io

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
zip_filename = "photos.zip"

photo_links = []
print("Type in to indexes of photos (in range 0 to", len(photo_links_or), ") keep in mind that the last index is not included")
a = int(input())
b = int(input()) #not included
for i in range(a, b):
    photo_links.append(photo_links_or[i])

print("photo_links: ", photo_links)
count = 0

# Создаём или открываем ZIP-архив для записи
with zipfile.ZipFile(zip_filename, "w") as zip_file:
    for i, url in enumerate(photo_links):
        try:
            # Загружаем изображение
            response = requests.get(url)
            response.raise_for_status()  # Проверяем успешность запроса

            # Определяем имя файла для архива
            file_name = f"photo_{i+1}.jpg"

            # Записываем изображение в архив в бинарном режиме
            with zip_file.open(file_name, 'w') as image_file:
                image_file.write(response.content)

            print(f"Сохранено: {file_name}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при скачивании {url}: {e}")
#        count += 1
#        print(count, "out of", count_all)
#        if count >= 10:
#            break

print(f"✅ Все фото сохранены в {zip_filename}")

#save_folder = "downloaded_photos"
#count = 0
#for i, url in enumerate(photo_links):
#    try:
#        response = requests.get(url)
#        response.raise_for_status()  # Проверяем успешность запроса

#        content_type = response.headers['Content-Type']
#        if 'image' not in content_type:
#            print(f"Ошибка: {url} не является изображением (тип: {content_type})")
#            continue
#        file_name = f"photo_{i+1}.jpg"
#        file_path = os.path.join(save_folder, file_name)
#        with open(file_path, 'wb') as f:
#            f.write(response.content)

#        print(f"Сохранено: {file_name}")
#    except requests.exceptions.RequestException as e:
#        print(f"Ошибка при скачивании {url}: {e}")
#    count += 1
#    print(count, "out of", count_all)
#    if count >= 10:
#        break

#print(f"✅ Все фото сохранены в папку '{save_folder}'")

f.close()