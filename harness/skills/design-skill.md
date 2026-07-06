# design-skill.md

## 1. 디자인 목표

CareerFit AI는 대학생을 위한 취업·공모전 포트폴리오 코치입니다.
전문적인 신뢰감과 친근한 사용성을 함께 제공합니다.

요리 비유로 하면, UI는 손님이 처음 마주하는 식당의 메뉴판입니다.
너무 딱딱하면 부담스럽고, 너무 가벼우면 신뢰가 떨어지므로 균형이 중요합니다.

---

## 2. 컬러 팔레트

| 역할         | Tailwind 예시   | 사용 위치         |
| ---------- | ------------- | ------------- |
| Primary    | `blue-600`    | 주요 버튼, 강조 텍스트 |
| Secondary  | `emerald-500` | 긍정 결과, 추천 태그  |
| Background | `slate-50`    | 전체 배경         |
| Text       | `slate-900`   | 기본 본문 텍스트     |
| Border     | `slate-200`   | 카드, 입력창 테두리   |
| Error      | `red-500`     | 오류 메시지, 실패 상태 |

사용 예시:

```jsx
className="bg-blue-600 text-white"
className="border border-slate-200"
className="text-red-500"
```

---

## 3. 타이포그래피 규칙

* 전체 폰트는 기본 sans-serif 계열을 사용한다.
* 페이지 제목은 `text-3xl font-bold`를 사용한다.
* 섹션 제목은 `text-xl font-semibold`를 사용한다.
* 본문은 `text-base text-slate-700`을 사용한다.
* 보조 설명은 `text-sm text-slate-500`을 사용한다.
* 버튼 텍스트는 `font-medium` 이상으로 설정한다.

---

## 4. 컴포넌트 구조

```text
src/
├── App.jsx
└── components/
    ├── InputForm.jsx
    ├── ResultCard.jsx
    └── SourceCard.jsx
```

### App

역할:

* 전체 페이지 레이아웃 관리
* 사용자 입력 상태 관리
* FastAPI `/analyze` 요청 처리
* 결과 데이터를 `ResultCard`, `SourceCard`에 전달

### InputForm

역할:

* 전공, 보유 스킬, 관심 직무 입력
* 제출 버튼 제공
* 입력값이 비어 있을 때 기본 안내 제공

UI 규칙:

* 입력창은 `rounded-lg border border-slate-200`
* 버튼은 `bg-blue-600 hover:bg-blue-700`
* 입력 영역은 카드 형태로 구성

### ResultCard

역할:

* AI 분석 결과 표시
* 일치 역량, 부족 역량, 추천 프로젝트 표시
* confidence 값이 낮을 경우 주의 문구 표시

UI 규칙:

* 카드 배경은 `bg-white`
* 그림자는 `shadow-sm`
* 중요한 결과는 `text-blue-600 font-semibold`

### SourceCard

역할:

* RAG가 참고한 공고 출처 표시
* 회사명, 공고명, 추천 이유 표시

UI 규칙:

* 출처 카드는 작고 명확하게 표시
* `border-l-4 border-emerald-500`로 근거 데이터 느낌을 준다
* sources가 없으면 “참고한 공고가 없습니다”를 표시한다

---

## 5. 레이아웃 규칙

* 전체 화면 배경은 `bg-slate-50`
* 콘텐츠 최대 너비는 `max-w-4xl`
* 가운데 정렬은 `mx-auto`
* 페이지 여백은 `px-4 py-8`
* 카드 간 간격은 `space-y-6`
* 모바일에서도 깨지지 않도록 세로 배치를 기본으로 한다.
* 데스크톱에서는 결과 영역을 넓게 보여준다.

기본 레이아웃 예시:

```jsx
<div className="min-h-screen bg-slate-50">
  <main className="max-w-4xl mx-auto px-4 py-8 space-y-6">
    ...
  </main>
</div>
```

---

## 6. 금지 사항

* API Key를 React 코드에 절대 넣지 않는다.
* 너무 많은 색상을 동시에 사용하지 않는다.
* 모든 텍스트를 가운데 정렬하지 않는다.
* 버튼 색상을 페이지마다 다르게 사용하지 않는다.
* RAG 출처 없이 확정적인 추천처럼 보이게 만들지 않는다.
* 오류 메시지를 숨기지 않는다.
* `any`, `data`, `result` 같은 의미 없는 표시명만 화면에 노출하지 않는다.
* 모바일 화면에서 입력창이 잘리는 레이아웃을 만들지 않는다.

---

## 7. 디자인 원칙 요약

CareerFit AI의 UI는 다음 기준을 따른다.

1. 대학생이 부담 없이 사용할 수 있어야 한다.
2. 취업·공모전 서비스답게 신뢰감을 줘야 한다.
3. AI 답변보다 근거 sources가 함께 보이도록 해야 한다.
4. 입력 → 분석 → 결과 → 출처 흐름이 한눈에 보여야 한다.

# harness/skills/design-skill.md — CareerFit AI UI 디자인 규칙


## 컬러 팔레트

- primary: #3B82F6 (파란색 — 신뢰, 전문성)

- secondary: #10B981 (초록색 — 성장, 추천)

- background: #F8FAFC (연한 회색)

- text-primary: #1E293B

- text-muted: #64748B

- border: #E2E8F0

- error: #EF4444



## 타이포그래피

- 제목: text-2xl font-bold text-slate-800

- 소제목: text-lg font-semibold text-slate-700

- 본문: text-base text-slate-600

- 설명: text-sm text-slate-500



## 컴포넌트 구조

- App.jsx: 최상위, 상태 관리, API 요청

- InputForm.jsx: 전공·스킬·직무 입력 폼

- ResultCard.jsx: AI 분석 답변 출력 (초록 왼쪽 테두리)

- SourceCard.jsx: 출처 공고 목록 출력



## 레이아웃 규칙

- 최대 너비: max-w-2xl mx-auto

- 카드 내부 여백: p-6

- 컴포넌트 간격: gap-4 / space-y-4

- 모서리: rounded-xl (카드), rounded-lg (버튼)



## 금지 사항

- API Key를 화면에 표시하거나 localStorage에 저장

- 다크 배경에 흰 텍스트 (가독성 우선)

- 아이콘 없이 버튼만 사용 (텍스트 레이블 필수)