from datetime import datetime, timedelta
import pytz


previous_month, previous_year = str((datetime.now() - timedelta(days=datetime.now().day)).month), str((datetime.now() - timedelta(days=datetime.now().day)).year)
print(previous_month + "- " + previous_year)
now_dt = datetime.now(pytz.timezone('America/Chicago'))
yesterday_dt = now_dt - timedelta(days=1)
print(str(now_dt.date()))

print(str(yesterday_dt.date()))
formatted_dates = [str(now_dt.date()),str(yesterday_dt.date())]

print(formatted_dates)