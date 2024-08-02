import os  #Bu kod sadəcə pdf-ləri oxuyub .txt fayla yazır
from PyPDF2 import PdfReader #pip install PyPDF2 


pdf_lists = "folder"  # Pdf folder name. (PDF-lər olan qovluq)

for filename in os.listdir(pdf_lists):
    if filename.endswith(".pdf"):
        pdf = os.path.join(pdf_lists, filename)
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt = os.path.join(pdf_lists, txt_filename)
        
        reader = PdfReader(pdf)
        number_of_pages = len(reader.pages)
        
        with open(txt, "w") as f:
            for x in range(number_of_pages):
                page = reader.pages[x]
                text = page.extract_text()
                f.write(text)
                f.write('\n')
        
        print(f"Finished processing {filename}")
