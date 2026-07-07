# Render Frontend Deploy Guide

이 문서는 React/Vite 프론트엔드를 FastAPI 백엔드와 연결하고, 로컬과 Render Docker Web Service에서 실행하는 방법을 정리합니다.

## 1. 로컬 실행 방법

백엔드를 먼저 실행합니다.

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

프론트엔드를 실행합니다.

```bash
cd frontend
npm install
npm run dev
```

브라우저에서 `http://localhost:5173`에 접속합니다. 백엔드 상태는 `http://localhost:8000/health`에서 확인할 수 있습니다.

## 2. 프론트엔드 환경변수 설정

프론트엔드는 `VITE_API_BASE_URL`로 백엔드 주소를 읽습니다. 로컬에서는 값을 생략해도 기본값 `http://localhost:8000`을 사용합니다.

필요하면 `frontend/.env`를 만들고 아래처럼 입력합니다. 이 파일은 Git에 올리지 않습니다.

```env
VITE_API_BASE_URL=http://localhost:8000
```

Render에서는 FastAPI 백엔드의 공개 URL을 넣습니다.

```env
VITE_API_BASE_URL=https://careerfit-ai-q80r.onrender.com
```

## 3. 백엔드 CORS 환경변수 설정

백엔드는 `FRONTEND_ORIGINS`로 허용할 프론트엔드 origin을 쉼표로 받습니다.

로컬 기본 허용값은 다음과 같습니다.

```text
http://localhost:5173
http://127.0.0.1:5173
http://localhost:3000
http://127.0.0.1:3000
```

Render 백엔드에는 로컬 주소와 Render 프론트엔드 주소를 함께 넣습니다.

```env
FRONTEND_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,https://your-frontend-service.onrender.com
GEMINI_API_KEY=your_real_gemini_key
```

## 4. 프론트엔드 Dockerfile 설명

`frontend/Dockerfile`은 멀티 스테이지 빌드입니다.

1. `node:22-alpine` build 단계에서 `npm ci` 후 `npm run build`를 실행합니다.
2. `VITE_API_BASE_URL`은 Vite 특성상 빌드 시점에 주입됩니다.
3. runtime 단계에서는 `serve`로 `dist` 정적 파일을 `0.0.0.0:${PORT}`에 서빙합니다.
4. Render Web Service의 기본 포트인 `10000`을 기본값으로 사용합니다.

로컬 Docker 테스트 예시:

```bash
cd frontend
docker build --build-arg VITE_API_BASE_URL=http://localhost:8000 -t careerfit-frontend .
docker run --rm -p 10000:10000 careerfit-frontend
```

## 5. Render Docker Web Service 배포 과정

Render 공식 문서 기준으로 Docker 배포는 서비스 생성 시 Language를 `Docker`로 선택하고, Dockerfile이 루트가 아닌 위치에 있으면 Dockerfile Path를 지정합니다. Web Service는 `0.0.0.0`의 포트에 바인딩해야 하며 기본 포트는 `10000`입니다.

1. GitHub에 변경사항을 push합니다.
2. Render Dashboard에서 `New > Web Service`를 선택합니다.
3. GitHub 저장소를 연결합니다.
4. 서비스 이름을 정합니다. 예: `careerfit-frontend`.
5. Language를 `Docker`로 선택합니다.
6. Root Directory는 비워둡니다.
7. Dockerfile Path에 `frontend/Dockerfile`을 입력합니다.
8. Environment Variables에 `VITE_API_BASE_URL`을 추가합니다.
9. Create Web Service를 눌러 배포합니다.
10. 배포가 끝나면 발급된 `https://your-frontend-service.onrender.com` 주소를 확인합니다.

참고 문서:

- [Render Docker deploys](https://render.com/docs/docker)
- [Render Web Services and port binding](https://render.com/docs/web-services)

## 6. Render 환경변수 설정값

프론트엔드 Web Service:

```env
VITE_API_BASE_URL=https://careerfit-ai-q80r.onrender.com
```

백엔드 Web Service:

```env
FRONTEND_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,https://your-frontend-service.onrender.com
GEMINI_API_KEY=your_real_gemini_key
```

## 7. 배포 후 확인 방법

1. 백엔드 `https://your-backend-service.onrender.com/health`가 응답하는지 확인합니다.
2. 프론트엔드 `https://your-frontend-service.onrender.com`에 접속합니다.
3. 브라우저 개발자도구 Network 탭에서 `/analyze` 요청이 Render 백엔드 URL로 나가는지 확인합니다.
4. 분석 요청이 성공하면 화면에 결과와 sources가 표시되는지 확인합니다.

## 8. CORS 오류 해결 방법

브라우저 콘솔에 CORS 오류가 보이면 아래를 확인합니다.

1. 백엔드 `FRONTEND_ORIGINS`에 프론트엔드 주소가 정확히 들어갔는지 확인합니다.
2. origin에는 경로를 넣지 않습니다. 예: `https://careerfit-frontend.onrender.com/analyze`가 아니라 `https://careerfit-frontend.onrender.com`.
3. 쉼표 사이 값에 오타나 공백이 있어도 백엔드에서 trim되지만, 주소 자체의 마지막 슬래시는 넣지 않는 편이 좋습니다.
4. 환경변수 변경 후 백엔드 서비스를 재배포합니다.

## 9. Git에 올리면 안 되는 파일 목록

아래 파일과 폴더는 GitHub에 올리지 않습니다.

```text
.env
.env.*
frontend/.env
backend/.env
node_modules/
dist/
__pycache__/
pycache/
.venv/
venv/
```

`.env.example`은 실제 키가 없는 예시 파일이므로 Git에 올려도 됩니다.
