import datetime

print("Enter date one in format Day Month Year")
day = int(input())
month = int(input())
year = int(input())

date1 = datetime.datetime(year, month, day)

print("Enter date two in format Day Month Year")
day = int(input())
month = int(input())
year = int(input())

date2 = datetime.datetime(year, month, day)


print((date2-date1).total_seconds(), "between these dates")