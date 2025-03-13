from io import BytesIO
from pdfminer.high_level import extract_text
from resume.resume_analyzer import analyze_resume

def parse_pdf(file):
    pdf_bytes = BytesIO(file.read())
    text = extract_text(pdf_bytes)

    return analyze_resume(text)
