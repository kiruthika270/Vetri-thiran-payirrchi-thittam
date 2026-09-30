import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered"
)

# Title
st.markdown(
    "<h1 style='text-align: center;'>⚖️ LegalEase</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>AI Legal Document Generator</h3>",
    unsafe_allow_html=True
)

st.write("---")

# Document Type
document_type = st.text_input(
    "Document Type",
    placeholder="Example: Rental Agreement"
)

# Parties Involved
parties = st.text_area(
    "Parties Involved",
    placeholder="Example: Party A: Name; Party B: Name"
)

# Terms and Conditions
terms = st.text_area(
    "Terms & Conditions",
    placeholder="Write conditions separated by semicolons (;)"
)

# Effective Date
date = st.text_input(
    "Effective Date",
    placeholder="Example: 28-09-2026"
)

st.write("")

# Generate Document
if st.button("Generate Document", use_container_width=True):

    # Check whether all fields are filled
    if not document_type or not parties or not terms or not date:
        st.warning("Please fill in all the fields.")

    else:
        st.success("Document generated successfully!")

        # Display document details
        st.markdown("## Document Details")

        st.write("*Document Type:*", document_type)
        st.write("*Parties Involved:*", parties)
        st.write("*Effective Date:*", date)

        # Terms and Conditions
        st.markdown("### Terms & Conditions")

        term_list = terms.split(";")

        for term in term_list:
            term = term.strip()

            if term:
                st.write("•", term)

        # Create downloadable document
        document_text = f"""
LEGALEASE
LEGAL DOCUMENT
==============================

Document Type:
{document_type}

Parties Involved:
{parties}

Effective Date:
{date}

Terms & Conditions:
"""

        for term in term_list:
            term = term.strip()

            if term:
                document_text += f"\n• {term}"

        # Download button
        st.write("")
        st.download_button(
            label="📥 Download Document",
            data=document_text,
            file_name="LegalEase_Document.txt",
            mime="text/plain",
            use_container_width=True
        )