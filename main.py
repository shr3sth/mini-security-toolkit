from modules.file_integrity import save_baseline, verify_integrity

print("1. Save Baseline")
print("2. Verify Integrity")

choice = input("Select option: ")

if choice == "1":
    save_baseline()

elif choice == "2":
    verify_integrity()
