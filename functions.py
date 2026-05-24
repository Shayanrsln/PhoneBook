import os
from sqlite3 import connect
from database import Db

db = Db("phonebook.db")

# این تابع رو تغییر دادیم که فقط جدول رو بسازه
def ensure_table_exists():
    db.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, email TEXT, address TEXT)")
    db.connection.commit()

# حالا اول مطمئن شو جدول هست، بعد تابع ثبت رو صدا بزن
ensure_table_exists()

def creat_contact():
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    query = "INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)"
    data = (name, number, email, address)
    
    db.cursor.execute(query, data)
    db.connection.commit()
    print("import succes")

def get_contact():
    email_input = input("Enter email: ")
    query = "SELECT * FROM contacts WHERE email = ?"
    db.cursor.execute(query, (email_input,))
    row = db.cursor.fetchone()

    if row:
        print(row)
    else:
        print("No contact found with this email.")


def edit_contact():
    # ۱. پیدا کردن مخاطب بر اساس ایمیل
    target_email = input("Enter the email of the contact to update: ")
    db.cursor.execute("SELECT * FROM contacts WHERE email = ?", (target_email,))
    contact = db.cursor.fetchone()

    if not contact:
        print("Contact not found!")
        return

    # ۲. پرسیدن اینکه چه فیلدی ویرایش شود
    print("Which field do you want to update? (name, phone, email, address)")
    field = input("Enter field name: ").lower()

    if field not in ['name', 'phone', 'email', 'address']:
        print("Invalid field!")
        return

    # ۳. گرفتن مقدار جدید
    new_value = input(f"Enter new {field}: ")

    # ۴. اجرای آپدیت (استفاده از F-string برای نام ستون امن است چون از لیستِ مجاز چک شده)
    query = f"UPDATE contacts SET {field} = ? WHERE email = ?"
    db.cursor.execute(query, (new_value, target_email))
    db.connection.commit()
    
    print(f"Contact {field} updated successfully!")

def delete_contact():
    email = input("email ro vared konid: ")
    query = "DELETE FROM contacts WHERE email = ? "
    db.cursor.execute(query, (email,))
    db.connection.commit()
    if db.cursor.rowcount > 0:
        print("delete succes")
    else:
        print("No Contact found with this email!!")
    