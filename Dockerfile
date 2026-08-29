# Stage 1: Frontend Stage
FROM node:alpine AS frontend
WORKDIR /app
COPY package.json .
COPY /app/static/src .
RUN npm install
RUN npm run build

# Stage 2: Backend Stage
FROM python:3.14 AS backend
WORKDIR /app
COPY /app ./app
COPY app.py .
COPY /calculation ./calculation
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY --from=frontend /app/output.css .
EXPOSE 8080
CMD ["python3", "app.py"]


 