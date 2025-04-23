import streamlit as st
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from PyPDF2 import PdfReader
from docx import Document
import os
from language_detector import LanguageIdentifier

DetectorFactory.seed = 0

st.title("Language Detector")
st.markdown("""
            <style>
                div[class*='stRadio'] label { display: inline-flex; align-items: center; margin-right: 15px; }
            </style>
            """, unsafe_allow_html=True)

method = st.radio("Select language detection method:", ("LangDetect", "Custom Method"), horizontal=True)

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

content = ""

def custom_language_detector(text_to_detect):
    language_identifier = LanguageIdentifier(n=3, top_k=400, penalty=400)
    languages = ["en", "fr", "de", "it", "es"]
    for lang in languages:
        file_path = os.path.join('.', 'languages', f'{lang}.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            language_identifier.add_language(lang, text)
    language, _ = language_identifier.identify_language(text_to_detect)
    return language

if uploaded_file is not None:
    try:
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            content = " ".join([page.extract_text() for page in reader.pages])
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            content = " ".join([para.text for para in doc.paragraphs])
        else:
            content = ""
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")

if content:
    try:
        with st.spinner("Detecting language..."):
            if method == "LangDetect":
                language = detect(content)
            else:
                language = custom_language_detector(content)
            st.success(f"Detected Language: {language}")
    except LangDetectException:
        st.error("Could not detect the language. The text might be too short or ambiguous.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    if uploaded_file is not None:
        st.warning("No text extracted from the file.")
