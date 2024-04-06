#ex1
from datetime import datetime, timedelta
current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print(current_date)
print(new_date)

#ex2
from datetime import datetime, timedelta
current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(yesterday.strftime("%Y-%m-%d"))
print(current_date.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

#ex3
from datetime import datetime
current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print(current_datetime)
print(current_datetime_without_microseconds)

#ex4
from datetime import datetime

date1 = input()
date2 = input()

difference_seconds = (date1 - date2).total_seconds()

print(difference_seconds)


