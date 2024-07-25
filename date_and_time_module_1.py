import datetime
'''

current_time = datetime.datetime.now()
print(current_time)
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.weekday())
print(current_time.date())
print(current_time.time())
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)
print(current_time.ctime())
print(current_time.today())
print(current_time.now())
print(current_time.timetuple())
###################################33
test_time = datetime.date(2023,11,10)
print(test_time)
print(type(test_time))
print((test_time.year))
print((test_time.month))
print((test_time.day))

from datetime import datetime

import_module = (datetime.now())
print(import_module.day)
print(import_module.month)

import datetime as dt
date = (dt.datetime.now())
print(date)
print(date.month)
print(date.day)
print(date.year)

# compare date
from datetime import datetime

todays_time = datetime.now()
print(todays_time)

future_time = datetime.now()
print(future_time)

#difference = (future_time-todays_time)
difference = (future_time-todays_time).microseconds
print(difference)

from datetime import datetime
start_time = datetime.strptime("2:13:45", "%H:%M:%S")
end_time = datetime.strptime("12:3:55", "%H:%M:%S")

diff = (end_time-start_time)
print(diff)
sec = (diff.total_seconds())
print("difference in seconds ", sec)
min = (sec/60)
print("difference in minutes", min)
hours = (min/60)
print("difference in hours  ",hours)
'''

import pytz
import datetime

pst = pytz.timezone('Asia/Karachi')
print(datetime.datetime.now(pst))
print(type(datetime.datetime.now(pst)))
print(pst)
print(dir(pytz))
