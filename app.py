import streamlit as st
from catalog_generator import generate_catalog_pdf
from email_funnel_generator import generate_email_funnel_pdf

st.title("📄 DMS PDF Generator")
st.write("Generate your product catalog and email funnel in one click.")

if st.button("Generate Product Catalog PDF"):
    generate_catalog_pdf("DMS_FIBC_Product_Catalog.pdf")
    st.success("✅ Product Catalog PDF generated!")

if st.button("Generate Email Funnel PDF"):
    generate_email_funnel_pdf("DMS_Email_Funnel.pdf")
    st.success("✅ Email Funnel PDF generated!")
