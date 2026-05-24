from functions import get_contact, add_contact, edit_contact, delete_contact

def main():
    print("welcome to your phonebook")
    
    print("hint: [get | add | edit | remove]")
    request_type = input("what do yo want? ")

    if request_type == "add":
        add_contact()

    if request_type == "get":
        email = input("enter your email: ")
        record = get_contact(email)
        print(record)

    if request_type == "edit":
        edit_contact()

    if request_type == "remove":
        delete_contact()

main()