from typing import Text
import customtkinter as ctk
# اطمینان حاصل کنید که فایل functions.py در همان پوشه است
from functions import read_phonebook, write_phonebook

# ۱. پنجره افزودن و ویرایش (بدون کدهای اضافی جستجو)
class ContactWindow(ctk.CTkToplevel):
    def __init__(self, master, refresh_callback, contact=None):
        super().__init__(master)
        self.refresh_callback = refresh_callback
        self.contact = contact
        self.title("Edit Contact" if contact else "Add New Contact")
        self.geometry("300x400")

        self.entry_name = ctk.CTkEntry(self, placeholder_text="Name")
        self.entry_name.pack(pady=10)
        self.entry_number = ctk.CTkEntry(self, placeholder_text="Number")
        self.entry_number.pack(pady=10)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email (Unique ID)")
        self.entry_email.pack(pady=10)
        self.entry_address = ctk.CTkEntry(self, placeholder_text="Address")
        self.entry_address.pack(pady=10)

        if contact:
            self.entry_name.insert(0, contact['name'])
            self.entry_number.insert(0, contact['number'])
            self.entry_email.insert(0, contact['email'])
            self.entry_email.configure(state="disabled") 
            self.entry_address.insert(0, contact['address'])

        ctk.CTkButton(self, text="Save", command=self.save).pack(pady=20)

    def save(self):
        phonebook = read_phonebook()
        new_data = {
            "name": self.entry_name.get(),
            "number": self.entry_number.get(),
            "email": self.entry_email.get() if not self.contact else self.contact['email'],
            "address": self.entry_address.get()
        }
        if self.contact:
            for i, c in enumerate(phonebook):
                if c['email'] == self.contact['email']:
                    phonebook[i] = new_data
        else:
            phonebook.append(new_data)
        write_phonebook(phonebook)
        self.refresh_callback()
        self.destroy()

# ۲. پنجره اصلی برنامه
class PhoneBookApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PhoneBook Pro")
        self.geometry("800x600")

        # سایدبا
        self.sidebar = ctk.CTkFrame(self, width=500)
        self.sidebar.pack(side="right", fill="y", padx=10, pady=10)

        # نوار جستجو
        
        self.search_entry = ctk.CTkEntry(self.sidebar, placeholder_text="Search...")
        self.search_entry.pack(pady=10, padx=10)
        self.search_entry.bind("<KeyRelease>", lambda event: self.show_contacts())

        #ctk.CTkButton(self.sidebar, text="List All", command=self.show_contacts).pack(pady=10, padx=10)
        ctk.CTkButton(self.sidebar, text="Add Contact", command=lambda: ContactWindow(self, self.show_contacts)).pack(pady=10, padx=10)

        self.display_area = ctk.CTkScrollableFrame(self, label_text="Contacts List")
        self.display_area.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        self.show_contacts()

    def show_contacts(self):
        for widget in self.display_area.winfo_children():
            widget.destroy()

        query = self.search_entry.get().lower()
        contacts = read_phonebook()
        contacts.reverse() 

        filtered = [c for c in contacts if query in c['name'].lower() or query in c['number']]

        for contact in filtered:
            row = ctk.CTkFrame(self.display_area, fg_color="transparent")
            row.pack(fill="x", pady=2)
            btn_name = ctk.CTkButton(row, text=contact['name'], fg_color="transparent", 
                                     anchor="w", command=lambda c=contact: self.open_details(c))
            btn_name.pack(side="left", fill="x", expand=True)
            ctk.CTkButton(row, text="Delete", width=50, fg_color="red", 
                          command=lambda c=contact['email']: self.delete_contact(c)).pack(side="right", padx=5)
            ctk.CTkButton(row, text="Edit", width=50, fg_color="orange",
                          command=lambda c=contact: ContactWindow(self, self.show_contacts, c)).pack(side="right", padx=5)

    def open_details(self, contact):
        detail_win = ctk.CTkToplevel(self)
        detail_win.title(f"Details: {contact['name']}")
        detail_win.geometry("300x250")
        ctk.CTkLabel(detail_win, text=f"Name: {contact['name']}", font=("Arial", 16, "bold")).pack(pady=10)
        ctk.CTkLabel(detail_win, text=f"Number: {contact['number']}").pack(pady=5)
        ctk.CTkLabel(detail_win, text=f"Email: {contact['email']}").pack(pady=5)
        ctk.CTkLabel(detail_win, text=f"Address: {contact['address']}").pack(pady=5)
        ctk.CTkButton(detail_win, text="Close", command=detail_win.destroy).pack(pady=20)

    def delete_contact(self, email):
        phonebook = [c for c in read_phonebook() if c['email'] != email]
        write_phonebook(phonebook)
        self.show_contacts()

if __name__ == "__main__":
    app = PhoneBookApp()
    app.mainloop()
