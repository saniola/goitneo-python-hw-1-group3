def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'add [name] [phone number]'."

    name, phone = args
    name = name.lower()
    contacts[name] = phone

    return f"Contact {name} with phone number {phone} added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'change [name] [new phone number]'."

    name, new_phone = args
    name = name.lower()

    if name in contacts:
        contacts[name] = new_phone

        return f"Contact {name} updated. New phone number: {new_phone}."
    else:
        return f"Error: Contact with name {name} not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid number of arguments. Use 'phone [name]'."

    name = args[0]
    name = name.lower()

    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}."
    else:
        return f"Error: Contact with name {name} not found."

def show_all(contacts):
    if not contacts:
        return "The contacts list is empty."
    else:
        result = "All saved contacts with phone numbers:\n"

        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result

def task_two():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")

            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

if __name__ == '__main__':
    task_two()
