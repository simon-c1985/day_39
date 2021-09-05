import math
import pandas as pd
pd.options.mode.chained_assignment = None
SHEET_DATA = pd.read_excel('Flight_Deals.xlsx', index_col=0, sheet_name='Flight')
USER_DATA = pd.read_excel('Flight_Deals.xlsx', sheet_name='Users')


class DataManager:
    def __init__(self):
        self.list_iata_codes = SHEET_DATA
        self.iata = SHEET_DATA['IATA Code'].tolist()
        print(self.iata)

    def save_data(self, new_price):
        for index in range(0, len(self.list_iata_codes['Lowest Price'])):
            try:
                if self.list_iata_codes['Lowest Price'][index] > new_price[index] \
                        or math.isnan(self.list_iata_codes['Lowest Price'][index])\
                        or self.list_iata_codes['Lowest Price'][index] == 0:
                    self.list_iata_codes['Lowest Price'][index] = new_price[index]
            except TypeError:
                self.list_iata_codes['Lowest Price'][index] = 0
        data_to_write = pd.DataFrame(self.list_iata_codes)
        sheets = {'Flight': data_to_write, 'Users': USER_DATA}
        writer = pd.ExcelWriter('Flight_Deals.xlsx')
        for sheet_name in sheets.keys():
            sheets[sheet_name].to_excel(writer, sheet_name=sheet_name)
        # data_to_write.to_excel(writer, sheet_name='Flight')
        writer.save()
