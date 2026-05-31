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

        report = "\n=== Security Report ===\n\n"

        report += f"Failed Events : {keywords['failed']}\n"
        report += f"Error Events  : {keywords['error']}\n"
        report += f"Warning Events: {keywords['warning']}\n"
        report += f"Sudo Events   : {keywords['sudo']}\n"

        report += "\n=== Recent Events ===\n\n"

        for entry in matches[-10:]:
            report += entry + "\n"

        return report

    except PermissionError:
        return "Permission denied. Run with sudo."

    except FileNotFoundError:
        return "Log file not found."
