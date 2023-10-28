import json
from datetime import datetime
from get_birthdays_list import get_birthdays_per_week

users = []

def get_custom_list_of_users():
    with open('users.json', 'r') as file:
        data = json.load(file)

    for user in data:
        user["birthday"] = datetime.strptime(user["birthday"], '%Y-%m-%d %H:%M:%S')
        users.append(user)

    return users

def task_one():
    print("The list of users whose birthday is today or within the next 6 days. Daily.")

    users = get_custom_list_of_users()

    if users:
        get_birthdays_per_week(users)
