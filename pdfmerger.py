import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog, messagebox

def merge_pdfs(directory_path, output_path):
    """
    Merge all PDF files in the specified directory into a single PDF file.
    
    Args:
        directory_path (str): Path to the directory containing PDF files
        output_path (str): Path where the merged PDF will be saved
    """
    # Create a PDF merger object
    merger = PdfMerger()
    
    # Track if we found any PDF files
    pdf_found = False
    
    try:
        # Iterate through all files in the directory
        for filename in sorted(os.listdir(directory_path)):
            if filename.lower().endswith('.pdf'):
                pdf_found = True
                filepath = os.path.join(directory_path, filename)
                merger.append(filepath)
        
        # If no PDFs were found, raise an exception
        if not pdf_found:
            raise ValueError("No PDF files found in the specified directory.")
        
        # Write the merged PDF to the output file
        merger.write(output_path)
        merger.close()
        return True
        
    except Exception as e:
        merger.close()
        raise e

def select_directory():
    """Open a directory selection dialog and return the selected path."""
    directory = filedialog.askdirectory(title="Select Directory Containing PDFs")
    return directory if directory else None

def select_output_file():
    """Open a file save dialog and return the selected path."""
    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Merged PDF As"
    )
    return output_file if output_file else None

def main():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    try:
        # Get the input directory
        directory_path = select_directory()
        if not directory_path:
            return
        
        # Get the output file path
        output_path = select_output_file()
        if not output_path:
            return
        
        # Merge the PDFs
        merge_pdfs(directory_path, output_path)
        
        messagebox.showinfo("Success", "PDFs merged successfully!")
        
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()