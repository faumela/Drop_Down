import datetime
import calendar



x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%D"))
print(x.strftime("%A"))

y = datetime.datetime(2021,1,17)

print(y)

cal = calendar.month(2019,1,17)
print(cal)
