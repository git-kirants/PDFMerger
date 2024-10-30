# PDF Merger Tool

This project is a simple Python-based application that merges multiple PDF files from a selected directory into a single PDF file. It uses `PyPDF2` for handling PDF files and `tkinter` for the GUI to select directories and files.

## Features

- Merge all PDF files from a selected directory into a single PDF.
- GUI interface for selecting the directory and saving the merged PDF file.
- Handles errors if no PDF files are found in the specified directory.

## Requirements

- **Python 3.7+**
- **PyPDF2** for merging PDF files.
- **Tkinter** for the GUI.

## Installation

1. Clone this repository or download the files.
2. Install the required packages:

    ```bash
    pip install PyPDF2
    ```

## Usage

1. Run the `pdfnerger` script:

    ```bash
    python pdfmerger.py
    ```

2. A file dialog will open for you to select a directory containing the PDF files to merge.
3. Another dialog will open to specify the output file location for the merged PDF.
4. Upon success, a message box will notify you that the PDFs were merged successfully.

## Code Overview

- **`merge_pdfs(directory_path, output_path)`**: This function iterates through all PDF files in the specified directory, merges them, and saves the final PDF at the specified output path.
- **`select_directory()`**: Opens a dialog to select the directory containing the PDFs.
- **`select_output_file()`**: Opens a save dialog to specify the output PDF file location.
- **`main()`**: The main function to initialize the Tkinter application, handle directory/file selection, and call the merge function.

## Error Handling

- If no PDFs are found in the selected directory, a `ValueError` will trigger an error message.
- Any other exceptions will display an error message with details.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
