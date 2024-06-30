import tkinter as tk
import customtkinter as ctk
import random
import string
from tkinter import messagebox

class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("350x400")
        self.title("Password Generator")
        self.configure(bg="#2f2f2f")

        self.grid_columnconfigure(1, weight=1)

        self.length_label = ctk.CTkLabel(self, text="Length:", font=("Times", 20, "bold"), text_color="white", corner_radius=6, bg_color="#2f2f2f")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = ctk.CTkEntry(self, width=200, height=30, font=("Times", 14), text_color="black", fg_color="white", bg_color="#2f2f2f")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.use_uppercase_var = tk.BooleanVar()
        self.use_uppercase_checkbox = ctk.CTkCheckBox(self, text="Use Uppercase", variable=self.use_uppercase_var, font=("Arial", 14), text_color="white", bg_color="#2f2f2f", fg_color="#4CAF50")
        self.use_uppercase_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.use_numbers_var = tk.BooleanVar()
        self.use_numbers_checkbox = ctk.CTkCheckBox(self, text="Use Numbers", variable=self.use_numbers_var, font=("Arial", 14), text_color="white", bg_color="#2f2f2f", fg_color="#4CAF50")
        self.use_numbers_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.use_special_chars_var = tk.BooleanVar()
        self.use_special_chars_checkbox = ctk.CTkCheckBox(self, text="Use Special Characters", variable=self.use_special_chars_var, font=("Arial", 14), text_color="white", bg_color="#2f2f2f", fg_color="#4CAF50")
        self.use_special_chars_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.generate_button = ctk.CTkButton(self, text="Generate Password", command=self.create_password, font=("Times", 20, "bold"), text_color="white", fg_color="#4CAF50", hover_color="#3e8e41")
        self.generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = ctk.CTkLabel(self, text="Password:", font=("Times", 20, "bold"), text_color="white", corner_radius=6, bg_color="#2f2f2f")
        self.password_label.grid(row=5, column=0, padx=10, pady=10)

        self.password_entry = ctk.CTkEntry(self, width=200, height=30, font=("Arial", 14), text_color="black", fg_color="white", bg_color="#2f2f2f")
        self.password_entry.grid(row=5, column=1, padx=10, pady=10)

        self.copy_button = ctk.CTkButton(self, text="Copy to Clipboard", command=self.copy_password, font=("Times", 20, "bold"), text_color="white", fg_color="#4CAF50", hover_color="#3e8e41")
        self.copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self, length, use_uppercase, use_numbers, use_special_chars):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def create_password(self):
        length = int(self.length_entry.get())
        use_uppercase = self.use_uppercase_var.get()
        use_numbers = self.use_numbers_var.get()
        use_special_chars = self.use_special_chars_var.get()

        password = self.generate_password(length, use_uppercase, use_numbers, use_special_chars)
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, password)

    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_entry.get())
        messagebox.showinfo("Copied", "Password copied to clipboard")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()