from datetime import datetime, timedelta
my_date_today = datetime.now()

def display_current_datetime():
    date = my_date_today
    current_date = date.strftime("%Y-%M-%d %H:%M:%S")
    return current_date
display_current_datetime()

def calculate_future_date():
    my_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days = my_days)
    print(f"{my_days} days to current date is {future_date.strftime("%Y - %m - %d")}")
    #return future_date.strftime("%Y - %m - %d")
    return future_date
calculate_future_date()

   
        
           




    
















from datetime import datetime
my_date_today = datetime.now()
print(my_date_today)