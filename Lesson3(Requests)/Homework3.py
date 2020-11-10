import requests
import json

def get_iata_code(city):
    resp = requests.get(f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{city}%20в%20Лондон').text
    data = json.loads(resp)
    return data['origin']['iata']

while True:
    try:
        from_city = input('Введите город отправления: ')
        to_city = input('Введите город прибытия: ')
        origin_city = get_iata_code(from_city)
        destination_city = get_iata_code(to_city)
        resp = requests.get(f'http://min-prices.aviasales.ru/calendar_preload?origin={origin_city}&destination={destination_city}').text
        flight_info = json.loads(resp)
        best_price = flight_info['best_prices'][0]["value"]
        depart_date = flight_info["best_prices"][0]["depart_date"]
        return_date = flight_info["best_prices"][0]["return_date"]
        print(f'На рейс {from_city} - {to_city} лучшая цена туда и обратно - {best_price} рублей. Дата отправления: {depart_date}, дата возвращения: {return_date}.')
        break
    except:
        print('Такие города не найдены или напишите их на русском языке')







