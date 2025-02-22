import datetime

xdate = datetime.datetime.now() - datetime.timedelta(days=5)
print("Five days ago it was:", xdate.strftime('%d.%m.%Y, %H:%M'))