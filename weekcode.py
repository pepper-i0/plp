from PyPDF2 import PdfReader

# Path to the PDF file
pdf_path = 'Abdul-gaffar-O CV nn .pdf'

try:
    # Create a PDF reader object
    reader = PdfReader(pdf_path)
    
    # Extract text from all pages
    data = ""
    for page in reader.pages:
        data += page.extract_text()

    # Print the extracted text
    print(data)

except FileNotFoundError:
    print(f"Error: The file '{pdf_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")