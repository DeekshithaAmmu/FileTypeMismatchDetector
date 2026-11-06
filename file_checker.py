
from pathlib import Path

SIGNATURES = {
    "JPEG Image": [b"\xFF\xD8\xFF"],
    "PNG Image": [b"\x89PNG\r\n\x1a\n"],
    "PDF Document": [b"%PDF-"],
    "GIF Image": [b"GIF87a", b"GIF89a"],
    "ZIP Archive": [b"PK\x03\x04"],
    "Windows Executable": [b"MZ"],
}

EXTENSIONS = {
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".png": "PNG Image",
    ".pdf": "PDF Document",
    ".gif": "GIF Image",
    ".zip": "ZIP Archive",
    ".exe": "Windows Executable",
}


def detect_file_type(file_path):
    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    with path.open("rb") as file:
        header = file.read(16)

    actual_type = "Unknown"

    for file_type, signatures in SIGNATURES.items():
        if any(header.startswith(sig) for sig in signatures):
            actual_type = file_type
            break

    extension = path.suffix.lower()
    expected_type = EXTENSIONS.get(extension)

    print("\n--- File Type Mismatch Detector ---")
    print("File name:", path.name)
    print("Extension:", extension or "No extension")
    print("Detected type:", actual_type)

    if actual_type == "Unknown" or expected_type is None:
        print("Result: UNKNOWN")
        print("File type or extension is not supported.")

    elif actual_type == expected_type:
        print("Result: MATCH")
        print("File type matches the extension.")

    else:
        print("Result: MISMATCH")
        print("Warning: File type and extension do not match!")


if __name__ == "__main__":
    file_name = input("Enter the file path to check: ").strip().strip('"')
    detect_file_type(file_name)
