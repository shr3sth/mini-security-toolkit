import tkinter as tk

from modules.system_monitor import get_system_info
from modules.log_analyzer import analyze_log
from modules.file_integrity import (
    save_baseline,
    verify_integrity
)
from modules.port_scanner import scan_ports


def show_system_monitor():

    output_box.delete("1.0", tk.END)

    output_box.insert(
        tk.END,
        get_system_info()
    )


def gui_port_scan():

    try:

        target = target_entry.get()

        start_port = int(
            start_port_entry.get()
        )

        end_port = int(
            end_port_entry.get()
        )

        result = scan_ports(
            target,
            start_port,
            end_port
        )

        output_box.delete("1.0", tk.END)

        output_box.insert(
            tk.END,
            result
        )

    except ValueError:

        output_box.delete("1.0", tk.END)

        output_box.insert(
            tk.END,
            "Please enter valid port numbers."
        )


def show_log_analysis():

    output_box.delete("1.0", tk.END)

    output_box.insert(
        tk.END,
        analyze_log()
    )


def gui_save_baseline():

    filepath = filepath_entry.get()

    result = save_baseline(filepath)

    output_box.delete("1.0", tk.END)

    output_box.insert(
        tk.END,
        result
    )


def gui_verify_integrity():

    filepath = filepath_entry.get()

    result = verify_integrity(filepath)

    output_box.delete("1.0", tk.END)

    output_box.insert(
        tk.END,
        result
    )


root = tk.Tk()

root.title("Mini Security Toolkit")
root.geometry("700x850")


title_label = tk.Label(
    root,
    text="Mini Security Toolkit",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)


filepath_label = tk.Label(
    root,
    text="File Path:"
)

filepath_label.pack()

filepath_entry = tk.Entry(
    root,
    width=50
)

filepath_entry.pack(pady=5)

target_label = tk.Label(
    root,
    text="Target:"
)

target_label.pack()

target_entry = tk.Entry(
    root,
    width=50
)

target_entry.pack(pady=5)


start_port_label = tk.Label(
    root,
    text="Start Port:"
)

start_port_label.pack()

start_port_entry = tk.Entry(
    root,
    width=20
)

start_port_entry.pack(pady=5)


end_port_label = tk.Label(
    root,
    text="End Port:"
)

end_port_label.pack()

end_port_entry = tk.Entry(
    root,
    width=20
)

end_port_entry.pack(pady=5)


tk.Button(
    root,
    text="Port Scanner",
    command=gui_port_scan
).pack(pady=5)

tk.Button(
    root,
    text="System Monitor",
    command=show_system_monitor
).pack(pady=5)

tk.Button(
    root,
    text="Save Baseline",
    command=gui_save_baseline
).pack(pady=5)

tk.Button(
    root,
    text="Verify Integrity",
    command=gui_verify_integrity
).pack(pady=5)

tk.Button(
    root,
    text="Log Analyzer",
    command=show_log_analysis
).pack(pady=5)


output_box = tk.Text(
    root,
    height=15,
    width=70
)

output_box.pack(pady=20)


root.mainloop()
