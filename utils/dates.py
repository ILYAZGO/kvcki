from datetime import datetime, timedelta
import calendar

#.strftime("%d/%m/%Y")
#.strftime("%Y-%m-%d")

today = datetime.now()
yesterday = (today - timedelta(days=1))

first_day_this_week = today - timedelta(days=today.weekday())
last_day_this_week = first_day_this_week + timedelta(days=6)

first_day_last_week = first_day_this_week - timedelta(days=7)
last_day_last_week = first_day_last_week + timedelta(days=6)

first_day_this_month = today.replace(day=1)
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
last_day_this_month = today.replace(day=days_in_current_month)


first_day_last_month = today - timedelta(days=today.month)
print(first_day_last_month)
# last_day_last_month =
#
# first_day_this_month =
# last_day_this_month =

#first_day_last_quarter =
#last_day_last_quarter =

#first_day_this_quarter =
#last_day_this_quarter =

#first_day_last_year =
#last_day_last_year =

#first_day_this_year =
#last_day_this_year =




tomorrow = (today + timedelta(days=1)).strftime("%d/%m/%Y")
tomorrow_with_dash = (today + timedelta(days=1)).strftime("%Y-%m-%d") # for quotas test

first_day_week_ago = (today - timedelta(days=6)).strftime("%d/%m/%Y")


first_day_year_ago = (today - timedelta(days=365)).strftime("%d/%m/%Y")


