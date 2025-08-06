from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_catalog_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("DMS Overseas LLP - Product Catalog", styles['Title']),
        Spacer(1, 12),
        Paragraph("We specialize in exporting high-quality FIBC (Flexible Intermediate Bulk Container) Bags across industries.", styles['BodyText']),
        Spacer(1, 12),
        Paragraph("Industries Served:", styles['Heading2']),
        Paragraph("- Agriculture<br/>- Chemicals<br/>- Construction<br/>- Food Processing<br/>- Pharmaceuticals", styles['BodyText']),
    ]
    doc.build(story)
