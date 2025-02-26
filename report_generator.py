from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

def generate_pdf_report(log_file="logs.csv", output="weekly_report.pdf"):
    df = pd.read_csv(log_file)
    c = canvas.Canvas(output, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Weekly File Integrity Report")

    y = 720
    for _, row in df.iterrows():
        c.drawString(50, y, f"{row['timestamp']} - {row['file_path']} - {row['change_type']}")
        y -= 20
    c.save()
