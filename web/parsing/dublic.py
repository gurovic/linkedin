import shutil
import os
def sv(ind):
    fl_name = "photos" + str(ind) + ".zip"
    # Исходный файл (укажи полный путь)
    source_path = "/Users/sueistratova/PycharmProjects/linkedin/web/parsing/" + fl_name
    # Определяем папку "Загрузки"
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Новый путь для дубликата в "Загрузках"
    destination_path = os.path.join(downloads_folder, fl_name)

    # Копируем файл
    shutil.copy(source_path, destination_path)

    print(f"✅ Дубликат создан в {destination_path}")

for i in range(50, 100):
    sv(i)