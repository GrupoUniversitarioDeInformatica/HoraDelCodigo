FROM python:3.12-slim

WORKDIR /app

# Copia requirements primero para aprovechar la cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del backend
COPY . .

# Ajusta este CMD a tu framework (ejemplo FastAPI con Uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
