import streamlit as st
from summarizer import summarize_text
from PyPDF2 import PdfReader
from rake_nltk import Rake

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Text Summarization Tool")

# ------------------------
# PDF Upload
# ------------------------

uploaded_file = st.file_uploader(
    "Upload a PDF File (Optional)",
    type=["pdf"]
)

pdf_text = ""

if uploaded_file is not None:

    pdf_reader = PdfReader(uploaded_file)

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            pdf_text += page_text + "\n"

# ------------------------
# Text Input
# ------------------------

text = st.text_area(
    "Enter Text or Upload PDF",
    value=pdf_text,
    height=300
)

# ------------------------
# Summary Length Selector
# ------------------------

num_sentences = st.slider(
    "Select Number of Summary Sentences",
    min_value=1,
    max_value=10,
    value=3
)

# ------------------------
# Generate Summary
# ------------------------

if st.button("Generate Summary"):

    if text.strip():

        with st.spinner(
            "Generating Summary..."
        ):

            summary = summarize_text(
                text,
                num_sentences
            )

        st.subheader("Summary")

        st.write(summary)

        # ------------------------
        # Statistics
        # ------------------------

        original_words = len(
            text.split()
        )

        summary_words = len(
            summary.split()
        )

        reduction = (
            (original_words - summary_words)
            / original_words
        ) * 100

        st.subheader("Statistics")

        st.write(
            f"Original Words: {original_words}"
        )

        st.write(
            f"Summary Words: {summary_words}"
        )

        st.write(
            f"Reduction: {reduction:.2f}%"
        )

        # ------------------------
        # Keywords
        # ------------------------

        st.subheader("Keywords")

        rake = Rake()

        rake.extract_keywords_from_text(
            text
        )

        keywords = rake.get_ranked_phrases()[:10]

        for keyword in keywords:

            st.write(
                f"• {keyword}"
            )

        # ------------------------
        # Download Button
        # ------------------------

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

    else:

        st.warning(
            "Please enter text or upload a PDF."
        )