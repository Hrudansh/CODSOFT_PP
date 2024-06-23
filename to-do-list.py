from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x600")
root.label = Label(root, text='To-Do-List', font='Arial, 25 bold', width=10, bd=5, bg='orange', fg='black')
root.label.pack(side='top', fill=BOTH)

task_listbox = tk.Listbox(root, width=35, height=12, font=('Arial, 15'))
task_listbox.pack(pady=10)

task_entry = tk.Entry(root, width=35, font=('Arial, 15'))
task_entry.pack(pady=10, ipady=5)


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        
add_button = tk.Button(root, text="Add Task", font='Arial, 15 bold', width=10, bd=5, bg='orange', fg='black', command=add_task)
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task",font='Arial, 15 bold', width=10, bd=5, bg='orange', fg='black', command=remove_task)

add_button.pack()
remove_button.pack()

root.mainloop()