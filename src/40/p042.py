import datetime as dt

month = int(input())
day = int(input())

date = dt.datetime(2020, month, day)
day_str = date.strftime('%A')

print(day_str[:3].upper())
print(date.weekday())
