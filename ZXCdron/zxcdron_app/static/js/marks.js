ymaps.ready(init);
        var myMap;

        function init() {

            myMap = new ymaps.Map("map", {
                center: [51.672, 39.1843], // Координаты центра карты
                zoom: 13 // Маштаб карты
            });

            myMap.controls.add(
                new ymaps.control.ZoomControl()  // Добавление элемента управления картой
            );

            myPlacemark = new ymaps.Placemark([51.673,39.298], { // Координаты метки объекта
                balloonContent: "<div class='ya_map'>Пункт №1</div>" // Подсказка метки
            }, {
                preset: "twirl#redDotIcon" // Тип метки
            });

            myPlacemark2 = new ymaps.Placemark([51.675,39.1845], { // Координаты метки объекта
                balloonContent: "<div class='ya_map'>Пункт №2</div>" // Подсказка метки
            }, {
                preset: "twirl#redDotIcon" // Тип метки
            });

            myMap.geoObjects.add(myPlacemark); // Добавление метки
            myMap.geoObjects.add(myPlacemark2); // Добавление метки
            myPlacemark.balloon.open(); // Открытие подсказки метки
            myPlacemark2.balloon.open(); // Открытие подсказки метки

        };