import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            extracted_text = page.extract_text() or ""
            text += extracted_text + "\n"
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
	)
    chunks = text_splitter.split_text(raw_text)
    return chunks

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your PDF")

    with st.sidebar:
        st.subheader("Uploaded documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here, then click on Process",
            accept_multiple_files=True
        )
        
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)

            # Display the extracted text after spinner completes
            # st.write("### Extracted Text from PDFs:")
            # st.write(raw_text)

            # Get text chunks
            text_chunks = get_text_chunks(raw_text)
            st.write(text_chunks)
			# Create vector store

if __name__ == "__main__":
    main()
