from flight_search import FlightSearch
from data_manager import DataManager
from user_data import UserData

data_manager = DataManager()
flight_search = FlightSearch(data_manager.iata)
flight_search.response_requests()
data_manager.save_data(flight_search.result_price)
user_data = UserData()
user_data.new_user_input()
user_data.add_new_user()
