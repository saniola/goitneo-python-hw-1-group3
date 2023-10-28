from collections import defaultdict
from datetime import datetime, timedelta

def get_today():
    return datetime.today().date()

def print_results(birthdays_per_week):
    today = get_today()
    current_weekday = today.weekday()

    for _ in range(7):
        day = (current_weekday % 7)
        day_name = today.strftime("%A")

        if day_name in birthdays_per_week:
            names = birthdays_per_week[day_name]
            print(f"{day_name}: {', '.join(names)}")

        today += timedelta(days=1)
        current_weekday += 1

def get_next_week_birthdays(users, birthdays_per_week):
    today = get_today()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 6:
            if birthday_this_year.weekday() == 5:
                delta_days += 2
            elif birthday_this_year.weekday() == 6:
                delta_days += 1

            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            birthdays_per_week[birthday_weekday].append(name)

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    get_next_week_birthdays(users, birthdays_per_week)
    print_results(birthdays_per_week)
