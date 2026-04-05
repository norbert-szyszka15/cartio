FROM python:3.14.3-slim

# env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# workdir
WORKDIR /app

# system deps (opcjonalne)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app
COPY app ./app

# port
EXPOSE 8000

# start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]