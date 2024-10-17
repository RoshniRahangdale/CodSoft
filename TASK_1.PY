#----------1ST TASK -----------#
# ------TO DO LIST-------- # 

import tkinter as tk
from tkinter import messagebox

tasks = []


def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

#  remove task
def delete_task():
    try:
        task = task_listbox.get(task_listbox.curselection())
        
        tasks.remove(task)
        update_task_list()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

#  mark task as completed
def mark_completed():
    try:
        task = task_listbox.get(task_listbox.curselection())
        idx = tasks.index(task)
        tasks[idx] = f"{task} (completed)"
        update_task_list()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")


def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


root = tk.Tk()
root.title("To-Do List Application")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

root.mainloop()










