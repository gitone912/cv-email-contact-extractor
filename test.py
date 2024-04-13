# import docx2txt

# doc_text = docx2txt.process('/Users/pranaymishra/Desktop/ast_ishla/ost_placement/Sample2/AkashGoel.docx')
# print(doc_text)
import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

pdf_text = extract_text_from_pdf('/Users/pranaymishra/Desktop/ast_ishla/ost_placement/Sample2/AarushiRohatgi.pdf')
print(pdf_text)
