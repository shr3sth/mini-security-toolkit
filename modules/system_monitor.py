import psutil


def get_system_info():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    info = (
        f"=== System Resource Monitor ===\n\n"
        f"CPU Usage: {cpu}%\n"
        f"Memory Usage: {memory.percent}%\n"
        f"Available Memory: {round(memory.available / (1024**3), 2)} GB\n\n"
        f"Disk Usage: {disk.percent}%\n"
        f"Free Disk Space: {round(disk.free / (1024**3), 2)} GB"
    )

    return info
