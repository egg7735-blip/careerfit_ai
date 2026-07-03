# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

---

# 📌 프로젝트 개요

취업을 준비하면서 **어떤 역량을 먼저 준비해야 하는지**, **내 전공과 관심 직무에 맞는 기술이 무엇인지** 파악하기 어려운 문제를 해결하기 위해 **CareerFit AI**를 개발했습니다.

저는 **기계정보공학과 학생**으로, 이번 프로젝트를 통해 **데이터 분석 능력과 생성형 AI 활용 능력**을 향상시키는 것을 목표로 했습니다.

관심 있는 직무는 다음과 같습니다.

* 데이터 분석
* 기계설계
* 설비 및 생산기술
* Python, C 기반 개발 및 자동화

CareerFit AI는 실제 취업 공고 데이터를 기반으로 사용자의 전공, 보유 기술, 관심 직무를 분석하고, 부족한 역량과 준비 방향을 AI가 제안하는 **RAG(Retrieval-Augmented Generation) 기반 취업·공모전 포트폴리오 코치**입니다.

---

# 🛠 기술 스택

| 영역         | 기술                       |
| ---------- | ------------------------ |
| Backend    | Python, FastAPI          |
| AI API     | Gemini 2.5 Flash-Lite    |
| Data       | Pandas, SQLite, ChromaDB |
| Frontend   | React, Vite              |
| Deployment | Docker                   |

---

# 🎯 프로젝트 목표

* 데이터 분석 및 AI 활용 역량 향상
* 실제 채용 공고 데이터를 활용한 데이터 전처리 경험
* Pandas, SQLite, ChromaDB를 활용한 데이터 파이프라인 구축
* RAG(Retrieval-Augmented Generation) 기반 AI 서비스 구현
* FastAPI와 React를 활용한 웹 서비스 개발
* GitHub 포트폴리오로 활용 가능한 프로젝트 완성

---

# ✨ 주요 기능

* 실제 취업 공고 데이터 조회
* 사용자 전공 및 보유 기술 입력
* 관심 직무 기반 맞춤형 분석
* ChromaDB를 활용한 의미 기반(RAG) 공고 검색
* Gemini API를 활용한 AI 역량 분석
* 부족한 기술 및 학습 방향 추천
* 추천 근거(Sources) 제공

---

# 💡 기대 효과

* 데이터 분석 직무에 필요한 핵심 기술을 확인할 수 있습니다.
* 부족한 역량을 데이터 기반으로 분석할 수 있습니다.
* 실제 채용 공고를 활용하여 취업 준비 방향을 설정할 수 있습니다.
* 생성형 AI와 RAG 기술을 활용한 프로젝트 경험을 포트폴리오로 활용할 수 있습니다.

---

# 🔮 향후 개선 계획

* 실제 채용 사이트 데이터 연동
* 이력서 PDF 자동 분석
* 공모전 추천 기능 추가
* 제조·기계설계 분야 데이터 확대
* 개인 맞춤형 학습 로드맵 제공
* 관심 기업 기반 채용 추천 기능

---

# 📅 진행 현황

## ✅ 1일차 - 프로젝트 기획 및 개발 환경 구축

* 프로젝트 기획
* GitHub Repository 생성
* Python 개발 환경 구축
* 프로젝트 구조 설계

---

## ✅ 2일차 - FastAPI 서버 및 Gemini API 연동

* FastAPI 기반 REST API 구현

  * `/health`
  * `/jobs`
  * `/analyze`
* Gemini 2.5 Flash-Lite API 연동
* Mock Mode 환경 구축
* FastAPI 서버 실행 및 API 테스트 완료

---

## ✅ 3일차 - 데이터 파이프라인 구축

* CSV 데이터 전처리
* Pandas 활용
* SQLite 저장
* ChromaDB 구축
* RAG 데이터 생성

---

## ⏳ 4일차 - RAG 서비스 및 React UI

예정

* ChromaDB 검색
* Gemini와 RAG 연동
* React UI 구현
* 분석 결과 화면 구현

---

## ⏳ 5일차 - Docker 및 포트폴리오 완성

예정

* Docker 환경 구축
* README 최종 정리
* GitHub 포트폴리오 완성
* 프로젝트 발표

---

# 📚 개발 메모

## Python 가상환경

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Git 명령어

```bash
git add .
git commit -m "commit message"
git push
```

## 용어정리
 *쿼리(Query)
    데이터베이스(SQLite)에 원하는 데이터를 조회, 추가, 수정, 삭제하도록 요청하는 명령어입니다.

---

## 프로젝트 핵심 개념

| 개념              | 설명                                   |
| --------------- | ------------------------------------ |
| SQLite          | 구조화된 데이터를 저장하는 데이터베이스                |
| ChromaDB        | 의미 기반 검색을 위한 벡터 데이터베이스               |
| 벡터(Vector)      | 데이터를 숫자 좌표로 표현한 값                    |
| 임베딩(Embedding)  | 의미가 비슷한 데이터를 가까운 벡터 공간에 표현하는 기술      |
| 메타데이터(Metadata) | 데이터의 추가 정보를 저장하는 속성(예: 회사명, 직무, 마감일) |
| RAG             | 검색된 데이터를 근거로 AI가 답변을 생성하는 방식         |

---

# 👨‍💻 개발자

**기계정보공학과**

### 관심 분야

* 데이터 분석
* 기계설계
* 설비 및 생산기술
* Python 자동화
* 생성형 AI 활용 서비스 개발

### 프로젝트 목표

이번 프로젝트를 통해 실제 취업 공고 데이터를 분석하고 RAG 기반 AI 서비스를 구현하며, 데이터 분석 및 생성형 AI 활용 역량을 향상시키는 것을 목표로 했습니다.
