import hashlib
import os


BASELINE_FILE = "data/baselines.txt"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_baseline():
    filepath = input("Enter file path: ")

    try:
        file_hash = calculate_hash(filepath)

        with open(BASELINE_FILE, "a") as baseline:
            baseline.write(f"{filepath}|{file_hash}\n")

        print("\nBaseline saved successfully.")

    except FileNotFoundError:
        print("File not found.")


def verify_integrity():
    filepath = input("Enter file path: ")

    try:
        current_hash = calculate_hash(filepath)

        with open(BASELINE_FILE, "r") as baseline:
            for line in baseline:
                saved_path, saved_hash = line.strip().split("|")

                if saved_path == filepath:

                    if current_hash == saved_hash:
                        print("\n✓ File unchanged")

                    else:
                        print("\n⚠ WARNING: File has been modified!")

                    return

        print("No baseline found for this file.")

    except FileNotFoundError:
        print("File not found.")
