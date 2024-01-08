#Date Time module
import datetime

d=datetime.date(2024,1,1)
print(d)

tday=datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())
print(tday.isocalendar())
    
tdelta=datetime.timedelta(days=7)
print(tday+tdelta)
print(tday-tdelta)

#calculation of my bday from current day
bday=datetime.date(2024,6,18)
till_bday=bday-tday
print(till_bday)

##############################################remaingggggggggggggggggggggggggggggggggggggggggg



