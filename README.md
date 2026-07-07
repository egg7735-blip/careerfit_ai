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

| 영역         | 기술                        |
| ---------- | ------------------------- |
| Backend    | Python, FastAPI           |
| AI API     | Gemini 2.5 Flash-Lite     |
| Data       | Pandas, SQLite, ChromaDB  |
| Frontend   | React, Vite, Tailwind CSS |
| Deployment | Docker                    |

---

# 🏗 프로젝트 아키텍처

```text
사용자
    │
    ▼
React + Vite
    │
    ▼
FastAPI (/analyze)
    │
    ├── ChromaDB (RAG 검색)
    ├── SQLite (공고 데이터 저장)
    └── Gemini API (AI 분석)
    │
    ▼
분석 결과 + 참고 공고(sources)
```

---

# 🚀 실행 방법

### Docker로 실행 (권장)

```bash

# 1. 이미지 빌드

docker build -t careerfit-ai ./backend

# 2. 컨테이너 실행

docker run -p 8000:8000 --env-file backend/.env careerfit-ai

```

API 문서: http://localhost:8000/docs

### 로컬 실행

```bash

Backend
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload

Frontend
cd frontend

npm install

npm run dev

Frontend

http://localhost:5173

Backend API

http://localhost:8000/docs

# Git

```bash

git add .
git commit -m "commit message"
git push
```

---

# 📊 데이터 파이프라인

```text
jobs.csv
    │
    ▼
Pandas 전처리
    │
    ├── SQLite 저장
    └── RAG 문서 생성
            │
            ▼
       ChromaDB 저장
            │
            ▼
사용자 질문 → 의미 기반 검색(RAG)
            │
            ▼
Gemini API
            │
            ▼
분석 결과 + Sources 반환
```

---

# ✨ 주요 기능

- RAG 기반 역량 분석: 취업 공고 데이터를 근거로 맞춤형 조언 제공

- 출처 표시: 어떤 공고 데이터를 참고했는지 sources로 함께 반환

- Mock Mode: API 한도 초과 시 MOCK_MODE=true 로 폴백 가능

---

# 📁 프로젝트 구조

```

careerfit-ai/

├── backend/ # FastAPI 서버

│ ├── main.py

│ ├── routers/

│ ├── services/

│ ├── data/

│ └── Dockerfile

├── frontend/ # React UI

└── docs/ # 하네스 파일 모음
```

---

# 📈 검증

## API 검증

* `/health` 엔드포인트를 통해 FastAPI 서버가 정상적으로 실행되는지 확인했습니다.
* `/analyze` 엔드포인트 호출 시 AI 분석 결과와 함께 `sources`가 정상적으로 반환되는지 검증했습니다.

## RAG 검증

* 다양한 질문으로 ChromaDB 검색을 수행하여 질문과 의미적으로 유사한 채용 공고가 검색되는지 확인했습니다.
* 검색된 공고를 근거로 Gemini가 답변을 생성하는지 검증했습니다.

## UI 검증

* React UI에서 입력 폼, 분석 결과 카드, 출처 카드가 정상적으로 출력되는지 확인했습니다.
* FastAPI와 React 간 API 연동이 정상적으로 동작하는지 확인했습니다.

## Docker 검증

* Docker Image가 정상적으로 빌드되는지 확인했습니다.
* Docker Container 실행 후 `/health` 엔드포인트가 정상적으로 응답하는지 확인했습니다.

---

# 📂 데이터

CareerFit AI는 실제 채용 공고 데이터를 기반으로 사용자의 전공, 보유 기술, 관심 직무를 분석합니다.

수집한 채용 공고 데이터는 Pandas를 활용하여 결측치와 중복 데이터를 전처리한 후 SQLite에 구조화하여 저장했습니다. 또한 동일한 데이터를 ChromaDB에 임베딩하여 의미 기반(RAG) 검색에 활용하고, 검색된 공고를 근거로 AI가 맞춤형 분석 결과를 생성하도록 구현했습니다.


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

# 📸 Demo

- Frontend: https://careerfit-ai-frontend-aujm.onrender.com

- Backend API: https://careerfit-ai-q80r.onrender.com

---

# 👨‍💻 개발자

- Name: 신혁진

- Role: Backend / AI Service Development

- GitHub: @egg7735-blip

- Email: egg7735@gmail.com
