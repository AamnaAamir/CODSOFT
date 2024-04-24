import tkinter as tk
from tkinter import ttk, messagebox
import json

root = tk.Tk()
root.title("Todo List App")
root.geometry("400x600")
root.resizable(False, False)
style = ttk.Style(root)
style.theme_use("clam")


def view_stats():
    done_count = 0
    total_count = task_list.size()
    for i in range(total_count):
        if task_list.get(i).startswith("✓"):
            done_count += 1
    messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")


def add_task():
    task = task_input.get()
    if task and task != "Enter your todo here...":
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)
        save_tasks()


def mark_done():
    selected_tasks = task_list.curselection()
    for task_index in selected_tasks:
        task_text = task_list.get(task_index)
        if not task_text.startswith("✓"):
            task_list.delete(task_index)
            task_list.insert(task_index, "✓ " + task_text)
            task_list.itemconfig(task_index, fg="black")
    save_tasks()


def delete_task():
    selected_tasks = task_list.curselection()
    if selected_tasks:
        for task_index in reversed(selected_tasks):
            task_list.delete(task_index)
        save_tasks()
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")


def clear_placeholder(event):
    if task_input.get() == "Enter your todo here...":
        task_input.delete(0, tk.END)


def restore_placeholder(event):
    if not task_input.get():
        task_input.insert(0, "Enter your todo here...")


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            for task in data:
                task_text = task["text"]
                if task["color"] == "black":
                    task_text = "✓ " + task_text
                task_list.insert(tk.END, task_text)
                task_list.itemconfig(tk.END, fg=task["color"])
    except FileNotFoundError:
        pass


def save_tasks():
    data = []
    for i in range(task_list.size()):
        text = task_list.get(i)
        color = task_list.itemcget(i, "fg")
        data.append({"text": text, "color": color})
    with open("tasks.json", "w") as f:
        json.dump(data, f)


style.configure("Custom.TButton",
                background="#004080",
                foreground="white",
                font=("Helvetica", 12, "bold"))

style.map("Custom.TButton",
          background=[("active", "#0059b3")],
          foreground=[("active", "white")])

style.configure("Custom.TFrame",
                background="#272727",
                borderwidth=2,
                relief="groove")

task_input = ttk.Entry(root, font=("Helvetica", 12), width=30)
task_input.pack(pady=10)
task_input.insert(0, "Enter your todo here...")
task_input.bind("<FocusIn>", clear_placeholder)
task_input.bind("<FocusOut>", restore_placeholder)

add_button = ttk.Button(root, text="Add", command=add_task, style="Custom.TButton")
add_button.pack(pady=5)

task_list_frame = ttk.Frame(root, style="Custom.TFrame")
task_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

task_list_scroll = ttk.Scrollbar(task_list_frame)
task_list_scroll.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(task_list_frame, font=("Helvetica", 12), yscrollcommand=task_list_scroll.set, selectmode=tk.MULTIPLE)
task_list.pack(fill=tk.BOTH, expand=True)

task_list_scroll.config(command=task_list.yview)

done_button = ttk.Button(root, text="Done", command=mark_done, style="Custom.TButton")
done_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", command=delete_task, style="Custom.TButton")
delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

stats_button = ttk.Button(root, text="View Stats", command=view_stats, style="Custom.TButton")
stats_button.pack(side=tk.BOTTOM, pady=10)

load_tasks()

root.mainloop()
