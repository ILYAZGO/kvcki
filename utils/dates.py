from datetime import datetime, timedelta
import calendar



current_date = datetime.now()

today = current_date.strftime("%d/%m/%Y")

yesterday = (current_date - timedelta(days=1)).strftime("%d/%m/%Y")

first_day_week_ago = (current_date - timedelta(days=6)).strftime("%d/%m/%Y")


days_in_current_month = calendar.monthrange(current_date.year, current_date.month)[1]

#first_day_month_ago = (current_date - timedelta(days=29)).strftime("%d/%m/%Y") #(current_date + relativedelta(weeks=-4)).strftime("%d/%m/%Y")                   #(current_date - timedelta(days=30)).strftime("%d/%m/%Y")

if days_in_current_month == 31:
    first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
elif days_in_current_month == 30:
    first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
#elif days_in_current_month == 29:
 #   first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
else:
    first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
# ----------------------------------------------------------------------------------

first_day_year_ago = (current_date - timedelta(days=365)).strftime("%d/%m/%Y")


