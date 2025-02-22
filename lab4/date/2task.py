import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday was:", yesterday.strftime('%d.%m.%Y'))
print("Today is:", today.strftime('%d.%m.%Y'))
print("Tommorow will be:", tomorrow.strftime('%d.%m.%Y'))