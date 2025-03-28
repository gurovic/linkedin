const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

// Основной URL, откуда начинаем парсить
const baseUrl = 'https://elk.letovo.ru/storage/';

// Функция для получения всех изображений с сайта
async function getImagesFromPage(pageUrl) {
  try {
    const response = await axios.get(pageUrl);
    const $ = cheerio.load(response.data);

    // Массив для хранения ссылок на изображения
    const imageUrls = [];

    // Ищем все теги <img>, у которых есть атрибут 'src', содержащий ссылки на изображения
    $('img').each((index, element) => {
      let imgUrl = $(element).attr('src');

      // Проверяем, что URL изображения соответствует нужному формату
      if (imgUrl && imgUrl.includes('/storage/')) {
        // Преобразуем относительный путь в абсолютный URL
        imgUrl = 'https://elk.letovo.ru' + imgUrl;
        imageUrls.push(imgUrl);
      }
    });

    return imageUrls;
  } catch (error) {
    console.error('Ошибка при получении изображений:', error);
  }
}

// Функция для загрузки изображений
async function downloadImage(url, filePath) {
  try {
    const response = await axios.get(url, { responseType: 'stream' });
    const writer = fs.createWriteStream(filePath);
    response.data.pipe(writer);

    return new Promise((resolve, reject) => {
      writer.on('finish', resolve);
      writer.on('error', reject);
    });
  } catch (error) {
    console.error(`Ошибка при загрузке изображения с URL: ${url}`, error);
  }
}

// Функция для скачивания изображений с собранными URL
async function downloadImages(imageUrls) {
  // Создаем папку для сохранения изображений, если её нет
  const imagesFolder = path.join(__dirname, 'images');
  if (!fs.existsSync(imagesFolder)) {
    fs.mkdirSync(imagesFolder);
  }

  for (let i = 0; i < imageUrls.length; i++) {
    const url = imageUrls[i];
    const fileName = path.basename(url);  // Получаем имя файла из URL
    const filePath = path.join(imagesFolder, fileName);  // Путь для сохранения

    try {
      await downloadImage(url, filePath);
      console.log(`Изображение ${fileName} успешно загружено!`);
    } catch (error) {
      console.error(`Ошибка при загрузке изображения ${fileName}:`, error);
    }
  }
}

// Главная функция для выполнения парсинга
async function main() {
  // Пример страницы, с которой начинаем парсить
  const pageUrl = 'https://elk.letovo.ru/storage/111479/conversions/';  // Замените на нужную страницу

  // Получаем все изображения с этой страницы
  const imageUrls = await getImagesFromPage(pageUrl);
  console.log('Найдено изображений:', imageUrls.length);

  // Загружаем изображения
  await downloadImages(imageUrls);
}

// Запуск парсинга
main();