from objects import *
from func import *


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip().lower()
        if not user_input:
            print("Please write a command")
            continue
        command, *args = parse_input(user_input)
        
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(book, args))
        elif command == "phone":
            print(show_phone(book, args))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()