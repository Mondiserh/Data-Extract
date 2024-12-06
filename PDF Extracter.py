import pdfplumber
import re
import os

# Define the folder containing PDF files
folder_path = r"C:\Users\Xolani.Sithole\OneDrive - EOH\Documents\GitHub\Data-Extract\cv's"

# List all files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

# Iterate over each PDF file in the folder
for pdf_file in pdf_files:
    pdf_path = os.path.join(folder_path, pdf_file)
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        
        # # Print the extracted text (optional)
        # print(f"Processing: {pdf_file}")
        # print(text)
        
        #Candidate Name: 
        match = re.search(r'Candidate Name: (\S+)', text)  

        if match:
            inv_num = match.group(1)
            print(f"Candidate Name: {pdf_file}: {inv_num}")
        else:
            print(f"Candidate Name not found for {pdf_file}")
    
    print("-" * 50)  # Separator for readability between PDFs
