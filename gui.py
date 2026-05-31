import tkinter as tk


root = tk.Tk()

root.title("Mini Security Toolkit")
root.geometry("500x400")


title_label = tk.Label(
    root,
    text="Mini Security Toolkit",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)


tk.Button(root, text="Port Scanner").pack(pady=5)

tk.Button(root, text="System Monitor").pack(pady=5)

tk.Button(root, text="File Integrity Monitor").pack(pady=5)

tk.Button(root, text="Log Analyzer").pack(pady=5)


root.mainloop()
