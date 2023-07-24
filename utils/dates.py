from datetime import datetime, timedelta

current_date = datetime.now()

today = current_date.strftime("%d/%m/%Y")

yesterday = (current_date - timedelta(days=1)).strftime("%d/%m/%Y")

first_day_week_ago = (current_date - timedelta(days=6)).strftime("%d/%m/%Y")

first_day_month_ago = (current_date - timedelta(days=29)).strftime("%d/%m/%Y")

first_day_year_ago = (current_date - timedelta(days=364)).strftime("%d/%m/%Y")

