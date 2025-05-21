from fpdf import FPDF
import os

def generate_pdf_report(name, description, photo_paths):
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "Healthy Home Report", ln=True, align="C")
            self.ln(10)

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, f"Homeowner: {name}\n\nDamage Summary:\n{description}\n")

    for path in photo_paths:
        pdf.add_page()
        pdf.image(path, x=10, y=30, w=180)

    report_path = os.path.join(os.path.dirname(photo_paths[0]), "report.pdf")
    pdf.output(report_path)
    return report_path