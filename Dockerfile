FROM python:latest
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 3000
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
