import PyPDF2
import os

def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        print(f"Merging: {pdf}")
        merger.append(pdf)
    
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)
    
    print(f"\n✅ Merged PDF saved as: {output_filename}")

if __name__ == "__main__":
    print("Enter the full path to each PDF file you want to merge.")
    print("Type 'done' when you're finished.\n")
    
    pdfs_to_merge = []
    
    while True:
        file_input = input("PDF file path: ")
        if file_input.lower() == 'done':
            break
        elif os.path.isfile(file_input) and file_input.lower().endswith('.pdf'):
            pdfs_to_merge.append(file_input)
        else:
            print("❌ Invalid file. Please try again.")
    
    if len(pdfs_to_merge) >= 2:
        merge_pdfs(pdfs_to_merge, "merged_output.pdf")
    else:
        print("⚠️ Need at least two PDF files to merge.")
