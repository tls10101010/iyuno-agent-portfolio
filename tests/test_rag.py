from langchain_chroma import Chroma

def test_chroma_database_exists():
    vectorstore = Chroma(
        collection_name="iyuno_knowledge",
        persist_directory="data/chroma",
    )

    documents = vectorstore.similarity_search(
        "FastAPI API 엔드포인트", k=1
    )

    assert len(documents) > 0