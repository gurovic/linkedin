// Инициализация карты и установка начальных координат и уровня приближения
var mymap = L.map('mapid').setView([51.505, -0.09], 3);  // Координаты [Широта, Долгота]

// Добавление базового слоя карты OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

// Создание группы для кластеризации маркеров
var markers = L.markerClusterGroup();

// Функция для получения координат по названию университета через Nominatim API
async function getCoordinates(university) {
        const response = await fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(university)}&format=json&limit=1`);
        const data = await response.json();
        if (data.length > 0) {
            return {
                lat: data[0].lat,
                lon: data[0].lon
            };
        } else {
            return null;  // Если координаты не найдены
        }
}

// Функция для получения данных выпускников из JSON файла
async function loadAlumniData() {
        try {
            const response = await fetch('alumni.json');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const alumni = await response.json();

            for (let person of alumni) {
                const coordinates = {
                    lat: person.lat,
                    lon: person.lon
                };

                if (coordinates) {
                    const marker = L.marker([coordinates.lat, coordinates.lon])
                        .bindPopup(`
                            <b>${person.name} ${person.surname}</b><br>
                            University: ${person.univ}<br>
                            Middle Name: ${person.surname || 'N/A'}
                        `);
                    markers.addLayer(marker);
                }
            }

            mymap.addLayer(markers);
        } catch (error) {
            console.error('Ошибка при загрузке данных:', error);
            alert('Произошла ошибка при загрузке данных выпускников');
        }
}

// Загрузка данных и отображение на карте
loadAlumniData();