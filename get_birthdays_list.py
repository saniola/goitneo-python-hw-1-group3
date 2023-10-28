from collections import defaultdict
from datetime import datetime, timedelta

def get_today():
    return datetime.today().date()

def print_results(birthdays_per_week):
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

def get_next_week_birthdays(users, birthdays_per_week):
    today = get_today()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        delta_days = (birthday_this_year - today).days

        birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")

        if 0 <= delta_days <= 6:
            birthdays_per_week[birthday_weekday].append(name)

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    get_next_week_birthdays(users, birthdays_per_week)
    print_results(birthdays_per_week)
