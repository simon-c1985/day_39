from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
flight_search = FlightSearch(data_manager.iata)
flight_search.response_requests()
data_manager.save_data(flight_search.result_price)
# data_manager.save_data(flight_search.response_requests())
