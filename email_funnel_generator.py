from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_email_funnel_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("DMS Email Marketing Funnel", styles['Title']),
        Spacer(1, 12),
        Paragraph("1. Welcome Email – Introduction to DMS Overseas LLP", styles['BodyText']),
        Paragraph("2. Product Highlights – Showcase FIBC Bag Features", styles['BodyText']),
        Paragraph("3. Case Study or Testimonial – Success Story", styles['BodyText']),
        Paragraph("4. FAQ or Objection Handling – Build Trust", styles['BodyText']),
        Paragraph("5. Offer or Discount – Encourage Conversion", styles['BodyText']),
        Paragraph("6. Final Call-to-Action – Book a Call / Request a Quote", styles['BodyText']),
    ]
    doc.build(story)
