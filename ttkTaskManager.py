import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Functions
def add_task():
    task=entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
        save_tasks()

def delete_task():
    selected_task_index=listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
        save_tasks()

# We are going now to save the state
def save_tasks():
    tasks=listbox.get(0,tk.END)
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt","r") as file:
            tasks=file.read().splitlines()
            for task in tasks:
                listbox.insert(tk.END,task)
    except FileNotFoundError:
        pass #Ignore if the file doesn't exist



root=tk.Tk()
root.title("Task Manager")

# Create and configure the listbox
listbox=tk.Listbox(root,selectmode=tk.SINGLE,height=10,width=40)
listbox.pack(padx=10,pady=10)

# Create and configure the entry field
entry=ttk.Entry(root,width=40)
entry.pack(padx=10,pady=5)

# Buttons
b1=ttk.Button(root,text="Add Task",bootstyle=SUCCESS,command=add_task)
b1.pack(side=LEFT,padx=10,pady=10)

b2=ttk.Button(root,text="Delete task",bootstyle=(DANGER,OUTLINE),command=delete_task)
b2.pack(side=LEFT,padx=10,pady=10)

load_tasks()

# Main loop
root.mainloop()