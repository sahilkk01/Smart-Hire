
from pypdf import PdfReader


def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text = resume_text + text + "\n"

    return resume_text
