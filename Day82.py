import PyPDF2

def merge_pdfs(pdf_list, output_path):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()
    
    # Iterate through the list of PDF files
    for pdf in pdf_list:
        with open(pdf, 'rb') as file:
            # Append each PDF file to the merger
            pdf_merger.append(file)
    
    # Write the combined PDF to the output file
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)
    
    print(f"PDFs merged successfully into {output_path}")

# Example usage:
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # List of PDF files to merge
output_file = 'merged_output.pdf'  # Output file name

merge_pdfs(pdf_files, output_file)
