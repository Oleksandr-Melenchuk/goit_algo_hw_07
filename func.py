from decorators import *
from objects import *

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if record.birthday:
        return f"{name}  birthday: {record.birthday.value}"
    return "Birthday not set."


@input_error
def birthdays(book):
    upcoming = book.get_upcoming_birthdays()
    return "\n".join([f"{item['name']}: {item['birthday']}" for item in upcoming]) or "No upcoming birthdays."

@input_error
def change_contact(book: AddressBook, args):
    
    name, new_phone = args
    record = book.find(name)
    
    if not record:
        raise KeyError("User not found")
    
    if not Phone.number_check(new_phone):
        raise ValueError("Invalid symbols in number")

    if record.phones:
        old_phone = record.phones[0].value
        record.edit_phone(old_phone, new_phone)
    else:
        record.add_phone(new_phone)
    
    return "Contact updated"


@input_error
def show_phone(book: AddressBook, args):
    if not args:
        raise ValueError("Please provide a name.")

    name = args[0]
    record = book.find(name)

    if not record:
        raise KeyError("Contact not found")

    if not record.phones:
        return f"{name} has no phone numbers."

    phones_str = "; ".join(phone.value for phone in record.phones)
    return f"{name}: {phones_str}"


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "Contact list is empty"
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book):
    name, date = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(date)
    return "Birthday added."


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args