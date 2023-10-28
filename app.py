from task_one import task_one

def app():
    print('''
        Welcome to HW#01 completed by Oleksandr Kydanov in Python for GoIT Neoversity.

        ####
        Please enter:
            0 to exit the menu
            1 to search for a list of birthdays in the next week.
            2 to call the assistant bot.
        ####
    ''')

    while True:
        value = input(">>> ")
        if value == "1":
            task_one()
            break
        elif value == "2":
            print("Task 2 selected")
            break
        elif value == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 0.")
