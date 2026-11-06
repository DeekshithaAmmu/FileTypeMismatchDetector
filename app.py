from flask import Flask, render_template_string, request
from pathlib import Path

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>File Type Mismatch Detector</title>
</head>
<body>
    <h1>File Type Mismatch Detector</h1>
    <p>Upload a file to check its actual type.</p>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Check File</button>
    </form>

    {% if result %}
        <h2>{{ result }}</h2>
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    message = ""

    if request.method == "POST":
        uploaded_file = request.files["file"]
        header = uploaded_file.read(16)
        extension = Path(uploaded_file.filename).suffix.lower()

        signatures = {
            "JPEG Image": [b"\xff\xd8\xff"],
            "PNG Image": [b"\x89PNG\r\n\x1a\n"],
            "PDF Document": [b"%PDF-"],
            "GIF Image": [b"GIF87a", b"GIF89a"],
            "ZIP Archive": [b"PK\x03\x04"],
            "Windows Executable": [b"MZ"]
        }

        extensions = {
            ".jpg": "JPEG Image",
            ".jpeg": "JPEG Image",
            ".png": "PNG Image",
            ".pdf": "PDF Document",
            ".gif": "GIF Image",
            ".zip": "ZIP Archive",
            ".exe": "Windows Executable"
        }

        actual_type = "Unknown"

        for file_type, sigs in signatures.items():
            if any(header.startswith(sig) for sig in sigs):
                actual_type = file_type
                break

        expected_type = extensions.get(extension)

        if actual_type == "Unknown" or expected_type is None:
            result = "UNKNOWN"
            message = "File type or extension is not supported."
        elif actual_type == expected_type:
            result = "MATCH"
            message = "File type matches the extension."
        else:
            result = "MISMATCH"
            message = "Warning: File type and extension do not match!"

    return render_template_string(
        HTML, result=result, message=message
    )

if __name__ == "__main__":
    app.run(debug=True)