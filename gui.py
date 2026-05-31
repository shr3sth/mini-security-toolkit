import tkinter as tk
from tkinter import messagebox

from modules.system_monitor import get_system_info


def show_system_monitor():

    info = get_system_info()

    messagebox.showinfo(
        "System Resource Monitor",
        info
    )


root = tk.Tk()

root.title("Mini Security Toolkit")
root.geometry("500x400")


title_label = tk.Label(
    root,
    text="Mini Security Toolkit",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)


tk.Button(
    root,
    text="Port Scanner"
).pack(pady=5)

tk.Button(
    root,
    text="System Monitor",
    command=show_system_monitor
).pack(pady=5)

tk.Button(
    root,
    text="File Integrity Monitor"
).pack(pady=5)

tk.Button(
    root,
    text="Log Analyzer"
).pack(pady=5)


root.mainloop()
