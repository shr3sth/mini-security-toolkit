import hashlib
import os


BASELINE_FILE = "data/baselines.txt"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_baseline(filepath):

    try:

        file_hash = calculate_hash(filepath)

        baselines = {}

        try:

            with open(BASELINE_FILE, "r") as baseline:

                for line in baseline:

                    saved_path, saved_hash = line.strip().split("|")

                    baselines[saved_path] = saved_hash

        except FileNotFoundError:
            pass

        baselines[filepath] = file_hash

        with open(BASELINE_FILE, "w") as baseline:

            for path, saved_hash in baselines.items():

                baseline.write(
                    f"{path}|{saved_hash}\n"
                )

        return "Baseline saved successfully."

    except FileNotFoundError:

        return "File not found."


def verify_integrity(filepath):

    try:
        current_hash = calculate_hash(filepath)

        with open(BASELINE_FILE, "r") as baseline:
            for line in baseline:
                saved_path, saved_hash = line.strip().split("|")

                if saved_path == filepath:

                    if current_hash == saved_hash:
                        return "✓ File unchanged"

                    else:
                        return "⚠ WARNING: File has been modified!"

                    return

        return "No baseline found for this file."

    except FileNotFoundError:
        return "File not found."
