import calendar

date = input().split(" ")
year = int(date[2])
month = int(date[0])
day = int(date[1])

print((calendar.day_name[calendar.weekday(year, month, day)]).upper())

