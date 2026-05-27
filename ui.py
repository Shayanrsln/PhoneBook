import customtkinter as ctk
from tkinter import messagebox
from functions import db


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class PhonebookApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Phonebook Manager")
        self.geometry("700x550")
        self.resizable(False, False)

        self.current_frame = None
        self.show_menu()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def show_menu(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.current_frame = frame

        title = ctk.CTkLabel(frame, text="Phonebook Manager", font=("Vazir", 28, "bold"))
        title.pack(pady=30)

        ctk.CTkButton(frame, text="Add Contact", width=250, command=self.show_add_contact).pack(pady=8)
        ctk.CTkButton(frame, text="Show All Contacts", width=250, command=self.show_all_contacts).pack(pady=8)
        ctk.CTkButton(frame, text="Get Contact by Email", width=250, command=self.show_get_contact).pack(pady=8)
        ctk.CTkButton(frame, text="Edit Contact", width=250, command=self.show_edit_contact).pack(pady=8)
        ctk.CTkButton(frame, text="Delete Contact", width=250, command=self.show_delete_contact).pack(pady=8)

    def show_add_contact(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.current_frame = frame

        ctk.CTkLabel(frame, text="Add Contact", font=("Arial", 24, "bold")).pack(pady=20)

        name_entry = ctk.CTkEntry(frame, placeholder_text="Name")
        phone_entry = ctk.CTkEntry(frame, placeholder_text="Phone")
        email_entry = ctk.CTkEntry(frame, placeholder_text="Email")
        address_entry = ctk.CTkEntry(frame, placeholder_text="Address")

        name_entry.pack(pady=8, padx=40, fill="x")
        phone_entry.pack(pady=8, padx=40, fill="x")
        email_entry.pack(pady=8, padx=40, fill="x")
        address_entry.pack(pady=8, padx=40, fill="x")

        def save_contact():
            name = name_entry.get().strip()
            phone = phone_entry.get().strip()
            email = email_entry.get().strip()
            address = address_entry.get().strip()

            if not name or not phone or not email or not address:
                messagebox.showerror("Error", "All fields are required.")
                return

            try:
                db.cursor.execute(
                    "INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                    (name, phone, email, address)
                )
                db.connection.commit()
                messagebox.showinfo("Success", "Contact added successfully.")
                self.show_menu()
            except Exception as e:
                messagebox.showerror("Error", f"Could not add contact:\n{e}")

        ctk.CTkButton(frame, text="Save", command=save_contact).pack(pady=20)
        ctk.CTkButton(frame, text="Back", command=self.show_menu).pack()

    def show_all_contacts(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.current_frame = frame

        ctk.CTkLabel(frame, text="All Contacts", font=("Arial", 24, "bold")).pack(pady=15)

        top_bar = ctk.CTkFrame(frame)
        top_bar.pack(fill="x", padx=10, pady=(0, 10))

        ctk.CTkButton(top_bar, text="Refresh", width=120, command=self.show_all_contacts).pack(side="left", padx=8, pady=8)
        ctk.CTkButton(top_bar, text="Back", width=120, command=self.show_menu).pack(side="right", padx=8, pady=8)

        scroll_frame = ctk.CTkScrollableFrame(frame, label_text="Contacts")
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        try:
            db.cursor.execute("SELECT id, name, phone, email, address FROM contacts ORDER BY id ASC")
            rows = db.cursor.fetchall()

            if not rows:
                ctk.CTkLabel(scroll_frame, text="No contacts found.").pack(pady=20)
                return

            for row in rows:
                contact_box = ctk.CTkFrame(scroll_frame)
                contact_box.pack(fill="x", padx=8, pady=6)

                info_text = (
                    f"ID: {row[0]}\n"
                    f"Name: {row[1]}\n"
                    f"Phone: {row[2]}\n"
                    f"Email: {row[3]}\n"
                    f"Address: {row[4]}"
                )

                ctk.CTkLabel(
                    contact_box,
                    text=info_text,
                    justify="left",
                    anchor="w"
                ).pack(fill="x", padx=12, pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"Could not load contacts:\n{e}")

    def show_get_contact(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.current_frame = frame

        ctk.CTkLabel(frame, text="Get Contact", font=("Arial", 24, "bold")).pack(pady=20)

        email_entry = ctk.CTkEntry(frame, placeholder_text="Enter email")
        email_entry.pack(pady=10, padx=40, fill="x")

        result_box = ctk.CTkTextbox(frame, height=180)
        result_box.pack(padx=40, pady=15, fill="both", expand=False)
        result_box.configure(state="disabled")

        def search_contact():
            email = email_entry.get().strip()

            if not email:
                messagebox.showerror("Error", "Email is required.")
                return

            try:
                db.cursor.execute("SELECT id, name, phone, email, address FROM contacts WHERE email = ?", (email,))
                row = db.cursor.fetchone()

                result_box.configure(state="normal")
                result_box.delete("1.0", "end")

                if row:
                    result_box.insert(
                        "end",
                        f"ID: {row[0]}\n"
                        f"Name: {row[1]}\n"
                        f"Phone: {row[2]}\n"
                        f"Email: {row[3]}\n"
                        f"Address: {row[4]}"
                    )
                else:
                    result_box.insert("end", "No contact found with this email.")

                result_box.configure(state="disabled")

            except Exception as e:
                messagebox.showerror("Error", f"Search failed:\n{e}")

        ctk.CTkButton(frame, text="Search", command=search_contact).pack(pady=8)
        ctk.CTkButton(frame, text="Back", command=self.show_menu).pack()

    def show_edit_contact(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.current_frame = frame

        ctk.CTkLabel(frame, text="Edit Contact", font=("Arial", 24, "bold")).pack(pady=20)

        email_entry = ctk.CTkEntry(frame, placeholder_text="Current email")
        field_entry = ctk.CTkEntry(frame, placeholder_text="Field: name / phone / email / address")
        value_entry = ctk.CTkEntry(frame, placeholder_text="New value")

        email_entry.pack(pady=8, padx=40, fill="x")
        field_entry.pack(pady=8, padx=40, fill="x")
        value_entry.pack(pady=8, padx=40, fill="x")

        def update_contact():
            email = email_entry.get().strip()
            field = field_entry.get().strip().lower()
            new_value = value_entry.get().strip()

            allowed_fields = {"name", "phone", "email", "address"}

            if not email or not field or not new_value:
                messagebox.showerror("Error", "All fields are required.")
                return

            if field not in allowed_fields:
                messagebox.showerror("Error", "Invalid field name.")
                return

            try:
                query = f"UPDATE contacts SET {field} = ? WHERE email = ?"
                db.cursor.execute(query, (new_value, email))
                db.connection.commit()

                if db.cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Contact updated successfully.")
                    self.show_menu()
                else:
                    messagebox.showerror("Error", "No contact found with this email.")

            except Exception as e:
                messagebox.showerror("Error", f"Update failed:\n{e}")

        ctk.CTkButton(frame, text="Update", command=update_contact).pack(pady=20)
        ctk.CTkButton(frame, text="Back", command=self.show_menu).pack()

    def show_delete_contact(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.current_frame = frame

        ctk.CTkLabel(frame, text="Delete Contact", font=("Arial", 24, "bold")).pack(pady=20)

        email_entry = ctk.CTkEntry(frame, placeholder_text="Enter email to delete")
        email_entry.pack(pady=10, padx=40, fill="x")

        def remove_contact():
            email = email_entry.get().strip()

            if not email:
                messagebox.showerror("Error", "Email is required.")
                return

            try:
                db.cursor.execute("DELETE FROM contacts WHERE email = ?", (email,))
                db.connection.commit()

                if db.cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Contact deleted successfully.")
                    self.show_menu()
                else:
                    messagebox.showerror("Error", "No contact found with this email.")

            except Exception as e:
                messagebox.showerror("Error", f"Delete failed:\n{e}")

        ctk.CTkButton(frame, text="Delete", command=remove_contact).pack(pady=20)
        ctk.CTkButton(frame, text="Back", command=self.show_menu).pack()


if __name__ == "__main__":
    app = PhonebookApp()
    app.mainloop()
