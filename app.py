# Manage imports
import streamlit as st
from ocr_utils import load_ocr_model, perform_ocr
import re

# Web app interface
st.set_page_config(page_title="English - Hindi OCR Tool", page_icon="🖼️")
st.title("English - Hindi OCR Tool")
st.write("This tool allows you to perform Optical Character Recognition (OCR) on images containing English and Hindi text, and search for specific keywords.")

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        text-align: center;
    }
    .stTextInput, .stButton {
        margin: 10px 0;
        width: 100%;
    }
    .stButton {
        width: 28%;
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# File uploader for image
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    try:
        # Load the OCR model
        processor, model = load_ocr_model()

        # Perform OCR on the uploaded image
        with st.spinner('Processing...'):
            extracted_text, boxes = perform_ocr(uploaded_image, processor, model)

        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        st.subheader("Extracted Text:")
        st.write(extracted_text)

        keyword = st.text_input("Enter keyword to search:", key="keyword_input")
        search_button = st.button("Search")

        if search_button or (keyword and st.session_state.keyword_input):
            # Match word irrespective of case 
            pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)

            # Highlight the keyword in the extracted text
            if pattern.search(extracted_text):
                def highlight_match(match):
                    return f"<mark style='background-color: yellow;'>{match.group(0)}</mark>"

                highlighted_text = pattern.sub(highlight_match, extracted_text)
                st.markdown(highlighted_text, unsafe_allow_html=True)
                st.success(f"Keyword '{keyword}' found!")
            else:
                st.error(f"Keyword '{keyword}' not found.")

    except Exception as e:
        st.error(f"Error: {e}")