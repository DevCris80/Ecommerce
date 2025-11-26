FROM python:3.12-slim

WORKDIR /app

# Instalar 'uv' y las dependencias del proyecto en un solo paso
# Esto garantiza que 'uv' esté disponible y que uvicorn sea accesible
# (Asumiendo que 'uvicorn' está en tu uv.lock)
COPY pyproject.toml uv.lock ./
RUN pip install uv && \
    uv sync --frozen

# El resto sigue igual
COPY app ./app

EXPOSE 8000