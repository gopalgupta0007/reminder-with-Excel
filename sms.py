# import schedule
# import time
# from tkinter import messagebox

# def job():
#     print("remider")

# # schedule.every(1).seconds.do(job)

# def job_with_argument(name):
#     print(f"I am {name}")
#     messagebox.showwarning("Warning", "Please select an Excel file first.")


# schedule.every().day.at("11:33").do(job_with_argument, name="Peter")

# while True:
#     schedule.run_pending()
#     time.sleep(1)




# import time
# from datetime import datetime

# #     year: SupportsIndex,
# #     month: SupportsIndex,
# #     day: SupportsIndex,
# #     hour: SupportsIndex = ...,
# #     minute: SupportsIndex = ...,
# #     second: SupportsIndex = ...,
# #     microsecond: SupportsIndex = ...
# dt2 = datetime(2018, 1, 1)
# dt = datetime(2019, 1, 1)
# milliseconds = int(round(dt.timestamp() * 1000))
# milliseconds2 = int(round(dt2.timestamp() * 1000))
# print(milliseconds ,"  ||  ", milliseconds2)

# if(milliseconds2>milliseconds): print("milliseconds2 is biggest")
# else : print("milliseconds is biggest")


# from datetime import datetime

# def convert_milliseconds_to_local_time(milliseconds):
#     # Convert milliseconds to seconds
#     seconds = milliseconds / 1000.0
#     # Convert to datetime object in local time
#     local_time = datetime.fromtimestamp(seconds)
#     return local_time

# # Example usage
# milliseconds = 1719471238.3949788
# local_time = convert_milliseconds_to_local_time(milliseconds)
# print("Local time:", local_time)




# get currnet date to convert in milliseconds
# from datetime import datetime
 
# # storing the current time in the variable
# c = datetime.now()

# # Displays Time
# current_time = c.strftime('%H-%M-%S-%d-%m-%Y')
# print(c.strftime('%H-%M-%S-%d-%m-%Y'))


# https://currentmillis.com/    <= best online millisecond to localTime OR localTime to milliseconds


from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
  body="this is trile for the sms",  
  from_=keys.twilio_number,
  to=keys.my_phone_number
)

print(message.sid)