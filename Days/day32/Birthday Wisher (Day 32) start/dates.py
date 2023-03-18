import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
print(now)

date_of_birth = dt.datetime(year=1994, month=12, day=9, hour=4)
print(date_of_birth)