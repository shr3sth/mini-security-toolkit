def analyze_log():

    log_file = "/var/log/auth.log"

    keywords = {
        "failed": 0,
        "error": 0,
        "warning": 0,
        "sudo": 0
    }

    matches = []

    try:

        with open(log_file, "r") as file:

            for line in file:

                line_lower = line.lower()

                for keyword in keywords:

                    if keyword in line_lower:
                        keywords[keyword] += 1
                        matches.append(line.strip())
                        break

        print("\n=== Security Report ===\n")

        print(f"Failed Events : {keywords['failed']}")
        print(f"Error Events  : {keywords['error']}")
        print(f"Warning Events: {keywords['warning']}")
        print(f"Sudo Events   : {keywords['sudo']}")

        print("\n=== Recent Events ===\n")

        for entry in matches[-10:]:
            print(entry)

    except PermissionError:
        print("Permission denied. Run with sudo.")

    except FileNotFoundError:
        print("Log file not found.")
