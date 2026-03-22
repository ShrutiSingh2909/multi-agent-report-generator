from fpdf import FPDF
import datetime
import os


class ReportPDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(30, 90, 160)
        self.cell(0, 10, 'AI Generated Research Report', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(30, 90, 160)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} | Page {self.page_no()}', align='C')


def generate_pdf(topic: str, content: str, filename: str = "report.pdf") -> str:
    """Generate a PDF report from the given content."""
    try:
        pdf = ReportPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Topic title
        pdf.set_font('Helvetica', 'B', 18)
        pdf.set_text_color(30, 90, 160)
        pdf.multi_cell(0, 12, topic, align='C')
        pdf.ln(8)

        # Clean and write content
        pdf.set_font('Helvetica', '', 11)
        pdf.set_text_color(40, 40, 40)

        # Split content into lines and write
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                pdf.ln(3)
                continue

            # Headings
            if line.startswith('##'):
                pdf.ln(4)
                pdf.set_font('Helvetica', 'B', 13)
                pdf.set_text_color(30, 90, 160)
                pdf.multi_cell(0, 8, line.replace('##', '').strip())
                pdf.set_font('Helvetica', '', 11)
                pdf.set_text_color(40, 40, 40)

            elif line.startswith('#'):
                pdf.ln(4)
                pdf.set_font('Helvetica', 'B', 15)
                pdf.set_text_color(30, 90, 160)
                pdf.multi_cell(0, 10, line.replace('#', '').strip())
                pdf.set_font('Helvetica', '', 11)
                pdf.set_text_color(40, 40, 40)

            # Bullet points
            elif line.startswith('*') or line.startswith('-'):
                pdf.multi_cell(0, 7, '  • ' + line[1:].strip())

            # Bold text
            elif line.startswith('**') and line.endswith('**'):
                pdf.set_font('Helvetica', 'B', 11)
                pdf.multi_cell(0, 7, line.replace('**', '').strip())
                pdf.set_font('Helvetica', '', 11)

            # Normal text
            else:
                pdf.multi_cell(0, 7, line)

        pdf.output(filename)
        print(f"PDF saved to: {filename}")
        print(f"File exists: {os.path.exists(filename)}")
        print(f"File size: {os.path.getsize(filename)} bytes")

    except Exception as e:
        return f"PDF generation failed: {str(e)}"