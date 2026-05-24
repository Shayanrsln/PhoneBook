import json
#dar soorat naboodan phone-book.json oon ro misaze
def read_phonebook(path="phone-book.json"):
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    except FileNotFoundError:
        return []

# baz nevisi dar file phone-book.json
def write_phonebook(phonebook):
    with open("phone-book.json", 'w', encoding='utf-8') as json_file:
        json.dump(phonebook, json_file, indent=1, ensure_ascii=False)
#in method contact ro baramoon print migire 
def get_contact(email):
    phonebook = read_phonebook()
    for contact in phonebook:
        if contact["email"] == email:
            return contact
    return None

# in method hame info haro dakhel temp mirize va append mishe tooye phone-book
def add_contact():
    phonebook = read_phonebook()
    name = input("enter your name: ")
    number = input("enter your number: ")
    email = input("enter your email: ")
    address = input("enter your address: ")

    temp = {"name":name, "number":number, "email":email, "address":address}

    phonebook.append(temp)
    write_phonebook(phonebook)

# in method email ro be onvan input migire va dar soorat sahih boodan amaliat edit ro rooye in email ejra mikone
def edit_contact():
    z = input("email: ") # فرض کنیم اینجا ایمیل وارد می‌شود
    contact = get_contact(z)
    if contact is None:
        print("Contact not found!")
        return
    key = input("what do you want to edit? [name | number | address | email ]: ")
    value = input("value: ")
    contact[key] = value

    phonebook = read_phonebook()

    for item in phonebook:
        if item["email"] == z:
            item.update(contact)
            break
        
    write_phonebook(phonebook)

# pak kardan contact
def delete_contact():
    phonebook = read_phonebook()
    are_u_sure = input("are u sure to delete contact? ")
    if are_u_sure.lower() == "yes":
        x = input("email ro vared konid :")
        contact = get_contact(x)
        if contact:
            phonebook.remove(contact)
            write_phonebook(phonebook)
            print(f"{contact['name']} delete succsseful")
        else:
            print("user not found")

    else:
        return
