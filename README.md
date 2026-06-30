# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치



## 프로젝트 개요



[어떤 것을 준비해야 할 지 모르겠다.]



## 기술 스택



| 영역 | 기술 |

|---|---|

| 백엔드 | Python, FastAPI |

| AI API | Gemini 2.5 Flash-Lite |

| 데이터 | Pandas, SQLite, ChromaDB |

| 프론트엔드 | React, Vite |

| 실행 환경 | Docker |

## 진행 현황



- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅

- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결
    * FastAPI 기반 `/health`, `/jobs`, `/analyze` API 엔드포인트를 구현하여 기본 백엔드 구조를 구축했습니다.
    * Python 개발 환경 및 프로젝트 실행 환경을 설정하고 서버 구동을 완료했습니다.
    * Gemini 2.5 Flash-Lite API를 연동하여 AI 응답 기능을 사용할 수 있는 기반을 마련했습니다.
    * 개발 및 테스트를 위한 `mock mode` 환경변수를 설정하여 목업 데이터 기반 실행 환경을 구성했습니다.
    * API 테스트 및 기본 동작을 확인하여 다음 단계(RAG 및 실제 AI 분석 기능 구현)를 위한 기반을 완성했습니다.

- [ ] 3일차: 데이터 파이프라인 구축

- [ ] 4일차: RAG 기반 서비스 + React UI

- [ ] 5일차: Docker + 포트폴리오 완성

## 메모



- venv 활성화
    venv\Scripts\activate.ps1

- 원격 저장소 연결 및 push
    git branch -M main
    git push -u origin main
