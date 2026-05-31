def analyze_log():

    log_file = "/var/log/auth.log"

    keywords = [
        "failed",
        "error",
        "warning",
        "sudo"
    ]

    print("\n=== Log Analysis Report ===\n")

    try:

        matches = []

        with open(log_file, "r") as file:

            for line in file:

                line_lower = line.lower()

                for keyword in keywords:

                    if keyword in line_lower:
                        matches.append(line.strip())
                        break

        print(f"Suspicious Entries Found: {len(matches)}\n")

        for entry in matches[-10:]:
            print(entry)

    except PermissionError:
        print("Permission denied. Run with sudo.")

    except FileNotFoundError:
        print("Log file not found.")
