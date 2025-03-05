from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
import shutil

DATA_PATH="data/books"
CHROMA_PATH="chroma"

def main():
    generate_data_store()

def generate_data_store():
    docs = load_documents()
    chunks = split_text(docs)
    save_to_chroma(chunks)
    
def load_documents():
    print(f"Looking for documents in: {DATA_PATH}")
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Directory not found: {DATA_PATH}")
    loader=DirectoryLoader(DATA_PATH,glob="*.md")
    documents=loader.load()
    return documents

def split_text(documents: list[Document]):    
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks=text_splitter.split_documents(documents)
    print(f"Splitted Document No: {len(documents)} into {len(chunks)} Chunks")
    document=chunks[23]
    print("Page Content:: "+str(document.page_content))
    print()
    print("Metadata::"+str(document.metadata))
    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    db=Chroma.from_documents(
    chunks,OpenAIEmbeddings(),persist_directory=CHROMA_PATH
    )
    print(f"Saved {len(chunks)} Chunks to {CHROMA_PATH}")

if __name__ == "__main__":
        main()
