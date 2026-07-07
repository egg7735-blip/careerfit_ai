FROM node:22-alpine AS build

WORKDIR /app

ARG VITE_API_BASE_URL=http://localhost:8000
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ .
RUN npm run build

FROM node:22-alpine AS runtime

WORKDIR /app

ENV PORT=10000
RUN npm install -g serve@14

COPY --from=build /app/dist ./dist

EXPOSE 10000

CMD ["sh", "-c", "serve -s dist -l tcp://0.0.0.0:${PORT}"]
