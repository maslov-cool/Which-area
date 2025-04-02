import sys
import requests


# поиск долготы + широты
geocode = ' '.join(sys.argv[1:])
server_address = 'http://geocode-maps.yandex.ru/1.x/'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'

# Выполняем запрос
response = requests.get(server_address, params={'apikey': api_key, 'geocode': geocode, 'format': 'json'})

if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    print(toponym['metaDataProperty']['GeocoderMetaData']['Address']['Components'][4]['name'])
else:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")

