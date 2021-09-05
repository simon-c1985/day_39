import requests
import datetime as dt


TEQUILA_API_KEY = 'i6klOJFF-DuZ5Ziz2QPik2NP5NUVjt9Z'
FLY_FROM = 'MOW'
FLY_TO = 'KGD'
SEARCHING_DAYS = 2
TODAY = str(dt.datetime.now().strftime('%d/%m/%Y'))
DAY_AFTER_TODAY = str((dt.datetime.now() + dt.timedelta(days=SEARCHING_DAYS)).strftime('%d/%m/%Y'))
NIGHTS_NUMBER = 3
MAX_FLY_DURATION = 10
ADULTS = 2
SELECTED_CABINS = 'M'
SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
TEQUILA_HEADER = {'apikey': TEQUILA_API_KEY}


class FlightSearch:
    def __init__(self, list_iata):
        self.result_price = []
        self.list_iata = list_iata
        self.search_params = {
            'fly_from': FLY_FROM,
            'fly_to': FLY_TO,
            'date_from': TODAY,
            'date_to': DAY_AFTER_TODAY,
            'nights_in_dst_from': NIGHTS_NUMBER,
            'nights_in_dst_to': NIGHTS_NUMBER + 4,
            'max_fly_duration': MAX_FLY_DURATION,
            'adults': ADULTS,
            'selected_cabins': SELECTED_CABINS,
            'curr': 'RUB',
            'flight_type': 'round',
            'adult_hold_bag': '0,0',
            'max_stopovers': 2,
        }

    def response_requests(self):
        for iata in self.list_iata:
            self.search_params['fly_to'] = iata
            self.response = requests.get(url=SEARCH_ENDPOINT, params=self.search_params, headers=TEQUILA_HEADER)
            self.data = self.response.json()['data']
            self.price = [price['price'] for price in self.data]
            self.air_company = [air['airlines'] for air in self.data]
            self.num_available_seats = [seats['availability'] for seats in self.data]
            self.departure_time = [time['local_departure'] for time in self.data]
            self.route = [route['route'] for route in self.data]
            self.print_results()

    def print_results(self):
        # result_price = []
        print(f"Race from {self.search_params['fly_from']} to: {self.search_params['fly_to']}")
        i = 0
        try:
            seats = self.num_available_seats[i]['seats']
            for i in range(0, len(self.data)):
                if self.num_available_seats[i]['seats']:
                    lower_price = self.price[i]
                    break
        except IndexError:
            print('No flights!')
        else:
            for index in range(1, len(self.data)):
                if lower_price > self.price[index] and self.num_available_seats[i]['seats']:
                    lower_price = self.price[index]
                    i = index
            print(f"Option {i + 1}: \n Price: {self.price[i]} \n "
                  f"Number of available seats: {self.num_available_seats[i]['seats']} \n"
                  f"Air company: {self.air_company[i]} \n "
                  f"Departure time: {self.departure_time[i]}")
            if len(self.route[i]) > 1:
                print(f"Number of transfers is: {len(self.route[i])}")
                for city in self.route[i]:
                    print(f"Departure city: {city['cityFrom']}, Arrived city: {city['cityTo']} ")
            else:
                print('Without transfer!')
        try:
            self.result_price.append(lower_price)
        except UnboundLocalError:
            self.result_price.append('')
        print(self.result_price)
