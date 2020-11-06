from datetime import datetime, date, timedelta
import calendar
check_lastday_is_valid = lambda date: date.weekday() < 5
def safe_recursive_check(date, counter = 1):
    if check_lastday_is_valid(date) or counter > 5:
        return date
    else:
        return safe_recursive_check(date-timedelta(1),counter+1)


today_date = date.today()
last_date = today_date.replace(day=calendar.monthrange(datetime.now().year,datetime.now().month)[1])
today_date = datetime.strptime("10/29/20","%m/%d/%y").date()
last_date = today_date.replace(day=calendar.monthrange(datetime.strptime("10/02/20","%m/%d/%y").year,datetime.strptime("10/02/20","%m/%d/%y").month)[1])

print(today_date)
last = safe_recursive_check(last_date)
print(last)

if today_date == last:
    print("last business day")
else:
    print("not the last business day")


# dod = datetime.now().strftime("%m/%d/%y")
# date_time = datetime.strptime(dod,"%m/%d/%y")
# print(dod)
# print(date_time.weekday())
# print(type(date_time))