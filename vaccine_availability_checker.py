import requests
from datetime import  datetime,timedelta
import json

todays_date=datetime.today()
days=int(input("Enter number of days "))
dates=[]
for d in range(days):
    dates.append(todays_date+timedelta(d))
finaldates=[]

for f in dates:
    finaldates.append(f.strftime("%d%m%y"))
pincode=int(input("Enter pincode "))
pincodes=[]
pincodes.append(pincode)
print("\n")
for pin in pincodes:
    for fdates in finaldates:
        URL="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin,fdates)
        data=requests.get(URL)
        actual_data=data.json()
        for center in actual_data["centers"]:
            for session in center["sessions"]:
                print("Pincode:",pin)
                print("Date:",fdates)
                print("Center Name:",center["name"])
                print("Address:",center["address"])
                print("Vaccine Type:",session["vaccine"])
                print("Fees:",center["fee_type"])
                print("\n")
