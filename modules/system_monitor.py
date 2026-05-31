import psutil


def show_system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("\n=== System Resource Monitor ===\n")

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Available Memory: {round(memory.available / (1024**3), 2)} GB")

    print(f"\nDisk Usage: {disk.percent}%")
    print(f"Free Disk Space: {round(disk.free / (1024**3), 2)} GB")
