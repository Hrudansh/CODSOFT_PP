import customtkinter as ct
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number=None, email=None, address=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number=None, email=None, address=None):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contact_list(self):
        contact_list = ""
        for i, contact in enumerate(self.contacts, 1):
            contact_list += f"{i}. {contact.name} - {contact.phone_number or 'No phone number'}\n"
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self, query=None):
        if query is None:
            query = ""
        results = [contact for contact in self.contacts if query in contact.name or query in (contact.phone_number or '')]
        if not results:
            messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            result_list = ""
            for i, contact in enumerate(results, 1):
                result_list += f"{i}. {contact.name} - {contact.phone_number or 'No phone number'}\n"
            messagebox.showinfo("Search Results", result_list)

    def update_contact(self, old_name, new_name=None, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == old_name:
                if new_name:
                    contact.name = new_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                messagebox.showinfo("Success", "Contact updated successfully!")
                return
        messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return
        messagebox.showinfo("Error", "Contact not found.")

class GUI(ct.CTk):
    def __init__(self):
        super().__init__()

        self.contact_manager = ContactManager()

        self.geometry("600x600")
        self.title("Contact Book")

        self.name_label = ct.CTkLabel(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ct.CTkEntry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_number_label = ct.CTkLabel(self, text="Phone Number:")
        self.phone_number_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_number_entry = ct.CTkEntry(self)
        self.phone_number_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = ct.CTkLabel(self, text="Email (optional):")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = ct.CTkEntry(self)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = ct.CTkLabel(self, text="Address (optional):")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = ct.CTkEntry(self)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = ct.CTkButton(self, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = ct.CTkButton(self, text="View Contact List", command=self.view_contact_list)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.search_label = ct.CTkLabel(self, text="Search:")
        self.search_label.grid(row=5, column=0, padx=10, pady=10)
        self.search_entry = ct.CTkEntry(self)
        self.search_entry.grid(row=5, column=1, padx=10, pady=10)
        self.search_button = ct.CTkButton(self, text="Search", command=lambda: self.search_contact(self.search_entry.get()))
        self.search_button.grid(row=5, column=2, padx=10, pady=10)

        self.update_button =ct.CTkButton(self, text="Update Contact", command=self.update_contact_page)
        self.update_button.grid(row=6, column=0, padx=10, pady=10)

        self.delete_button = ct.CTkButton(self, text="Delete Contact", command=self.delete_contact_page)
        self.delete_button.grid(row=6, column=1, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contact_manager.add_contact(name, phone_number, email, address)
        self.name_entry.delete(0, 'end')
        self.phone_number_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')

    def view_contact_list(self):
        self.contact_manager.view_contact_list()

    def search_contact(self, query):
        self.contact_manager.search_contact(query)

    def update_contact_page(self):
        self.update_window = ct.CTkToplevel(self)
        self.update_window.title("Update Contact")

        self.search_label = ct.CTkLabel(self.update_window, text="Search for contact:")
        self.search_label.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = ct.CTkEntry(self.update_window)  
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)
        self.search_button = ct.CTkButton(self.update_window, text="Search", command=lambda: self.search_contact(self.search_entry.get()))
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.old_name_label = ct.CTkLabel(self.update_window, text="Old Name:")
        self.old_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.old_name_entry = ct.CTkEntry(self.update_window)
        self.old_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.new_name_label = ct.CTkLabel(self.update_window, text="New Name:")
        self.new_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_name_entry = ct.CTkEntry(self.update_window)
        self.new_name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.new_phone_number_label = ct.CTkLabel(self.update_window, text="New Phone Number (optional):")
        self.new_phone_number_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_phone_number_entry = ct.CTkEntry(self.update_window)
        self.new_phone_number_entry.grid(row=3, column=1, padx=10, pady=10)

        self.new_email_label = ct.CTkLabel(self.update_window, text="New Email (optional):")
        self.new_email_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_email_entry = ct.CTkEntry(self.update_window)
        self.new_email_entry.grid(row=4, column=1, padx=10, pady=10)

        self.new_address_label = ct.CTkLabel(self.update_window, text="New Address (optional):")
        self.new_address_label.grid(row=5, column=0, padx=10, pady=10)
        self.new_address_entry = ct.CTkEntry(self.update_window)
        self.new_address_entry.grid(row=5, column=1, padx=10, pady=10)

        self.update_button = ct.CTkButton(self.update_window, text="Update Contact", command=lambda: self.contact_manager.update_contact(self.old_name_entry.get(), self.new_name_entry.get(), self.new_phone_number_entry.get(), self.new_email_entry.get(), self.new_address_entry.get()))
        self.update_button.grid(row=6, column=0, padx=10, pady=10)

    def delete_contact_page(self):
        self.delete_window = ct.CTkToplevel(self)
        self.delete_window.title("Delete Contact")

        self.delete_name_label = ct.CTkLabel(self.delete_window, text="Name:")
        self.delete_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.delete_name_entry = ct.CTkEntry(self.delete_window)  
        self.delete_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.delete_button = ct.CTkButton(self.delete_window, text="Delete Contact", command=lambda: self.contact_manager.delete_contact(self.delete_name_entry.get()))
        self.delete_button.grid(row=1, column=0, padx=10, pady=10)

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()