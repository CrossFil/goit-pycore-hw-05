'''bot assistant'''
def parse_input(user_input):
    '''отримання данних'''
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    '''додавання контакту'''
    if len(args) != 2:
        return "Invalid arguments. Please provide username and phone."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    '''зміна даних контакту'''
    if len(args) != 2:
        return "Invalid arguments. Please provide username and new phone."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number updated for {name}."
    else:
        return f"{name} not found in contacts."

def get_phone(args, contacts):
    '''виведення даних контакту'''
    if len(args) != 1:
        return "Invalid arguments. Please provide username."
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"{name} not found in contacts."

def show_all_contacts(contacts):
    '''виведення всіх контактів'''
    if not contacts:
        return "No contacts available."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def input_error(func):
    '''декоратор обробки помилок'''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Invalid command. Enter a valid command.'
        except ValueError:
            return 'Invalid arguments. Please provide valid arguments.'
        except IndexError:
            return 'Invalid arguments. Please provide all necessary arguments.'
    return inner

@input_error
def add_contacts_decorated(args, contacts):
    '''chek for error'''
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact_decorated(args, contacts):
    '''chek for error'''
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    if name in contacts:
        contacts[name] = phone
        return f'Phone numer updated for {name}.'
    else:
        raise KeyError(name)

@input_error
def get_phone_decorated(args, contacts):
    '''chek for error'''
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f'Phone numer for {name}: {contacts[name]}'
    else:
        return KeyError(name)

@input_error
def show_all_contacts_decorated(contacts):
    '''chek for error'''
    if not contacts:
        return 'No contacts available.'
    else:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])


def main():
    '''точка входу'''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts_decorated(args, contacts))
        elif command == "change":
            print(change_contact_decorated(args, contacts))
        elif command == "phone":
            print(get_phone_decorated(args, contacts))
        elif command == "all":
            print(show_all_contacts_decorated(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
