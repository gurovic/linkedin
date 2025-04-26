import shutil
import os

# Исходный файл (укажи полный путь)
source_path = "/Users/sueistratova/PycharmProjects/linkedin/web/parsing/photos.zip"

# Определяем папку "Загрузки"
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Новый путь для дубликата в "Загрузках"
destination_path = os.path.join(downloads_folder, "photos.zip")

# Копируем файл
shutil.copy(source_path, destination_path)

print(f"✅ Дубликат создан в {destination_path}")