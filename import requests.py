import requests

def get_weather(city, date):
    api_key = '7626f36de2be21979ff53e160ae5b792'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&dt={date}&appid={api_key}&lang=uk'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature_kelvin = data['main']['temp']
        temperature_celsius = int(temperature_kelvin - 273.15)  # Конвертація з Кельвіна в градуси Цельсія (як ціле число)
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f'Погода у місті {city} на дату {date}:')
        print(f'Температура: {temperature_celsius}°C')
        print(f'Вологість: {humidity}%')
        print(f'Опис: {description}')
    else:
        print('Не вдалося отримати погоду.')

# Запитуємо користувача про місце та дату
city = input('Введіть назву міста: ')
date = input('Введіть дату у форматі день.місяць.рік: ')

get_weather(city, date)
