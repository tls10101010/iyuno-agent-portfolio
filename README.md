# Iyuno Agentic Knowledge Triage

## 프로젝트 소개

기술 문서를 기반으로 사용자의 질문에 답변하는 간단한 RAG 기반 AI Agent 프로젝트입니다.

Iyuno AI Agent Engineer 채용 공고의 주요 기술 요구사항 중
LLM, RAG, 문서 검색을 중심으로 구현했습니다.

## 주요 기능

- 기술 문서 수집
- 문서 분할 및 벡터 DB 저장
- Chroma 기반 유사 문서 검색
- Ollama 로컬 LLM을 이용한 답변 생성
- 답변에 참고 문서 표시

## 기술 스택

- Python
- FastAPI
- LangChain
- Chroma
- Ollama
- Llama 3.2 3B

## RAG 구조

사용자 질문 → 관련 문서 검색 → LLM에 문서 전달 → 답변 생성 → 참고 문서 표시

## 실행 방법

```bash
pip install -r requirements.txt
python app/rag.py
python app/rag_chat.py