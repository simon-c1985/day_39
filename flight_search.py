import requests
import datetime as dt

TEQUILA_API_KEY = 'i6klOJFF-DuZ5Ziz2QPik2NP5NUVjt9Z'
FLY_FROM = 'LED'
FLY_TO = 'KGD'
SEARCHING_DAYS = 2
TODAY = str(dt.datetime.now().strftime('%d/%m/%Y'))
DAY_AFTER_TODAY = str((dt.datetime.now() + dt.timedelta(days=SEARCHING_DAYS)).strftime('%d/%m/%Y'))
NIGHTS_NUMBER = 3
MAX_FLY_DURATION = 10
ADULTS = 2
SELECTED_CABINS = 'M'
SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'

search_params = {
    'fly_from': FLY_FROM,
    'fly_to': FLY_TO,
    'date_from': TODAY,
    'date_to': DAY_AFTER_TODAY,
    # 'nights_in_dst_from': NIGHTS_NUMBER,
    # 'nights_in_dst_to': NIGHTS_NUMBER + 4,
    'max_fly_duration': MAX_FLY_DURATION,
    'adults': ADULTS,
    'selected_cabins': SELECTED_CABINS,
}

tequila_header = {'apikey': TEQUILA_API_KEY}
response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=tequila_header)
# print(response.json())
for data in response.json()['data']:
    print(data['price'])
    print(data['airlines'])
    print(data['availability'])
    print(data['local_departure'])
    print(len(data['route']))
    if len(data['route']) > 1:
        print(f"Number of transfers is: {len(data['route'])}")
        for city in data['route']:
            print(f"City from: {city['cityFrom']}, City to: {city['cityTo']} ")
    else:
        print('Without transfer!')

class FlightSearch:
    def __init__(self):
        pass