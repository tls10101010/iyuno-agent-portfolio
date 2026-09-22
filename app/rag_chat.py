from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM

DB_DIR = "data/chroma"

vectorstore = Chroma(
    collection_name="iyuno_knowledge",
    persist_directory=DB_DIR,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
llm = OllamaLLM(model="llama3.2:3b")

question = input("질문: ")

documents = retriever.invoke(question)

context = "\n\n".join(doc.page_content for doc in documents)

prompt = f"""
아래 기술 문서를 참고해서 질문에 답해줘.
문서에 없는 내용은 추측하지 말고 모른다고 답해줘.

[문서]
{context}

[질문]
{question}

[답변]
"""

answer = llm.invoke(prompt)

print("\n===== AI 답변 =====")
print(answer)

print("\n===== 참고 문서 =====")
for doc in documents:
    print(doc.metadata.get("source"))