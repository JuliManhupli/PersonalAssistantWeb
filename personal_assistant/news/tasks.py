from datetime import datetime, timedelta
import json

import requests
from bs4 import BeautifulSoup


def get_weather_data(city, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,apparent_temperature,cloudcover,precipitation_probability",
        "forecast_days": 3
    }
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        hourly = data.get("hourly", {})
        times = hourly.get("time", [])
        temperature_2m = hourly.get("temperature_2m", [])
        apparent_temperatures = hourly.get("apparent_temperature", [])

        days_data = [{"temperature": [], "apparent_temperature": []} for _ in range(3)]
        today = datetime.today()

        for i in range(len(times)):
            time = datetime.strptime(times[i], "%Y-%m-%dT%H:%M")
            day_index = (time.date() - today.date()).days
            if 0 <= day_index < 3:
                days_data[day_index]["temperature"].append(temperature_2m[i])
                days_data[day_index]["apparent_temperature"].append(apparent_temperatures[i])

        weather_data = {
            "city": city,
            "forecast_days": [
                {
                    "date": (today + timedelta(days=i + 1)).strftime("%Y-%m-%d"),
                    "max_temperature": max(day_data["temperature"]),
                    "min_temperature": min(day_data["temperature"])
                }
                for i, day_data in enumerate(days_data)
            ]
        }

        # Convert the dictionary to JSON
        json_data = json.dumps(weather_data, indent=2)
        return json_data
    else:
        print(f"Error fetching weather for {city.name}")


def scraping_ukraine(limit=10):
    result = []

    response = requests.get("https://www.unian.ua/society")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('div[class=list-thumbs__item]')
        count = 0

        for item in content:

            if count >= limit:
                break
            news_data = {}

            title_element = item.find('a', class_='list-thumbs__title')
            if title_element:
                news_data['title'] = title_element.text.strip()

            link_element = item.find('a', class_='list-thumbs__image')
            if link_element:
                news_data['link'] = link_element['href']

                img_element = link_element.find('img')

                if img_element:
                    news_data['image'] = img_element['data-src']

            time_element = item.find('div', class_='list-thumbs__time')
            if time_element:
                news_data['time'] = time_element.text.strip()

            if news_data:
                result.append(news_data)

            count += 1

    return result[:limit]


def scraping_finance(limit=10):
    result = []

    response = requests.get("https://minfin.com.ua/ua/news/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('li[class=item]')

        count = 0

        for item in content:
            if count >= limit:
                break

            news_data = {}

            title_element = item.find('a')
            if title_element:
                news_data['title'] = title_element.text.strip()

            link_element = item.find('a')
            if link_element:
                news_data['link'] = link_element['href']

            time_element = item.find('span', class_='data')
            if time_element:
                datetime_str = time_element['content']
                datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                formatted_time = datetime_object.strftime('%H:%M, %d.%m.%Y')

                news_data['time'] = formatted_time

            if news_data:
                result.append(news_data)

            count += 1

    return result[:limit]


def scraping_sport(limit=10):
    result = []

    response = requests.get("https://sport.unian.ua/othersports")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('div[class=list-thumbs__item]')
        count = 0

        for item in content:

            if count >= limit:
                break
            news_data = {}

            title_element = item.find('a', class_='list-thumbs__title')
            if title_element:
                news_data['title'] = title_element.text.strip()

            link_element = item.find('a', class_='list-thumbs__image')
            if link_element:
                news_data['link'] = link_element['href']

                img_element = link_element.find('img')

                if img_element:
                    news_data['image'] = img_element['data-src']

            time_element = item.find('div', class_='list-thumbs__time')
            if time_element:
                news_data['time'] = time_element.text.strip()

            if news_data:
                result.append(news_data)

            count += 1

    return result[:limit]

def scraping_culture(limit=10):
    result = []

    response = requests.get("https://www.radiosvoboda.org/z/635")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('li.fui-grid__inner')
        print(content)

        count = 0

        for item in content:
            if count >= limit:
                break

            news_data = {}

            # Extracting title
            title_element = item.find('h4', class_='media-block__title')
            if title_element:
                news_data['title'] = title_element.text.strip()

            # Extracting link
            link_element = item.find('a', class_='img-wrap')
            if link_element:
                news_data['link'] = "https://www.radiosvoboda.org/" + link_element['href']

            time_element = item.find('span', class_='date')
            if time_element:
                news_data['time'] = time_element.text.strip()

            if news_data:
                result.append(news_data)

            count += 1

    return result[:limit]
