import hashlib


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def check_file():
    filepath = input("Enter file path: ")

    try:
        file_hash = calculate_hash(filepath)

        print("\n=== File Integrity Check ===")
        print(f"SHA-256: {file_hash}")

    except FileNotFoundError:
        print("File not found.")
