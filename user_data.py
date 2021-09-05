import pandas as pd
# import xlsxwriter

USER_DATA = pd.read_excel('Flight_Deals.xlsx', sheet_name='Users')
FLIGHT_DATA = pd.read_excel('Flight_Deals.xlsx', sheet_name='Flight')
print(USER_DATA)

first_name = USER_DATA['First Name'].tolist()
last_name = USER_DATA['Last Name'].tolist()
email = USER_DATA['Email'].tolist()

data = {
    'First Name': first_name,
    'Last Name': last_name,
    'Email': email,
}


class UserData:
    def new_user_input(self):
        print("Welcome to flight club! \n We find the best flight deals and email you.")
        new_first_name = input("What is your first name?: ")
        new_last_name = input("What is your last name?: ")
        self.email_input = input("What is your email?: ")
        new_email = self.email_input
        # email.append(self.email_input)
        self.confirm_email = input("Please, confirm your email: ")
        self.new_row = {'First Name': new_first_name, 'Last Name': new_last_name, 'Email': new_email}

    def add_new_user(self):
        if self.email_input == self.confirm_email:
            print("Success! Your email has been added! Check your email.")
            user_data = pd.DataFrame(data)
            user_data = user_data.append(self.new_row, ignore_index=True)
            sheets = {'Flight': FLIGHT_DATA, 'Users': user_data}
            writer = pd.ExcelWriter('Flight_Deals.xlsx', engine='xlsxwriter')
            for sheet_name in sheets.keys():
                sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
            # user_data.to_excel(writer)
            writer.save()
        else:
            print('Wrong email')
