from langchain_chroma import Chroma


DB_DIR = "data/chroma"


def get_retriever():
    vectorstore = Chroma(
        collection_name="iyuno_knowledge",
        persist_directory=DB_DIR,
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )


def search(query):
    retriever = get_retriever()
    documents = retriever.invoke(query)

    print(f"\n질문: {query}")
    print(f"검색된 문서: {len(documents)}개\n")

    for i, document in enumerate(documents, start=1):
        print("=" * 60)
        print(f"[검색 결과 {i}]")
        print(f"출처: {document.metadata.get('source')}")
        print(document.page_content[:1000])
        print()


if __name__ == "__main__":
    search("FastAPI에서 API 엔드포인트를 어떻게 만드는가?")