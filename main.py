from modules.port_scanner import scan_ports
from modules.system_monitor import show_system_info
from modules.file_integrity import save_baseline, verify_integrity
from modules.log_analyzer import analyze_log


def main():

    while True:

        print("\n=== Mini Security Toolkit ===\n")

        print("1. Port Scanner")
        print("2. System Resource Monitor")
        print("3. Save File Baseline")
        print("4. Verify File Integrity")
        print("5. Log Analyzer")
        print("6. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            scan_ports()

        elif choice == "2":
            show_system_info()

        elif choice == "3":
            save_baseline()

        elif choice == "4":
            verify_integrity()

        elif choice == "5":
            analyze_log()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
