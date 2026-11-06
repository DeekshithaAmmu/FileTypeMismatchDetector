\# File Type Mismatch Detector



\## Project Overview

The File Type Mismatch Detector is a cybersecurity project that identifies whether a file's actual type matches its file extension.



It uses file signatures (magic bytes) to identify the actual file format and compares it with the extension.



\## Objectives

\- Identify the actual type of a file.

\- Detect mismatches between file content and extension.

\- Display MATCH, MISMATCH, or UNKNOWN results.

\- Provide a simple web interface for file checking.



\## Technologies Used

\- Python

\- Flask

\- HTML

\- GitHub

\- Render



\## Supported File Formats

\- JPEG

\- PNG

\- PDF

\- GIF

\- ZIP

\- Windows Executable (EXE)



\## Project Files

\- `app.py` – Flask web application.

\- `file\_checker.py` – Python file detection program.

\- `requirements.txt` – Required Python packages.

\- `Procfile` – Application start command.

\- Screenshots – Project test results.



\## How It Works

1\. The user uploads a file.

2\. The application reads the file signature.

3\. It identifies the actual file type.

4\. It compares the detected type with the filename extension.

5\. It displays MATCH, MISMATCH, or UNKNOWN.



\## Test Results

\- `image\_2.jpg` – MATCH

\- `test\_image.pdf` – MISMATCH



\## Safety Note

A file type mismatch is a warning that requires further investigation. It does not automatically mean that a file is malicious.



\## Conclusion

This project demonstrates a simple method of identifying file type mismatches using Python and Flask. It helps users recognize files whose extensions do not match their actual content.

