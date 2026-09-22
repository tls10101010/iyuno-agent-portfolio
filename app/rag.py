from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_DIR = Path("data/raw")
DB_DIR = "data/chroma"


def load_documents():
    documents = []

    for file_path in DATA_DIR.glob("*.txt"):
        loader = TextLoader(str(file_path), encoding="utf-8")
        documents.extend(loader.load())

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
    )

    return splitter.split_documents(documents)


def build_vector_database(chunks):
    vectorstore = Chroma(
        collection_name="iyuno_knowledge",
        persist_directory=DB_DIR,
    )

    vectorstore.add_documents(chunks)

    return vectorstore


if __name__ == "__main__":
    documents = load_documents()

    print(f"불러온 문서 수: {len(documents)}")

    chunks = split_documents(documents)

    print(f"생성된 청크 수: {len(chunks)}")

    print("벡터DB 저장 시작...")

    vectorstore = build_vector_database(chunks)

    print("벡터DB 저장 완료!")