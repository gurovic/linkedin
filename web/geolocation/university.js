// Функция для получения координат по названию университета
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

// Получение данных выпускников и отображение на карте
async function loadAlumniData() {
    const alumniResponse = await fetch('/api/alumni/');
    const alumni = await alumniResponse.json();

    for (let person of alumni) {
        const coordinates = await getCoordinates(person.university);
        if (coordinates) {
            // Добавляем маркер на карту
            const marker = L.marker([coordinates.lat, coordinates.lon]).addTo(mymap)
                .bindPopup(`${person.first_name} ${person.last_name}<br>${person.university}`);
            markers.addLayer(marker);  // Добавление маркера в кластерную группу
        }
    }
    mymap.addLayer(markers);  // Добавление группы кластеров на карту
}

console.log(getCoordinates("Brown University"));