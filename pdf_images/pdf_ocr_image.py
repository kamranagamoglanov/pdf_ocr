import os  #Bu kod pdf-ləri oxuyub ayrı-ayrı qovluqlarda şəkil və .txt fayl olaraq yerləşdirir
import fitz  # pip install pymupdf 

pdf_lists = "folders"  # Pdf folder name. (PDF-lər olan qovluq)

for filename in os.listdir(pdf_lists):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_lists, filename)
        pdf_name = os.path.splitext(filename)[0]
        output_folder = os.path.join(pdf_lists, pdf_name)
        
        os.makedirs(output_folder, exist_ok=True)

        txt_filename = os.path.join(output_folder, pdf_name + ".txt")


        doc = fitz.open(pdf_path)
        number_of_pages = doc.page_count

        with open(txt_filename, "w") as f:
            for x in range(number_of_pages):
                page = doc.load_page(x)
                text = page.get_text()
                f.write(text)
                f.write('\n')

                image_list = page.get_images(full=True)
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_filename = os.path.join(output_folder, f"page_{x+1}_img_{img_index}.png")
                    with open(image_filename, "wb") as img_file:
                        img_file.write(image_bytes)

        print(f"Finished processing {filename}")
