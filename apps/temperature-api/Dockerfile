FROM python:3.12-slim

WORKDIR /app

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

COPY main.py /app
COPY is_ready.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
