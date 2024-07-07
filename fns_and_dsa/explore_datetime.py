from datetime import datetime
my_date_today = datetime.now()

def display_current_datetime(current_date = my_date_today):
    print(current_date)
    
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    def calculate_future_date(future_date):
        future_date = current_date + number_of_days.timedelta(days = number_of_days)
        print(future_date)
    calculate_future_date
display_current_datetime(current_date= my_date_today)   




    
















from datetime import datetime
my_date_today = datetime.now()
print(my_date_today)