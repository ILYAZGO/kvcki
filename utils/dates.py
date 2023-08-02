from datetime import datetime, timedelta

current_date = datetime.now()

today = current_date.strftime("%d/%m/%Y")

yesterday = (current_date - timedelta(days=1)).strftime("%d/%m/%Y")

first_day_week_ago = (current_date - timedelta(days=6)).strftime("%d/%m/%Y")

# if today not 31, calendar shows month period like (today - 29 days), if 31 or 01 (today - 30 days). wtf
# so we need this if statement
# ---------------------------------------------------------------------------------

if current_date.strftime("%d") == "31":
    first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
elif current_date.strftime("%d") == "01":
    first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
else:
    first_day_month_ago = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
# ----------------------------------------------------------------------------------

first_day_year_ago = (current_date - timedelta(days=364)).strftime("%d/%m/%Y")


