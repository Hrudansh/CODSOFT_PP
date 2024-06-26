import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("280x280")
        self.root.configure(background='orange')

        self.result_entry = tk.Entry(root, width=25, background='white', foreground='red', font=('Ariel, 15'))
        self.result_entry.grid(row=0, column=0, columnspan=4)


        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, width=8, height=3, command=lambda button=button: self.click_button(button), background='white', foreground='red').grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(root, text="Clear", width=38, command=self.clear, background='white', foreground='red').grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.result_entry.get()))
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(tk.END, result)
            except Exception as e:
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(tk.END, "Error")
        else:
            self.result_entry.insert(tk.END, button)

    def clear(self):
        self.result_entry.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()